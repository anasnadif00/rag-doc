"""Admin login, session validation, and audit logging."""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.auth.passwords import hash_password, needs_rehash, verify_password
from app.auth.tokens import TokenValidationError, decode_admin_session_token, issue_admin_session_token
from app.core.config import Settings
from app.persistence.repositories import AdminUserRepository, AuditRepository
from app.tenancy.models import AdminPrincipal


class AdminAuthenticationError(RuntimeError):
    def __init__(self, message: str = "Accesso non autorizzato.", *, status_code: int = 401) -> None:
        super().__init__(message)
        self.status_code = status_code


class AdminAuthService:
    def __init__(self, session: Session, settings: Settings) -> None:
        self.session = session
        self.settings = settings
        self.admin_users = AdminUserRepository(session)
        self.audit = AuditRepository(session)

    def login(self, username: str, password: str) -> tuple[AdminPrincipal, str]:
        cleaned_username = username.strip()
        user = self.admin_users.get_by_username(cleaned_username)
        if user is None or not user.is_active or not verify_password(user.password_hash, password):
            self._record_login_attempt(cleaned_username, decision="deny")
            raise AdminAuthenticationError("Credenziali non valide.")

        if needs_rehash(user.password_hash):
            user.password_hash = hash_password(password)

        principal = AdminPrincipal(
            subject="admin_user",
            user_id=user.id,
            username=user.username,
            display_name=user.display_name,
            authentication_method="session",
        )
        token, _ = issue_admin_session_token(
            self.settings,
            user_id=user.id,
            username=user.username,
            display_name=user.display_name,
        )
        user.last_login_at = principal.issued_at
        self.admin_users.save(user)
        self._record_login_attempt(user.username, resource_id=user.id, decision="allow")
        self.session.commit()
        return principal, token

    def principal_from_session_token(self, token: str) -> AdminPrincipal:
        try:
            claims = decode_admin_session_token(self.settings, token)
        except TokenValidationError as exc:
            raise AdminAuthenticationError(str(exc)) from exc

        user = self.admin_users.get_by_id(claims.sub)
        if user is None or not user.is_active:
            raise AdminAuthenticationError("Sessione amministratore non valida.")

        return AdminPrincipal(
            subject="admin_user",
            user_id=user.id,
            username=user.username,
            display_name=user.display_name,
            authentication_method="session",
        )

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
