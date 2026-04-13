"""JWT helpers for ERP bootstrap and session tokens."""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import Any

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from app.auth.schemas import AdminSessionClaims, BootstrapClaims, SessionClaims
from app.core.config import Settings


class TokenValidationError(RuntimeError):
    pass


def read_unverified_claims(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(token, options={"verify_signature": False, "verify_exp": False})
    except InvalidTokenError as exc:
        raise TokenValidationError("Token JWT non valido.") from exc


def read_unverified_header(token: str) -> dict[str, Any]:
    try:
        return jwt.get_unverified_header(token)
    except InvalidTokenError as exc:
        raise TokenValidationError("Header JWT non valido.") from exc


def decode_bootstrap_token(
    token: str,
    *,
    public_key_pem: str,
    audience: str,
    algorithms: list[str],
) -> BootstrapClaims:
    try:
        payload = jwt.decode(token, public_key_pem, audience=audience, algorithms=algorithms)
    except ExpiredSignatureError as exc:
        raise TokenValidationError("Bootstrap token scaduto.") from exc
    except InvalidTokenError as exc:
        raise TokenValidationError("Bootstrap token non valido.") from exc
    return BootstrapClaims.model_validate(payload)


def issue_session_token(
    settings: Settings,
    *,
    tenant_id: str,
    user_id: str,
    session_id: str,
    roles: list[str],
    mask_id: str | None,
    mask_permissions: list[str],
    company_code: str | None,
) -> tuple[str, datetime]:
    issued_at_ts = int(time.time())
    expires_at_ts = issued_at_ts + settings.session_ttl_seconds
    issued_at = datetime.utcfromtimestamp(issued_at_ts)
    expires_at = datetime.utcfromtimestamp(expires_at_ts)
    payload = {
        "iss": settings.session_jwt_issuer,
        "aud": settings.session_jwt_audience,
        "tid": tenant_id,
        "sub": user_id,
        "sid": session_id,
        "roles": roles,
        "mask_id": mask_id,
        "mask_permissions": mask_permissions,
        "company_code": company_code,
        "iat": issued_at_ts,
        "exp": expires_at_ts,
    }
    token = jwt.encode(payload, settings.session_jwt_secret, algorithm=settings.session_jwt_algorithm)
    return token, expires_at


def decode_session_token(settings: Settings, token: str) -> SessionClaims:
    try:
        payload = jwt.decode(
            token,
            settings.session_jwt_secret,
            audience=settings.session_jwt_audience,
            issuer=settings.session_jwt_issuer,
            algorithms=[settings.session_jwt_algorithm],
        )
    except ExpiredSignatureError as exc:
        raise TokenValidationError("Session token scaduto.") from exc
    except InvalidTokenError as exc:
        raise TokenValidationError("Session token non valido.") from exc
    return SessionClaims.model_validate(payload)


def issue_admin_session_token(
    settings: Settings,
    *,
    user_id: str,
    username: str,
    display_name: str,
) -> tuple[str, datetime]:
    issued_at_ts = int(time.time())
    expires_at_ts = issued_at_ts + settings.admin_session_ttl_seconds
    issued_at = datetime.utcfromtimestamp(issued_at_ts)
    expires_at = datetime.utcfromtimestamp(expires_at_ts)
    payload = {
        "iss": settings.admin_session_jwt_issuer,
        "aud": settings.admin_session_jwt_audience,
        "sub": user_id,
        "usr": username,
        "name": display_name,
        "iat": issued_at_ts,
        "exp": expires_at_ts,
    }
    token = jwt.encode(payload, settings.session_jwt_secret, algorithm=settings.session_jwt_algorithm)
    return token, expires_at


def decode_admin_session_token(settings: Settings, token: str) -> AdminSessionClaims:
    try:
        payload = jwt.decode(
            token,
            settings.session_jwt_secret,
            audience=settings.admin_session_jwt_audience,
            issuer=settings.admin_session_jwt_issuer,
            algorithms=[settings.session_jwt_algorithm],
        )
    except ExpiredSignatureError as exc:
        raise TokenValidationError("Sessione amministratore scaduta.") from exc
    except InvalidTokenError as exc:
        raise TokenValidationError("Sessione amministratore non valida.") from exc
    return AdminSessionClaims.model_validate(payload)
