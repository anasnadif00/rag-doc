"""Admin login, session validation, and audit logging."""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.auth.passwords import hash_password, needs_rehash, verify_password
from app.auth.refresh import RefreshTokenService
from app.auth.schemas import RefreshClaims
from app.auth.tokens import TokenValidationError, decode_admin_session_token, issue_admin_session_token
from app.core.config import Settings
from app.persistence.repositories import AdminUserRepository, AuditRepository
from app.tenancy.cache import AsyncStateStore
from app.tenancy.models import AdminPrincipal


class AdminAuthenticationError(RuntimeError):
    def __init__(self, message: str = "Accesso non autorizzato.", *, status_code: int = 401) -> None:
        super().__init__(message)
        self.status_code = status_code


class AdminAuthService:
    def __init__(self, session: Session, settings: Settings, state_store: AsyncStateStore) -> None:
        self.session = session
        self.settings = settings
        self.admin_users = AdminUserRepository(session)
        self.audit = AuditRepository(session)
        self.refresh_tokens = RefreshTokenService(settings, state_store)

    async def login(self, username: str, password: str) -> tuple[AdminPrincipal, str, str]:
        cleaned_username = username.strip()
        user = self.admin_users.get_by_username(cleaned_username)
        if user is None or not user.is_active or not verify_password(user.password_hash, password):
            self._record_login_attempt(cleaned_username, decision="deny")
            raise AdminAuthenticationError("Credenziali non valide.")

        if needs_rehash(user.password_hash):
            user.password_hash = hash_password(password)

        principal = self._principal_from_user(user)
        token = self._issue_access_token(principal)
        refresh = await self.refresh_tokens.issue_admin(user_id=user.id)
        user.last_login_at = principal.issued_at
        self.admin_users.save(user)
        self._record_login_attempt(user.username, resource_id=user.id, decision="allow")
        self.session.commit()
        return principal, token, refresh.token

    async def refresh(self, refresh_token: str) -> tuple[AdminPrincipal, str, str]:
        claims = await self.refresh_tokens.consume(refresh_token, expected_kind="admin")
        principal = self.principal_from_refresh_claims(claims)
        access_token = self._issue_access_token(principal)
        refresh = await self.refresh_tokens.rotate(claims)
        self.audit.record(
            tenant_id=None,
            session_id=None,
            user_ref_hash=None,
            actor_type="admin_user",
            action="refresh",
            resource_type="admin_user",
            resource_id=principal.user_id,
            decision="allow",
            metadata_json={"username": principal.username},
        )
        self.session.commit()
        return principal, access_token, refresh.token

    def principal_from_session_token(self, token: str) -> AdminPrincipal:
        try:
            claims = decode_admin_session_token(self.settings, token)
        except TokenValidationError as exc:
            raise AdminAuthenticationError(str(exc)) from exc

        user = self.admin_users.get_by_id(claims.sub)
        if user is None or not user.is_active:
            raise AdminAuthenticationError("Sessione amministratore non valida.")

        return self._principal_from_user(user)

    def principal_from_refresh_claims(self, claims: RefreshClaims) -> AdminPrincipal:
        user = self.admin_users.get_by_id(claims.sub)
        if user is None or not user.is_active:
            raise AdminAuthenticationError("Sessione amministratore non valida.")
        return self._principal_from_user(user)

    async def revoke_refresh(self, token: str | None) -> RefreshClaims | None:
        return await self.refresh_tokens.revoke(token, expected_kind="admin")

    @staticmethod
    def _principal_from_user(user) -> AdminPrincipal:
        return AdminPrincipal(
            subject="admin_user",
            user_id=user.id,
            username=user.username,
            display_name=user.display_name,
            authentication_method="session",
        )

    def _issue_access_token(self, principal: AdminPrincipal) -> str:
        token, _ = issue_admin_session_token(
            self.settings,
            user_id=principal.user_id or "",
            username=principal.username,
            display_name=principal.display_name,
        )
        return token

    def record_logout(self, principal: AdminPrincipal) -> None:
        self.audit.record(
            tenant_id=None,
            session_id=None,
            user_ref_hash=None,
            actor_type="admin_user",
            action="logout",
            resource_type="admin_user",
            resource_id=principal.user_id,
            decision="allow",
            metadata_json={"username": principal.username},
        )
        self.session.commit()

    def _record_login_attempt(
        self,
        username: str,
        *,
        resource_id: str | None = None,
        decision: str,
    ) -> None:
        self.audit.record(
            tenant_id=None,
            session_id=None,
            user_ref_hash=None,
            actor_type="admin_user",
            action="login",
            resource_type="admin_user",
            resource_id=resource_id,
            decision=decision,
            metadata_json={"username": username},
        )
        self.session.commit()
