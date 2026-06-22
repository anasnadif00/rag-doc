"""Retrieval routing, reciprocal-rank fusion, and semantic reranking."""

from __future__ import annotations

from typing import Any

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
from app.retrieval.reranker import OpenAIReranker, RerankOutcome


RRF_K = 60


class RetrievalRouter:
    def __init__(
        self,
        settings: Settings,
        retriever: QdrantRetriever,
        lexical_retriever: LexicalRetriever | None = None,
        query_planner: QueryPlanner | None = None,
        reranker: Any | None = None,
    ) -> None:
        self.settings = settings
        self.retriever = retriever
        self.lexical_retriever = lexical_retriever or LexicalRetriever(settings=settings)
        self.query_planner = query_planner or QueryPlanner(settings=settings)
        self.reranker = reranker or OpenAIReranker(settings=settings)
        self.last_diagnostics: RetrievalDiagnostics | None = None

    def search(
        self,
        request: QueryRequest,
        screen_context: ScreenContext,
        conversation_history: list[dict[str, str]] | None = None,
        additional_retrievers: list[tuple[str, QdrantRetriever]] | None = None,
    ) -> tuple[QueryPlan, list[QuerySource]]:
        plan = self.query_planner.build(request=request, screen_context=screen_context)
        retrieval_options = request.retrieval_options
        final_limit = (
            retrieval_options.top_k
            if retrieval_options and retrieval_options.top_k is not None
            else max(6, self.settings.top_k)
        )

        candidates, rankings = self._collect_candidates(
            plan=plan,
            retrieval_options=retrieval_options,
            additional_retrievers=additional_retrievers or [],
        )
        fused = self._fuse_candidates(candidates, rankings)
        rerank_pool = fused[: self.settings.rerank_candidate_limit]
        excluded = fused[self.settings.rerank_candidate_limit :]
        for candidate in excluded:
            candidate.selected = False
            candidate.selection_reason = (
                f"excluded before rerank by candidate limit {self.settings.rerank_candidate_limit}"
            )

        ranking_method = "rrf"
        rerank_status = "skipped"
        fallback_reason: str | None = None
        rerank_outcome: RerankOutcome | None = None
        fallback_prompt_tokens = 0
        fallback_completion_tokens = 0
        ranked = rerank_pool
        if rerank_pool:
            try:
                rerank_outcome = self.reranker.rerank(
                    message=request.message,
                    screen_context=screen_context,
                    query_plan=plan,
                    candidates=rerank_pool,
                    conversation_history=conversation_history,
                )
                ranked = self._apply_rerank(rerank_pool, rerank_outcome)
                plan.question_type = rerank_outcome.question_type
                plan.subjects = rerank_outcome.subjects
                ranking_method = "openai_rerank"
                rerank_status = "succeeded"
            except Exception as exc:
                ranked = self._apply_rrf_fallback(rerank_pool)
                rerank_status = "fallback"
                fallback_reason = f"{type(exc).__name__}: reranker unavailable or invalid"
                fallback_prompt_tokens = getattr(exc, "prompt_tokens", 0) or 0
                fallback_completion_tokens = getattr(exc, "completion_tokens", 0) or 0

        score_floor, eligible = self._apply_score_cutoff(ranked)
        returned = self._apply_result_limit(eligible, final_limit)
        all_diagnostics_candidates = [*ranked, *excluded]
        self.last_diagnostics = self._build_diagnostics(
            plan=plan,
            ranked=all_diagnostics_candidates,
            returned=returned,
            score_floor=score_floor,
            ranking_method=ranking_method,
            rerank_status=rerank_status,
            fallback_reason=fallback_reason,
            rerank_outcome=rerank_outcome,
            fallback_prompt_tokens=fallback_prompt_tokens,
            fallback_completion_tokens=fallback_completion_tokens,
        )
        return plan, [candidate.source for candidate in returned]

    def _collect_candidates(
        self,
        *,
        plan: QueryPlan,
        retrieval_options: Any,
        additional_retrievers: list[tuple[str, QdrantRetriever]],
    ) -> tuple[dict[str, RetrievalCandidate], list[list[str]]]:
        candidate_map: dict[str, RetrievalCandidate] = {}
        rankings: list[list[str]] = []
        score_threshold = retrieval_options.score_threshold if retrieval_options else None
        dense_retrievers = [("base", self.retriever), *additional_retrievers]

        for scope in plan.scope_order:
            for source_name, retriever in dense_retrievers:
                dense_results = retriever.search(
                    query_text=plan.semantic_query,
                    limit=self.settings.dense_candidate_limit,
                    metadata_filter=self._build_dense_filter(plan, scope),
                    score_threshold=score_threshold,
                )
                dense_ranking: list[str] = []
                for source in dense_results:
                    if not self._matches_post_filters(source, plan):
                        continue
                    dense_ranking.append(source.chunk_id)
                    reasons = [f"match semantico su scope {scope}"]
                    is_overlay = source_name != "base"
                    if is_overlay:
                        reasons.append("match tenant overlay")
                    self._merge_candidate(
                        candidate_map,
                        RetrievalCandidate(
                            source=source,
                            dense_score=source.score,
                            scope=scope,
                            is_tenant_overlay=is_overlay,
                            retrieval_reasons=reasons,
                        ),
                    )
                if dense_ranking:
                    rankings.append(dense_ranking)

            lexical_results = self.lexical_retriever.search(
                plan=plan,
                scope=scope,
                limit=self.settings.lexical_candidate_limit,
            )
            if lexical_results:
                rankings.append([candidate.source.chunk_id for candidate in lexical_results])
                for candidate in lexical_results:
                    self._merge_candidate(candidate_map, candidate)

            exact_results = self.lexical_retriever.exact_match(
                plan=plan,
                scope=scope,
                limit=self.settings.lexical_candidate_limit,
            )
            if exact_results:
                rankings.append([candidate.source.chunk_id for candidate in exact_results])
                for candidate in exact_results:
                    self._merge_candidate(candidate_map, candidate)

        return candidate_map, rankings

    def _build_dense_filter(self, plan: QueryPlan, scope: str) -> Filter | None:
        conditions: list[FieldCondition] = []
        review_statuses = self._as_list(plan.hard_filters.get("review_status"))
        doc_kinds = self._as_list(plan.hard_filters.get("doc_kinds"))
        if review_statuses:
            conditions.append(
                FieldCondition(key="metadata.review_status", match=MatchAny(any=review_statuses))
            )
        if doc_kinds:
            conditions.append(FieldCondition(key="metadata.doc_kind", match=MatchAny(any=doc_kinds)))

        modules = plan.soft_signals.get("module", [])
        submenus = plan.soft_signals.get("submenu", [])
        screen_ids = plan.soft_signals.get("screen_id", [])
        screen_titles = plan.soft_signals.get("screen_title", [])
        tab_names = plan.soft_signals.get("tab_name", [])

        if scope in {"screen", "module"} and modules:
            conditions.append(FieldCondition(key="metadata.module", match=MatchValue(value=modules[0])))
        if scope == "screen":
            if screen_ids:
                conditions.append(
                    FieldCondition(key="metadata.screen_id", match=MatchValue(value=screen_ids[0]))
                )
            elif screen_titles:
                conditions.append(
                    FieldCondition(key="metadata.screen_title", match=MatchValue(value=screen_titles[0]))
                )
            if tab_names:
                conditions.append(
                    FieldCondition(key="metadata.tab_name", match=MatchValue(value=tab_names[0]))
                )
        elif scope == "module" and submenus:
            conditions.append(FieldCondition(key="metadata.submenu", match=MatchValue(value=submenus[0])))
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

        requested_doc_kinds = {
            value.lower() for value in self._as_list(plan.hard_filters.get("doc_kinds"))
        }
        return not requested_doc_kinds or str(source.doc_kind or "").lower() in requested_doc_kinds

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
        if incoming.is_tenant_overlay and not existing.is_tenant_overlay:
            existing.source = incoming.source
        existing.is_tenant_overlay = existing.is_tenant_overlay or incoming.is_tenant_overlay
        if self._scope_rank(incoming.scope) > self._scope_rank(existing.scope):
            existing.scope = incoming.scope
        existing.retrieval_reasons = list(
            dict.fromkeys(existing.retrieval_reasons + incoming.retrieval_reasons)
        )

    def _fuse_candidates(
        self,
        candidate_map: dict[str, RetrievalCandidate],
        rankings: list[list[str]],
    ) -> list[RetrievalCandidate]:
        raw_scores = {chunk_id: 0.0 for chunk_id in candidate_map}
        for ranking in rankings:
            for rank, chunk_id in enumerate(dict.fromkeys(ranking), start=1):
                if chunk_id in raw_scores:
                    raw_scores[chunk_id] += 1.0 / (RRF_K + rank)

        maximum = max(raw_scores.values(), default=0.0)
        for chunk_id, candidate in candidate_map.items():
            candidate.rrf_score = raw_scores[chunk_id] / maximum if maximum > 0 else 0.0
            candidate.final_score = self._with_overlay_boost(candidate.rrf_score, candidate)
            candidate.ranking_method = "rrf"
            candidate.source.score = round(candidate.final_score, 4)
            candidate.source.retrieval_reasons = list(dict.fromkeys(candidate.retrieval_reasons))
        return sorted(candidate_map.values(), key=lambda item: item.final_score, reverse=True)

    def _apply_rerank(
        self,
        candidates: list[RetrievalCandidate],
        outcome: RerankOutcome,
    ) -> list[RetrievalCandidate]:
        score_by_id = {score.chunk_id: score for score in outcome.candidates}
        for candidate in candidates:
            score = score_by_id[candidate.source.chunk_id]
            candidate.rerank_score = score.relevance_score
            candidate.rerank_reason = score.reason
            candidate.ranking_method = "openai_rerank"
            candidate.final_score = self._with_overlay_boost(score.relevance_score, candidate)
            candidate.retrieval_reasons.append(f"rerank semantico: {score.reason}")
            candidate.source.score = round(candidate.final_score, 4)
            candidate.source.retrieval_reasons = list(dict.fromkeys(candidate.retrieval_reasons))
        return sorted(candidates, key=lambda item: (item.final_score, item.rrf_score), reverse=True)

    def _apply_rrf_fallback(self, candidates: list[RetrievalCandidate]) -> list[RetrievalCandidate]:
        for candidate in candidates:
            candidate.ranking_method = "rrf"
            candidate.final_score = self._with_overlay_boost(candidate.rrf_score, candidate)
            candidate.source.score = round(candidate.final_score, 4)
            candidate.source.retrieval_reasons = list(dict.fromkeys(candidate.retrieval_reasons))
        return sorted(candidates, key=lambda item: item.final_score, reverse=True)

    def _with_overlay_boost(self, score: float, candidate: RetrievalCandidate) -> float:
        if candidate.is_tenant_overlay:
            return min(1.0, score + self.settings.overlay_score_boost)
        return min(1.0, score)

    def _apply_score_cutoff(
        self,
        candidates: list[RetrievalCandidate],
    ) -> tuple[float | None, list[RetrievalCandidate]]:
        if not candidates:
            return None, []

        top_score = candidates[0].final_score
        minimum = self.settings.rerank_min_score
        if top_score < minimum:
            reason = f"top score {top_score:.4f} below minimum {minimum:.4f}"
            for candidate in candidates:
                candidate.selected = False
                candidate.selection_reason = reason
            return minimum, []

        score_floor = max(minimum, top_score * self.settings.retrieval_relative_score_floor)
        eligible: list[RetrievalCandidate] = []
        for index, candidate in enumerate(candidates):
            if index == 0 or candidate.final_score >= score_floor:
                candidate.selected = True
                candidate.selection_reason = (
                    "top ranked candidate"
                    if index == 0
                    else f"score {candidate.final_score:.4f} above floor {score_floor:.4f}"
                )
                eligible.append(candidate)
            else:
                candidate.selected = False
                candidate.selection_reason = (
                    f"score {candidate.final_score:.4f} below floor {score_floor:.4f}"
                )
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
                returned.append(candidate)
            else:
                candidate.selected = False
                candidate.selection_reason = f"trimmed by top_k {final_limit}"
        return returned

    def _build_diagnostics(
        self,
        *,
        plan: QueryPlan,
        ranked: list[RetrievalCandidate],
        returned: list[RetrievalCandidate],
        score_floor: float | None,
        ranking_method: str,
        rerank_status: str,
        fallback_reason: str | None,
        rerank_outcome: RerankOutcome | None,
        fallback_prompt_tokens: int,
        fallback_completion_tokens: int,
    ) -> RetrievalDiagnostics:
        return RetrievalDiagnostics(
            query_plan=plan,
            active_filters=plan.hard_filters,
            semantic_query=plan.semantic_query,
            lexical_index_path=self.settings.lexical_index_path,
            candidate_count=len(ranked),
            returned_count=len(returned),
            score_floor=round(score_floor, 4) if score_floor is not None else None,
            ranking_method=ranking_method,
            rerank_status=rerank_status,
            rerank_model=self.settings.rerank_model or self.settings.generation_model,
            rerank_fallback_reason=fallback_reason,
            rerank_prompt_tokens=(
                rerank_outcome.prompt_tokens if rerank_outcome else fallback_prompt_tokens
            ),
            rerank_completion_tokens=(
                rerank_outcome.completion_tokens if rerank_outcome else fallback_completion_tokens
            ),
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
                    rrf_score=round(candidate.rrf_score, 4),
                    rerank_score=(
                        round(candidate.rerank_score, 4)
                        if candidate.rerank_score is not None
                        else None
                    ),
                    rerank_reason=candidate.rerank_reason,
                    ranking_method=candidate.ranking_method,
                    is_tenant_overlay=candidate.is_tenant_overlay,
                    selected=candidate.selected,
                    selection_reason=candidate.selection_reason,
                    retrieval_reasons=candidate.source.retrieval_reasons,
                )
                for candidate in ranked
            ],
        )

    def _scope_rank(self, scope: str) -> int:
        return {"global": 0, "module": 1, "screen": 2}.get(scope, 0)

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
