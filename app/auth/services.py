"""Bootstrap auth, session principal resolution, and WebSocket ticketing."""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.auth.passwords import hash_password, needs_rehash, verify_password
from app.auth.refresh import RefreshTokenService
from app.auth.schemas import BootstrapRequest, BootstrapResponse, RefreshClaims, SessionClaims, WSTicketPayload, WSTicketResponse
from app.auth.tokens import (
    TokenValidationError,
    decode_bootstrap_token,
    decode_session_token,
    issue_session_token,
    read_unverified_claims,
    read_unverified_header,
)
from app.core.config import Settings
from app.persistence.repositories import AuditRepository, ChatSessionRepository, TenantRepository, TenantUsersRepository
from app.tenancy.cache import AsyncStateStore
from app.tenancy.models import SessionPrincipal
from app.tenancy.security import hash_user_reference
from app.tenancy.services import TenantAccessError, TenantAccessService

WEB_CHAT_USAGE_LIMIT_MESSAGE = (
    "Servizio non disponibile: hai superato il limite di utilizzo previsto. "
    "Contatta l'amministratore o l'assistenza di sistema."
)
USAGE_LIMIT_REASON_CODES = {"daily_message_limit", "daily_token_limit"}


@dataclass
class WebChatSessionContext:
    session_id: str
    access_token: str
    refresh_token: str
    display_name: str
    expires_in: int


@dataclass
class ChatAuthSessionContext:
    session_id: str
    access_token: str
    refresh_token: str
    tenant_id: str
    tenant_code: str
    tenant_display_name: str
    username: str
    display_name: str
    expires_at: datetime


