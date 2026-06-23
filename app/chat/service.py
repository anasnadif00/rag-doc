"""Tenant-aware chat runtime built on top of the existing RAG service."""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.chat.memory import ConversationMemoryService
from app.chat.schemas import ChatTurnRequest, ChatTurnResponse, ChatUsage, ConversationMessage
from app.context import normalize_query_request, summarize_screen_context
from app.core.config import Settings
from app.core.runtime_config import get_runtime_settings
from app.domain.schemas import QueryRequest, QueryResponse, RetrievalOptions, UserContext
from app.persistence.repositories import AuditRepository, ChatSessionRepository
from app.retrieval import QdrantRetriever
from app.security import redact_screen_context
from app.services.query_service import QueryService
from app.tenancy.cache import AsyncStateStore
from app.tenancy.models import SessionPrincipal
from app.tenancy.services import QuotaService, TenantAccessService


class TenantAwareRAGService(QueryService):
    def __init__(self, settings: Settings, principal: SessionPrincipal) -> None:
        super().__init__(settings=settings)
        self.principal = principal
        self.last_usage = {"prompt_tokens": 0, "completion_tokens": 0}
        self.overlay_retriever: QdrantRetriever | None = None
        overlay_collection = self._overlay_collection_name()
        if overlay_collection:
            self.overlay_retriever = QdrantRetriever(
                settings=settings,
                collection_name=overlay_collection,
            )

    def run_chat_request(
        self,
        request: QueryRequest,
        *,
        conversation_history: list[ConversationMessage] | None = None,
    ) -> QueryResponse:
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

        history_payload = [item.model_dump(mode="json") for item in (conversation_history or [])]
        additional_retrievers = (
            [("tenant_overlay", self.overlay_retriever)]
            if self.overlay_retriever is not None
            else []
        )
        query_plan, sources = self.retrieval_router.search(
            request=normalized_request,
            screen_context=redaction.screen_context,
            conversation_history=history_payload,
            additional_retrievers=additional_retrievers,
        )
        diagnostics = getattr(self.retrieval_router, "last_diagnostics", None)
        self.last_usage = {
            "prompt_tokens": diagnostics.rerank_prompt_tokens if diagnostics else 0,
            "completion_tokens": diagnostics.rerank_completion_tokens if diagnostics else 0,
        }

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
                retrieval_diagnostics=self._maybe_include_diagnostics(normalized_request, diagnostics),
            )

        generated = self.generator.generate(
            message=normalized_request.message,
            screen_context=redaction.screen_context,
            query_plan=query_plan,
            sources=sources,
            conversation_history=history_payload,
        )
        self.last_usage = {
            "prompt_tokens": self.last_usage["prompt_tokens"] + generated.prompt_tokens,
            "completion_tokens": self.last_usage["completion_tokens"] + generated.completion_tokens,
        }

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

        return QueryResponse(
            answer=generated.answer,
            steps=generated.steps if answer_mode != "clarification" else [],
            citations=[self._to_citation(source) for source in sources],
            follow_up_question=generated.follow_up_question,
            confidence=self._combine_confidence(generated, sources),
            used_screen_context=summary,
            redaction_notice=redaction.notice,
            answer_mode=answer_mode,
            inference_notice=generated.inference_notice,
            retrieval_diagnostics=self._maybe_include_diagnostics(normalized_request, diagnostics),
        )

    def _overlay_collection_name(self) -> str | None:
        if not self.principal.tenant.overlay_kb_enabled:
            return None
        return self.principal.tenant.overlay_collection or (
            f"{self.settings.tenant_overlay_collection_prefix}{self.principal.tenant_id}"
        )

