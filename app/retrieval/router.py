"""Retrieval routing for ERP-aware metadata filters and hybrid fusion."""

from __future__ import annotations

from qdrant_client.http.models import FieldCondition, Filter, MatchAny, MatchValue

from app.core.config import Settings
from app.domain.schemas import QueryPlan, QueryRequest, QuerySource, RetrievalCandidate, ScreenContext
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
        return plan, [candidate.source for candidate in ranked[:final_limit]]

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
        requested_versions = {value.lower() for value in self._as_list(plan.hard_filters.get("erp_versions"))}
        source_versions = {value.lower() for value in source.erp_versions}
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
            candidate.version_match = 1.0 if not candidate.source.erp_versions else self._intersects(
                candidate.source.erp_versions,
                self._as_list(plan.hard_filters.get("erp_versions")),
            )

            exact_bonus = 0.25 * normalized_exact
            candidate.final_score = (
                0.45 * normalized_dense
                + 0.25 * normalized_lexical
                + 0.10 * candidate.doc_kind_match
                + 0.10 * candidate.scope_specificity
                + 0.05 * candidate.role_match
                + 0.05 * candidate.version_match
                + exact_bonus
            )
            candidate.source.score = round(candidate.final_score, 4)
            candidate.source.retrieval_reasons = list(dict.fromkeys(candidate.retrieval_reasons))

        candidates.sort(key=lambda item: item.final_score, reverse=True)
        return candidates

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
