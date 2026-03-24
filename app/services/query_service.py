"""Service layer for ERP context-aware grounded question answering."""

from __future__ import annotations

import logging

from app.context import normalize_query_request, summarize_screen_context
from app.core.config import Settings
from app.domain.schemas import (
    GeneratedAnswer,
    KnowledgeCitation,
    QueryRequest,
    QueryResponse,
    QuerySource,
)
from app.llm import AnswerGenerator
from app.retrieval import QdrantRetriever, RetrievalRouter
from app.security import redact_screen_context

logger = logging.getLogger(__name__)


class QueryService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._validate_settings()
        self.retriever = QdrantRetriever(settings=settings)
        self.retrieval_router = RetrievalRouter(settings=settings, retriever=self.retriever)
        self.generator = AnswerGenerator(settings=settings)

    def run(self, request: QueryRequest) -> QueryResponse:
        normalized_request = normalize_query_request(
            request=request,
            default_locale=self.settings.default_locale,
        )
        redaction = redact_screen_context(
            normalized_request.screen_context,
            allowlist=self.settings.redaction_allowlist,
            denylist=self.settings.redaction_denylist,
        )
        summary = summarize_screen_context(redaction.screen_context)

        if self._needs_clarification(normalized_request):
            return QueryResponse(
                answer="Mi serve piu contesto per capire su quale procedura ERP devo guidarti.",
                steps=[],
                citations=[],
                follow_up_question="Quale operazione vuoi completare e in quale schermata o modulo ti trovi?",
                confidence=0.1,
                used_screen_context=summary,
                redaction_notice=redaction.notice,
                answer_mode="clarification",
                inference_notice=None,
            )

        query_plan, sources = self.retrieval_router.search(
            request=normalized_request,
            screen_context=redaction.screen_context,
        )

        logger.info(
            "ERP query processed",
            extra={
                "conversation_id": normalized_request.conversation_id,
                "module": summary.module,
                "screen_id": summary.screen_id,
                "intent": query_plan.intent_label,
                "retrieved_chunks": len(sources),
                "redacted_fields": len(redaction.redacted_fields),
                "top_retrieval_reasons": sources[0].retrieval_reasons if sources else [],
            },
        )

        if not sources:
            return QueryResponse(
                answer=(
                    "Non ho trovato fonti approvate abbastanza pertinenti per rispondere in modo sicuro "
                    "alla tua richiesta."
                ),
                steps=[],
                citations=[],
                follow_up_question="Puoi indicarmi il modulo, la schermata o l'errore preciso che stai vedendo?",
                confidence=0.15,
                used_screen_context=summary,
                redaction_notice=redaction.notice,
                answer_mode="clarification",
                inference_notice=None,
            )

        generated = self.generator.generate(
            message=normalized_request.message,
            screen_context=redaction.screen_context,
            query_plan=query_plan,
            sources=sources,
        )

        allow_inferred_guidance = (
            normalized_request.retrieval_options.allow_inferred_guidance
            if normalized_request.retrieval_options
            else True
        )
        answer_mode = self._resolve_answer_mode(generated, sources, allow_inferred_guidance)
        if answer_mode == "clarification" and not generated.follow_up_question:
            generated.follow_up_question = "Mi indichi il nome esatto della schermata o il testo dell'errore?"

        if answer_mode == "partial_inference" and not generated.inference_notice:
            generated.inference_notice = (
                "La risposta combina fonti ERP recuperate con inferenze generali esplicitamente separate."
            )

        confidence = self._combine_confidence(generated, sources)
        return QueryResponse(
            answer=generated.answer,
            steps=generated.steps if answer_mode != "clarification" else [],
            citations=[self._to_citation(source) for source in sources],
            follow_up_question=generated.follow_up_question,
            confidence=confidence,
            used_screen_context=summary,
            redaction_notice=redaction.notice,
            answer_mode=answer_mode,
            inference_notice=generated.inference_notice,
        )

    def _to_citation(self, source: QuerySource) -> KnowledgeCitation:
        return KnowledgeCitation(
            chunk_id=source.chunk_id,
            title=source.title,
            section_title=source.section_title,
            source_uri=source.source_uri,
            doc_type=source.doc_type,
            doc_kind=source.doc_kind,
            domain=source.domain,
            feature=source.feature,
            module=source.module,
            screen_title=source.screen_title,
            tab_name=source.tab_name,
            score=source.score,
        )

    def _needs_clarification(self, request: QueryRequest) -> bool:
        context = request.screen_context
        has_location = bool(context.module or context.screen_title or context.screen_id)
        has_evidence = bool(context.fields or context.error_messages or context.free_text_context)
        return len(request.message.strip()) < 12 and not has_location and not has_evidence

    def _resolve_answer_mode(
        self,
        generated: GeneratedAnswer,
        sources: list[QuerySource],
        allow_inferred_guidance: bool,
    ) -> str:
        if not sources:
            return "clarification"

        top_score = max(min(sources[0].score, 1.0), 0.0)
        if not allow_inferred_guidance and generated.answer_mode == "partial_inference":
            return "clarification"
        if generated.answer_mode == "clarification":
            return "clarification"
        if generated.answer_mode == "partial_inference":
            return "partial_inference"
        if top_score < 0.3 and allow_inferred_guidance:
            return "partial_inference"
        if top_score < 0.2:
            return "clarification"
        return "grounded"

    def _combine_confidence(self, generated: GeneratedAnswer, sources: list[QuerySource]) -> float | None:
        if not sources and generated.confidence is None:
            return None

        retrieval_confidence = min(
            1.0,
            sum(max(min(source.score, 1.0), 0.0) for source in sources[:3]) / max(1, min(len(sources), 3)),
        )
        if generated.confidence is None:
            return round(retrieval_confidence, 2)
        return round(min(1.0, (0.65 * retrieval_confidence) + (0.35 * generated.confidence)), 2)

    def _validate_settings(self) -> None:
        missing = self.settings.missing_required_env
        if missing:
            raise RuntimeError(
                "Missing required configuration: " + ", ".join(missing)
            )