class ChatRuntimeService:
    def __init__(self, session: Session, settings: Settings, state_store: AsyncStateStore) -> None:
        self.session = session
        self.settings = settings
        self.state_store = state_store
        self.memory = ConversationMemoryService(state_store, settings)
        self.sessions = ChatSessionRepository(session)
        self.audit = AuditRepository(session)
        self.quota = QuotaService(session, settings, state_store)

    def record_ws_connect(self, principal: SessionPrincipal) -> ChatUsage:
        snapshot = self.quota.record_ws_connect(principal)
        self.audit.record(
            tenant_id=principal.tenant_id,
            session_id=principal.session_id,
            user_ref_hash=principal.user_ref_hash,
            actor_type="tenant_user",
            action="ws_connect",
            resource_type="chat_session",
            resource_id=principal.session_id,
            decision="allow",
        )
        self.session.commit()
        return ChatUsage(
            messages_in=snapshot.messages_in,
            messages_out=snapshot.messages_out,
            prompt_tokens=snapshot.prompt_tokens,
            completion_tokens=snapshot.completion_tokens,
            ws_connects=snapshot.ws_connects,
        )

    async def handle_turn(self, principal: SessionPrincipal, request: ChatTurnRequest) -> ChatTurnResponse:
        if "chat:use" not in principal.mask_permissions:
            raise PermissionError("La sessione non dispone del permesso chat:use.")

        TenantAccessService(self.session, self.settings).require_tenant_allowed(principal.tenant_id)
        await self.quota.enforce_burst_limit(principal)
        chat_session = self.sessions.get_session(principal.session_id)
        if chat_session is None:
            raise RuntimeError("Sessione chat non trovata.")

        history = await self.memory.read_history(principal)
        user_context = request.user_context.model_copy(deep=True) if request.user_context else UserContext(
            username=principal.user_id,
            roles=principal.roles,
            company_code=principal.company_code,
        )
        user_context.username = user_context.username or principal.user_id
        user_context.roles = list(principal.roles)
        user_context.company_code = principal.company_code or user_context.company_code
        retrieval_options = (
            request.retrieval_options.model_copy(deep=True)
            if request.retrieval_options
            else RetrievalOptions()
        )
        retrieval_options.role_scope = list(principal.roles)

        query_request = QueryRequest(
            message=request.message,
            conversation_id=principal.session_id,
            user_locale="it",
            screen_context=request.screen_context,
            user_context=user_context,
            retrieval_options=retrieval_options,
        )
        runtime_settings = get_runtime_settings(self.session, self.settings)
        rag = TenantAwareRAGService(settings=runtime_settings, principal=principal)
        response = rag.run_chat_request(query_request, conversation_history=history)

        await self.memory.append(principal, "user", request.message)
        await self.memory.append(principal, "assistant", response.answer)

        self.sessions.touch_session(chat_session, screen_id=request.screen_context.screen_id)
        usage_snapshot = self.quota.record_turn(
            principal,
            prompt_tokens=rag.last_usage["prompt_tokens"],
            completion_tokens=rag.last_usage["completion_tokens"],
        )
        self.audit.record(
            tenant_id=principal.tenant_id,
            session_id=principal.session_id,
            user_ref_hash=principal.user_ref_hash,
            actor_type="tenant_user",
            action="chat_turn",
            resource_type="chat_session",
            resource_id=principal.session_id,
            decision="allow",
            metadata_json={
                "answer_mode": response.answer_mode,
                "citation_count": len(response.citations),
            },
        )
        self.session.commit()

        return ChatTurnResponse(
            session_id=principal.session_id,
            answer=response.answer,
            steps=response.steps,
            citations=response.citations,
            follow_up_question=response.follow_up_question,
            confidence=response.confidence,
            answer_mode=response.answer_mode,
            inference_notice=response.inference_notice,
            usage=ChatUsage(
                messages_in=usage_snapshot.messages_in,
                messages_out=usage_snapshot.messages_out,
                prompt_tokens=usage_snapshot.prompt_tokens,
                completion_tokens=usage_snapshot.completion_tokens,
                ws_connects=usage_snapshot.ws_connects,
            ),
        )

    async def close_session(self, principal: SessionPrincipal) -> None:
        chat_session = self.sessions.get_session(principal.session_id)
        if chat_session is None:
            return
        self.sessions.close_session(chat_session)
        await self.memory.clear(principal)
        self.audit.record(
            tenant_id=principal.tenant_id,
            session_id=principal.session_id,
            user_ref_hash=principal.user_ref_hash,
            actor_type="tenant_user",
            action="close_session",
            resource_type="chat_session",
            resource_id=principal.session_id,
            decision="allow",
        )
        self.session.commit()