class ChatAuthenticationError(RuntimeError):
    def __init__(
        self,
        message: str = "Credenziali non valide.",
        *,
        status_code: int = 401,
        reason_code: str = "invalid_credentials",
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.reason_code = reason_code


class AuthService:
    def __init__(self, session: Session, settings: Settings, state_store: AsyncStateStore) -> None:
        self.session = session
        self.settings = settings
        self.state_store = state_store
        self.tenants = TenantRepository(session, settings)
        self.tenant_users = TenantUsersRepository(session)
        self.sessions = ChatSessionRepository(session)
        self.audit = AuditRepository(session)
        self.access = TenantAccessService(session, settings, audit_repository=self.audit)
        self.refresh_tokens = RefreshTokenService(settings, state_store)

    async def bootstrap(self, request: BootstrapRequest, *, origin: str | None = None) -> tuple[BootstrapResponse, str]:
        self._ensure_security_configured()
        unverified_claims = read_unverified_claims(request.bootstrap_token)
        issuer = str(unverified_claims.get("iss") or "").strip()
        tenant_id = str(unverified_claims.get("tid") or "").strip()
        if not issuer:
            raise TokenValidationError("Bootstrap token privo di issuer.")
        tenant = self.tenants.get_tenant_by_issuer(issuer)
        if tenant is None and tenant_id:
            tenant = self.tenants.get_tenant(tenant_id)
        if tenant is None:
            raise TokenValidationError("Tenant bootstrap non riconosciuto.")
        if tenant_id and tenant.id != tenant_id:
            raise TokenValidationError("Tenant bootstrap non coerente con il token.")
        self._ensure_origin_allowed(tenant.allowed_origins, origin)

        header = read_unverified_header(request.bootstrap_token)
        key = self.tenants.get_active_key(tenant.id, kid=header.get("kid"))
        if key is None or not key.public_key_pem:
            raise TokenValidationError("Chiave pubblica tenant non configurata.")

        claims = decode_bootstrap_token(
            request.bootstrap_token,
            public_key_pem=key.public_key_pem,
            audience=self.settings.bootstrap_jwt_audience,
            algorithms=[key.algorithm],
        )
        if "chat:use" not in claims.mask_permissions:
            raise TokenValidationError("Il token bootstrap non abilita l'uso della chat.")

        replay_key = f"auth:bootstrap:jti:{claims.jti}"
        replay_count = await self.state_store.increment(
            replay_key,
            ttl_seconds=self.settings.bootstrap_replay_ttl_seconds,
            amount=1,
        )
        if replay_count > 1:
            raise TokenValidationError("Bootstrap token gia utilizzato.")

        tenant_context = self.access.require_tenant_allowed(tenant.id)
        user_ref_hash = hash_user_reference(tenant.id, claims.sub, self.settings.user_hash_salt)
        chat_session = self.sessions.create_session(
            tenant_id=tenant.id,
            user_ref_hash=user_ref_hash,
            mask_id=claims.mask_id,
            screen_id=None,
        )
        access_token, _ = issue_session_token(
            self.settings,
            tenant_id=tenant.id,
            user_id=claims.sub,
            session_id=chat_session.id,
            roles=claims.roles,
            mask_id=claims.mask_id,
            mask_permissions=claims.mask_permissions,
            company_code=claims.company_code,
        )
        refresh = await self.refresh_tokens.issue_chat(
            user_id=claims.sub,
            tenant_id=tenant.id,
            session_id=chat_session.id,
            roles=claims.roles,
            mask_id=claims.mask_id,
            mask_permissions=claims.mask_permissions,
            company_code=claims.company_code,
        )
        self.audit.record(
            tenant_id=tenant.id,
            session_id=chat_session.id,
            user_ref_hash=user_ref_hash,
            actor_type="tenant_user",
            action="bootstrap",
            resource_type="session",
            resource_id=chat_session.id,
            decision="allow",
        )
        self.session.commit()
        return (
            BootstrapResponse(
                session_id=chat_session.id,
                access_token=access_token,
                expires_in=self.settings.session_ttl_seconds,
                tenant_id=tenant_context.tenant_id,
                tenant_code=tenant_context.tenant_code,
                display_name=tenant_context.display_name,
            ),
            refresh.token,
        )

    def principal_from_session_token(self, token: str) -> SessionPrincipal:
        self._ensure_security_configured()
        claims = decode_session_token(self.settings, token)
        return self._principal_from_claims(claims)

    async def start_web_chat_session(self, *, origin: str | None = None) -> WebChatSessionContext:
        self._ensure_security_configured()
        tenant_code = self.settings.web_chat_default_tenant_code.strip()
        if not tenant_code:
            raise TenantAccessError(
                "Servizio momentaneamente non disponibile.",
                reason_code="web_chat_not_configured",
                status_code=503,
            )

        tenant = self.tenants.get_tenant_by_code(tenant_code)
        if tenant is None:
            raise TenantAccessError(
                "Servizio momentaneamente non disponibile.",
                reason_code="web_chat_tenant_missing",
                status_code=503,
            )

        try:
            self._ensure_origin_allowed(tenant.allowed_origins, origin)
            tenant_context = self.access.require_tenant_allowed(tenant.id)
        except TokenValidationError as exc:
            raise TenantAccessError(
                "Servizio momentaneamente non disponibile.",
                reason_code="web_chat_unavailable",
                status_code=503,
            ) from exc
        except TenantAccessError as exc:
            if exc.reason_code in USAGE_LIMIT_REASON_CODES:
                raise TenantAccessError(
                    WEB_CHAT_USAGE_LIMIT_MESSAGE,
                    reason_code=exc.reason_code,
                    status_code=429,
                ) from exc
            raise TenantAccessError(
                "Servizio momentaneamente non disponibile.",
                reason_code=getattr(exc, "reason_code", "web_chat_unavailable"),
                status_code=503,
            ) from exc

        user_id = f"utente-web-{secrets.token_urlsafe(8)}"
        user_ref_hash = hash_user_reference(tenant.id, user_id, self.settings.user_hash_salt)
        chat_session = self.sessions.create_session(
            tenant_id=tenant.id,
            user_ref_hash=user_ref_hash,
            mask_id=None,
            screen_id=None,
            client_type="web_portal",
        )
        access_token, _ = issue_session_token(
            self.settings,
            tenant_id=tenant.id,
            user_id=user_id,
            session_id=chat_session.id,
            roles=[],
            mask_id=None,
            mask_permissions=["chat:use"],
            company_code=None,
        )
        refresh = await self.refresh_tokens.issue_chat(
            user_id=user_id,
            tenant_id=tenant.id,
            session_id=chat_session.id,
            roles=[],
            mask_id=None,
            mask_permissions=["chat:use"],
            company_code=None,
        )
        self.audit.record(
            tenant_id=tenant.id,
            session_id=chat_session.id,
            user_ref_hash=user_ref_hash,
            actor_type="web_chat",
            action="start_web_session",
            resource_type="session",
            resource_id=chat_session.id,
            decision="allow",
        )
        self.session.commit()
        return WebChatSessionContext(
            session_id=chat_session.id,
            access_token=access_token,
            refresh_token=refresh.token,
            display_name=tenant_context.display_name,
            expires_in=self.settings.session_ttl_seconds,
        )

    async def login_chat_user(
        self,
        *,
        tenant_code: str,
        username: str,
        password: str,
        origin: str | None = None,
    ) -> ChatAuthSessionContext:
        self._ensure_security_configured()
        cleaned_tenant_code = tenant_code.strip()
        cleaned_username = username.strip()
        tenant = self.tenants.get_tenant_by_code(cleaned_tenant_code)
        if tenant is None:
            self._record_chat_login_attempt(
                tenant_id=None,
                username=cleaned_username,
                decision="deny",
                reason_code="tenant_not_found",
            )
            raise ChatAuthenticationError()

        self._ensure_origin_allowed(tenant.allowed_origins, origin)
        tenant_context = self.access.require_tenant_allowed(tenant.id)
        user = self.tenant_users.get_active_user(tenant.id, cleaned_username)
        user_ref_hash = hash_user_reference(tenant.id, cleaned_username, self.settings.user_hash_salt)
        if user is None or not verify_password(user.password_hash, password):
            self._record_chat_login_attempt(
                tenant_id=tenant.id,
                username=cleaned_username,
                user_ref_hash=user_ref_hash,
                resource_id=user.id if user else None,
                decision="deny",
                reason_code="invalid_credentials",
            )
            raise ChatAuthenticationError()

        if needs_rehash(user.password_hash):
            user.password_hash = hash_password(password)
            self.tenant_users.save(user)

        chat_session = self.sessions.create_session(
            tenant_id=tenant.id,
            user_ref_hash=user_ref_hash,
            mask_id=None,
            screen_id=None,
            client_type="web_portal",
        )
        access_token, expires_at = issue_session_token(
            self.settings,
            tenant_id=tenant.id,
            user_id=user.username,
            session_id=chat_session.id,
            roles=[],
            mask_id=None,
            mask_permissions=["chat:use"],
            company_code=None,
        )
        refresh = await self.refresh_tokens.issue_chat(
            user_id=user.username,
            tenant_id=tenant.id,
            session_id=chat_session.id,
            roles=[],
            mask_id=None,
            mask_permissions=["chat:use"],
            company_code=None,
        )
        self.audit.record(
            tenant_id=tenant.id,
            session_id=chat_session.id,
            user_ref_hash=user_ref_hash,
            actor_type="tenant_user",
            action="login",
            resource_type="tenant_user",
            resource_id=user.id,
            decision="allow",
            metadata_json={"username": user.username},
        )
        self.session.commit()
        return ChatAuthSessionContext(
            session_id=chat_session.id,
            access_token=access_token,
            refresh_token=refresh.token,
            tenant_id=tenant.id,
            tenant_code=tenant_context.tenant_code,
            tenant_display_name=tenant_context.display_name,
            username=user.username,
            display_name=user.display_name,
            expires_at=expires_at,
        )

    async def refresh_chat_session(self, refresh_token: str) -> ChatAuthSessionContext:
        claims = await self.refresh_tokens.consume(refresh_token, expected_kind="chat")
        if not claims.tid or not claims.sid:
            raise TokenValidationError("Refresh token chat non valido.")

        tenant_context = self.access.require_tenant_allowed(claims.tid)
        chat_session = self.sessions.get_session(claims.sid)
        if chat_session is None or chat_session.status != "active":
            raise TenantAccessError("Sessione chat non attiva.", reason_code="session_inactive", status_code=401)

        tenant_user = self.tenant_users.get_active_user(claims.tid, claims.sub)
        is_anonymous_web_user = claims.sub.startswith("utente-web-")
        if chat_session.client_type == "web_portal" and not is_anonymous_web_user and tenant_user is None:
            raise TenantAccessError("Utente chat non attivo.", reason_code="user_inactive", status_code=401)

        access_token, expires_at = issue_session_token(
            self.settings,
            tenant_id=claims.tid,
            user_id=claims.sub,
            session_id=claims.sid,
            roles=claims.roles,
            mask_id=claims.mask_id,
            mask_permissions=claims.mask_permissions,
            company_code=claims.company_code,
        )
        refresh = await self.refresh_tokens.rotate(claims)
        self.audit.record(
            tenant_id=claims.tid,
            session_id=claims.sid,
            user_ref_hash=chat_session.user_ref_hash,
            actor_type="tenant_user",
            action="refresh",
            resource_type="session",
            resource_id=claims.sid,
            decision="allow",
        )
        self.session.commit()
        return ChatAuthSessionContext(
            session_id=claims.sid,
            access_token=access_token,
            refresh_token=refresh.token,
            tenant_id=claims.tid,
            tenant_code=tenant_context.tenant_code,
            tenant_display_name=tenant_context.display_name,
            username=claims.sub,
            display_name=tenant_user.display_name if tenant_user is not None else claims.sub,
            expires_at=expires_at,
        )

    async def revoke_refresh(self, token: str | None) -> RefreshClaims | None:
        return await self.refresh_tokens.revoke(token, expected_kind="chat")

    def _principal_from_claims(self, claims: SessionClaims) -> SessionPrincipal:
        tenant_context = self.access.require_tenant_allowed(claims.tid)
        chat_session = self.sessions.get_session(claims.sid)
        if chat_session is None or chat_session.status != "active":
            raise TenantAccessError("Sessione chat non attiva.", reason_code="session_inactive", status_code=401)
        user_ref_hash = hash_user_reference(claims.tid, claims.sub, self.settings.user_hash_salt)
        return SessionPrincipal(
            tenant_id=claims.tid,
            tenant_code=tenant_context.tenant_code,
            session_id=claims.sid,
            user_id=claims.sub,
            user_ref_hash=user_ref_hash,
            roles=claims.roles,
            mask_id=claims.mask_id,
            mask_permissions=claims.mask_permissions,
            company_code=claims.company_code,
            session_expires_at=datetime.utcfromtimestamp(claims.exp),
            tenant=tenant_context,
        )

    def _ensure_security_configured(self) -> None:
        if not self.settings.session_jwt_secret or not self.settings.user_hash_salt:
            raise TokenValidationError("Configurazione sicurezza incompleta.")

    def _ensure_origin_allowed(self, allowed_origins: list[str], origin: str | None) -> None:
        if not allowed_origins or not origin:
            return
        if origin not in allowed_origins:
            raise TokenValidationError("Origine non autorizzata per il tenant.")

    def _record_chat_login_attempt(
        self,
        *,
        tenant_id: str | None,
        username: str,
        decision: str,
        user_ref_hash: str | None = None,
        resource_id: str | None = None,
        reason_code: str | None = None,
    ) -> None:
        self.audit.record(
            tenant_id=tenant_id,
            session_id=None,
            user_ref_hash=user_ref_hash,
            actor_type="tenant_user",
            action="login",
            resource_type="tenant_user",
            resource_id=resource_id,
            decision=decision,
            reason_code=reason_code,
            metadata_json={"username": username},
        )
        self.session.commit()


class WSTicketService:
    def __init__(self, session: Session, settings: Settings, state_store: AsyncStateStore) -> None:
        self.session = session
        self.settings = settings
        self.state_store = state_store
        self.auth = AuthService(session, settings, state_store)
        self.sessions = ChatSessionRepository(session)

    async def issue_ticket(self, principal: SessionPrincipal) -> WSTicketResponse:
        self.auth.access.require_tenant_allowed(principal.tenant_id)
        ticket = secrets.token_urlsafe(24)
        expires_at = datetime.utcnow() + timedelta(seconds=self.settings.ws_ticket_ttl_seconds)
        payload = WSTicketPayload(
            ticket=ticket,
            session_id=principal.session_id,
            tenant_id=principal.tenant_id,
            tenant_code=principal.tenant_code,
            user_id=principal.user_id,
            user_ref_hash=principal.user_ref_hash,
            roles=principal.roles,
            mask_id=principal.mask_id,
            mask_permissions=principal.mask_permissions,
            company_code=principal.company_code,
            expires_at=expires_at,
        )
        await self.state_store.set_json(
            f"chat:wsticket:{ticket}",
            payload.model_dump(mode="json"),
            ttl_seconds=self.settings.ws_ticket_ttl_seconds,
        )
        return WSTicketResponse(ticket=ticket, expires_in=self.settings.ws_ticket_ttl_seconds)

    async def consume_ticket(self, ticket: str) -> SessionPrincipal:
        payload = await self.state_store.pop_json(f"chat:wsticket:{ticket}")
        if payload is None:
            raise TenantAccessError("Ticket WebSocket non valido o scaduto.", reason_code="ws_ticket_invalid", status_code=401)
        ticket_payload = WSTicketPayload.model_validate(payload)
        if ticket_payload.expires_at <= datetime.utcnow():
            raise TenantAccessError("Ticket WebSocket scaduto.", reason_code="ws_ticket_expired", status_code=401)
        tenant_context = self.auth.access.require_tenant_allowed(ticket_payload.tenant_id)
        principal = SessionPrincipal(
            tenant_id=ticket_payload.tenant_id,
            tenant_code=ticket_payload.tenant_code,
            session_id=ticket_payload.session_id,
            user_id=ticket_payload.user_id,
            user_ref_hash=ticket_payload.user_ref_hash,
            roles=ticket_payload.roles,
            mask_id=ticket_payload.mask_id,
            mask_permissions=ticket_payload.mask_permissions,
            company_code=ticket_payload.company_code,
            session_expires_at=ticket_payload.expires_at,
            tenant=tenant_context,
        )
        chat_session = self.sessions.get_session(principal.session_id)
        if chat_session is None:
            raise TenantAccessError("Sessione WebSocket non trovata.", reason_code="ws_session_missing", status_code=401)
        self.sessions.touch_session(chat_session)
        self.session.commit()
        return principal
