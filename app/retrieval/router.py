"""Retrieval routing for ERP-aware metadata filters and hybrid fusion."""

from __future__ import annotations

from qdrant_client.http.models import FieldCondition, Filter, MatchAny, MatchValue

from app.core.config import Settings
from app.core.normalization import normalize_erp_version
from app.domain.schemas import (
    QueryPlan,
    QueryRequest,
    QuerySource,
    RetrievalCandidate,
    RetrievalCandidateDebug,
    RetrievalDiagnostics,
    ScreenContext,
)
from app.retrieval.lexical_retriever import LexicalRetriever
from app.retrieval.qdrant_retriever import QdrantRetriever
from app.retrieval.query_planner import QueryPlanner


class RetrievalRouter:
    def __init__(
        self,
        settings: Settings,
        retriever: QdrantRetriever,
        lexical_retriever: LexicalRetriever | None = None,
        query_planner: QueryPlanner | None = None,
    ) -> None:
        self.settings = settings
        self.retriever = retriever
        self.lexical_retriever = lexical_retriever or LexicalRetriever(settings=settings)
        self.query_planner = query_planner or QueryPlanner(settings=settings)
        self.last_diagnostics: RetrievalDiagnostics | None = None

    def search(
        self,
        request: QueryRequest,
        screen_context: ScreenContext,
    ) -> tuple[QueryPlan, list[QuerySource]]:
        plan = self.query_planner.build(request=request, screen_context=screen_context)
        retrieval_options = request.retrieval_options
        dense_limit = self.settings.dense_candidate_limit
        lexical_limit = self.settings.lexical_candidate_limit
        score_threshold = retrieval_options.score_threshold if retrieval_options else None
        final_limit = retrieval_options.top_k if retrieval_options and retrieval_options.top_k is not None else max(6, self.settings.top_k)

        candidate_map: dict[str, RetrievalCandidate] = {}
        for scope in plan.scope_order:
            dense_results = self.retriever.search(
                query_text=plan.semantic_query,
                limit=dense_limit,
                metadata_filter=self._build_dense_filter(plan, scope),
                score_threshold=score_threshold,
            )
            for source in dense_results:
                if not self._matches_post_filters(source, plan):
                    continue
                self._merge_candidate(
                    candidate_map,
                    RetrievalCandidate(
                        source=source,
                        dense_score=source.score,
                        scope=scope,
                        retrieval_reasons=[f"match semantico su scope {scope}"],
                    ),
                )

            for candidate in self.lexical_retriever.search(plan=plan, scope=scope, limit=lexical_limit):
                self._merge_candidate(candidate_map, candidate)

            for candidate in self.lexical_retriever.exact_match(plan=plan, scope=scope, limit=lexical_limit):
                self._merge_candidate(candidate_map, candidate)

        ranked = self._rerank(list(candidate_map.values()), plan)
        score_floor, eligible = self._apply_score_cutoff(ranked)
        returned = self._apply_result_limit(eligible, final_limit)
        self.last_diagnostics = self._build_diagnostics(
            plan=plan,
            ranked=ranked,
            returned=returned,
            score_floor=score_floor,
        )
        return plan, [candidate.source for candidate in returned]

    def _build_dense_filter(self, plan: QueryPlan, scope: str) -> Filter | None:
        conditions: list[FieldCondition] = [
            FieldCondition(
                key="metadata.review_status",
                match=MatchAny(any=self._as_list(plan.hard_filters.get("review_status"))),
            ),
            FieldCondition(
                key="metadata.doc_kind",
                match=MatchAny(any=self._as_list(plan.hard_filters.get("doc_kinds"))),
            ),
        ]

        modules = plan.soft_signals.get("module", [])
        submenus = plan.soft_signals.get("submenu", [])
        screen_ids = plan.soft_signals.get("screen_id", [])
        screen_titles = plan.soft_signals.get("screen_title", [])
        tab_names = plan.soft_signals.get("tab_name", [])

        if scope in {"screen", "module"} and modules:
            conditions.append(
                FieldCondition(
                    key="metadata.module",
                    match=MatchValue(value=modules[0]),
                )
            )

        if scope == "screen":
            if screen_ids:
                conditions.append(
                    FieldCondition(
                        key="metadata.screen_id",
                        match=MatchValue(value=screen_ids[0]),
                    )
                )
            elif screen_titles:
                conditions.append(
                    FieldCondition(
                        key="metadata.screen_title",
                        match=MatchValue(value=screen_titles[0]),
                    )
                )
            if tab_names:
                conditions.append(
                    FieldCondition(
                        key="metadata.tab_name",
                        match=MatchValue(value=tab_names[0]),
                    )
                )
        elif scope == "module" and submenus:
            conditions.append(
                FieldCondition(
                    key="metadata.submenu",
                    match=MatchValue(value=submenus[0]),
                )
            )

        return Filter(must=conditions) if conditions else None

    def _matches_post_filters(self, source: QuerySource, plan: QueryPlan) -> bool:
        requested_versions = self._normalized_erp_versions(plan.hard_filters.get("erp_versions"))
        source_versions = self._normalized_erp_versions(source.erp_versions)
        if requested_versions and source_versions and not (requested_versions & source_versions):
            return False

        requested_roles = {value.lower() for value in self._as_list(plan.hard_filters.get("role_scope"))}
        source_roles = {value.lower() for value in source.role_scope}
        if requested_roles and source_roles and not (requested_roles & source_roles):
            return False
        return True

    def _merge_candidate(
        self,
        candidate_map: dict[str, RetrievalCandidate],
        incoming: RetrievalCandidate,
    ) -> None:
        existing = candidate_map.get(incoming.source.chunk_id)
        if not existing:
            candidate_map[incoming.source.chunk_id] = incoming
            return

        existing.dense_score = max(existing.dense_score, incoming.dense_score)
        existing.lexical_score = max(existing.lexical_score, incoming.lexical_score)
        existing.exact_match_score = max(existing.exact_match_score, incoming.exact_match_score)
        if self._scope_rank(incoming.scope) > self._scope_rank(existing.scope):
            existing.scope = incoming.scope
        existing.retrieval_reasons = list(dict.fromkeys(existing.retrieval_reasons + incoming.retrieval_reasons))

    def _rerank(self, candidates: list[RetrievalCandidate], plan: QueryPlan) -> list[RetrievalCandidate]:
        dense_scores = [candidate.dense_score for candidate in candidates]
        lexical_scores = [candidate.lexical_score for candidate in candidates]
        exact_scores = [candidate.exact_match_score for candidate in candidates]

        for candidate in candidates:
            normalized_dense = self._normalize(candidate.dense_score, dense_scores)
            normalized_lexical = self._normalize(candidate.lexical_score, lexical_scores)
            normalized_exact = self._normalize(candidate.exact_match_score, exact_scores)
            candidate.normalized_dense = normalized_dense
            candidate.normalized_lexical = normalized_lexical
            candidate.normalized_exact = normalized_exact
            candidate.doc_kind_match = self._doc_kind_match(candidate.source, plan)
            candidate.scope_specificity = {
                "screen": 1.0,
                "module": 0.6,
                "global": 0.3,
            }[candidate.scope]
            candidate.role_match = 1.0 if not candidate.source.role_scope else self._intersects(
                candidate.source.role_scope,
                self._as_list(plan.hard_filters.get("role_scope")),
            )
            candidate.version_match = 1.0 if not candidate.source.erp_versions else self._version_intersects(
                candidate.source.erp_versions,
                self._as_list(plan.hard_filters.get("erp_versions")),
            )

            exact_bonus = 0.25 * normalized_exact
            candidate.final_score = (
                0.40 * normalized_dense
                + 0.25 * normalized_lexical
                + 0.15 * candidate.doc_kind_match
                + 0.10 * candidate.scope_specificity
                + 0.05 * candidate.role_match
                + 0.05 * candidate.version_match
                + exact_bonus
            )
            candidate.source.score = round(candidate.final_score, 4)
            candidate.source.retrieval_reasons = list(dict.fromkeys(candidate.retrieval_reasons))

        candidates.sort(key=lambda item: item.final_score, reverse=True)
        return candidates

    def _apply_score_cutoff(self, candidates: list[RetrievalCandidate]) -> tuple[float | None, list[RetrievalCandidate]]:
        if not candidates:
            return None, []

        top_score = candidates[0].final_score
        if top_score < self.settings.retrieval_min_score:
            reason = (
                f"top score {top_score:.4f} below minimum "
                f"{self.settings.retrieval_min_score:.4f}"
            )
            for candidate in candidates:
                candidate.selected = False
                candidate.selection_reason = reason
            return self.settings.retrieval_min_score, []

        score_floor = max(
            self.settings.retrieval_min_score,
            top_score * self.settings.retrieval_relative_score_floor,
        )
        eligible: list[RetrievalCandidate] = []
        for index, candidate in enumerate(candidates):
            if index == 0:
                candidate.selected = True
                candidate.selection_reason = "top ranked candidate"
                eligible.append(candidate)
                continue

            if candidate.exact_match_score > 0 and candidate.final_score >= self.settings.retrieval_min_score:
                candidate.selected = True
                candidate.selection_reason = "passed exact-match safeguard"
                eligible.append(candidate)
                continue

            if candidate.final_score >= score_floor:
                candidate.selected = True
                candidate.selection_reason = f"score {candidate.final_score:.4f} above floor {score_floor:.4f}"
                eligible.append(candidate)
                continue

            candidate.selected = False
            candidate.selection_reason = f"score {candidate.final_score:.4f} below floor {score_floor:.4f}"
        return score_floor, eligible

    def _apply_result_limit(
        self,
        candidates: list[RetrievalCandidate],
        final_limit: int,
    ) -> list[RetrievalCandidate]:
        returned: list[RetrievalCandidate] = []
        for index, candidate in enumerate(candidates):
            if index < final_limit:
                candidate.selected = True
                if candidate.selection_reason != "top ranked candidate":
                    candidate.selection_reason = (
                        candidate.selection_reason or f"returned in top_k {final_limit}"
                    )
                returned.append(candidate)
                continue

            candidate.selected = False
            candidate.selection_reason = f"trimmed by top_k {final_limit}"
        return returned

    def _build_diagnostics(
        self,
        plan: QueryPlan,
        ranked: list[RetrievalCandidate],
        returned: list[RetrievalCandidate],
        score_floor: float | None,
    ) -> RetrievalDiagnostics:
        return RetrievalDiagnostics(
            query_plan=plan,
            active_filters=plan.hard_filters,
            semantic_query=plan.semantic_query,
            lexical_index_path=self.settings.lexical_index_path,
            candidate_count=len(ranked),
            returned_count=len(returned),
            score_floor=round(score_floor, 4) if score_floor is not None else None,
            returned_chunk_ids=[candidate.source.chunk_id for candidate in returned],
            candidates=[
                RetrievalCandidateDebug(
                    chunk_id=candidate.source.chunk_id,
                    title=candidate.source.title,
                    doc_kind=candidate.source.doc_kind,
                    source_uri=candidate.source.source_uri,
                    scope=candidate.scope,
                    score=round(candidate.final_score, 4),
                    dense_score=round(candidate.dense_score, 4),
                    lexical_score=round(candidate.lexical_score, 4),
                    exact_match_score=round(candidate.exact_match_score, 4),
                    normalized_dense=round(candidate.normalized_dense, 4),
                    normalized_lexical=round(candidate.normalized_lexical, 4),
                    normalized_exact=round(candidate.normalized_exact, 4),
                    doc_kind_match=round(candidate.doc_kind_match, 4),
                    scope_specificity=round(candidate.scope_specificity, 4),
                    role_match=round(candidate.role_match, 4),
                    version_match=round(candidate.version_match, 4),
                    selected=candidate.selected,
                    selection_reason=candidate.selection_reason,
                    retrieval_reasons=candidate.source.retrieval_reasons,
                )
                for candidate in ranked
            ],
        )

    def _doc_kind_match(self, source: QuerySource, plan: QueryPlan) -> float:
        if source.doc_kind not in plan.preferred_doc_kinds:
            return 0.0
        index = plan.preferred_doc_kinds.index(source.doc_kind)
        return max(0.2, 1.0 - (0.2 * index))

    def _normalize(self, value: float, series: list[float]) -> float:
        if not series:
            return 0.0
        minimum = min(series)
        maximum = max(series)
        if maximum == minimum:
            return 1.0 if value > 0 else 0.0
        return (value - minimum) / (maximum - minimum)

    def _scope_rank(self, scope: str) -> int:
        return {"global": 0, "module": 1, "screen": 2}.get(scope, 0)

    def _intersects(self, left: list[str], right: list[str]) -> float:
        if not left or not right:
            return 1.0
        return 1.0 if {value.lower() for value in left} & {value.lower() for value in right} else 0.0

    def _as_list(self, value: list[str] | str | None) -> list[str]:
        if value is None:
            return []
        if isinstance(value, list):
            return [str(item) for item in value if str(item).strip()]
        return [str(value)]

    def _normalized_erp_versions(self, value: list[str] | str | None) -> set[str]:
        normalized: set[str] = set()
        for item in self._as_list(value):
            version = normalize_erp_version(item)
            if version:
                normalized.add(version)
        return normalized

    def _version_intersects(self, left: list[str], right: list[str]) -> float:
        normalized_left = self._normalized_erp_versions(left)
        normalized_right = self._normalized_erp_versions(right)
        if not normalized_left or not normalized_right:
            return 1.0
        return 1.0 if normalized_left & normalized_right else 0.0
