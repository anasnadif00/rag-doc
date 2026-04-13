"""Dependencies for admin, chat, and session principals."""

from __future__ import annotations

from fastapi import Depends, HTTPException, Request, WebSocketException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.auth.admin_service import AdminAuthService, AdminAuthenticationError
from app.auth.services import AuthService, WSTicketService
from app.auth.tokens import TokenValidationError
from app.core.config import Settings, get_settings
from app.persistence.db import get_db_session
from app.tenancy.cache import get_state_store
from app.tenancy.models import AdminPrincipal, SessionPrincipal
from app.tenancy.services import TenantAccessError

bearer_scheme = HTTPBearer(auto_error=False)


def get_state_store_dependency(settings: Settings = Depends(get_settings)):
    return get_state_store(settings)


def get_auth_service(
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
    state_store=Depends(get_state_store_dependency),
) -> AuthService:
    return AuthService(session=session, settings=settings, state_store=state_store)


def get_ws_ticket_service(
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
    state_store=Depends(get_state_store_dependency),
) -> WSTicketService:
    return WSTicketService(session=session, settings=settings, state_store=state_store)


def get_admin_auth_service(
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
) -> AdminAuthService:
    return AdminAuthService(session=session, settings=settings)


def require_provider_admin(
    request: Request,
    settings: Settings = Depends(get_settings),
    admin_auth_service: AdminAuthService = Depends(get_admin_auth_service),
) -> AdminPrincipal:
    cookie_token = request.cookies.get(settings.admin_session_cookie_name)
    if cookie_token:
        try:
            return admin_auth_service.principal_from_session_token(cookie_token)
        except AdminAuthenticationError as exc:
            raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Accesso non autorizzato.")


def require_session_principal(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    auth_service: AuthService = Depends(get_auth_service),
    settings: Settings = Depends(get_settings),
) -> SessionPrincipal:
    token = credentials.credentials if credentials else request.cookies.get(settings.chat_session_cookie_name)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sessione non valida.")
    try:
        return auth_service.principal_from_session_token(token)
    except (TokenValidationError, TenantAccessError) as exc:
        status_code = getattr(exc, "status_code", status.HTTP_401_UNAUTHORIZED)
        raise HTTPException(status_code=status_code, detail=str(exc)) from exc


async def require_ws_principal(ticket: str, ws_ticket_service: WSTicketService) -> SessionPrincipal:
    try:
        return await ws_ticket_service.consume_ticket(ticket)
    except (TokenValidationError, TenantAccessError) as exc:
        status_code = getattr(exc, "status_code", status.WS_1008_POLICY_VIOLATION)
        raise WebSocketException(code=status_code, reason=str(exc)) from exc
