"""Chat authentication routes for browser and ERP-launched chat."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from app.auth.cookies import clear_chat_auth_cookies, set_chat_auth_cookies
from app.auth.dependencies import get_auth_service, require_session_principal
from app.auth.schemas import ChatLoginRequest, ChatSessionInfoResponse, ChatSessionResponse
from app.auth.services import AuthService, ChatAuthenticationError
from app.auth.tokens import TokenValidationError
from app.core.config import Settings, get_settings
from app.persistence.db import get_db_session
from app.persistence.repositories import ChatSessionRepository, TenantUsersRepository
from app.tenancy.models import SessionPrincipal
from app.tenancy.services import TenantAccessError

router = APIRouter(prefix="/v1/chat-auth", tags=["chat-auth"])


def _session_info(
    principal: SessionPrincipal,
    *,
    display_name: str | None = None,
) -> ChatSessionInfoResponse:
    return ChatSessionInfoResponse(
        authenticated=True,
        session_id=principal.session_id,
        tenant_id=principal.tenant_id,
        tenant_code=principal.tenant_code,
        tenant_display_name=principal.tenant.display_name,
        username=principal.user_id,
        display_name=display_name or principal.user_id,
        expires_at=principal.session_expires_at,
    )


@router.post("/login", response_model=ChatSessionResponse)
async def login(
    request: ChatLoginRequest,
    raw_request: Request,
    response: Response,
    service: AuthService = Depends(get_auth_service),
    settings: Settings = Depends(get_settings),
) -> ChatSessionResponse:
    try:
        session_context = await service.login_chat_user(
            tenant_code=request.tenant_code,
            username=request.username,
            password=request.password,
            origin=raw_request.headers.get("origin"),
        )
    except (ChatAuthenticationError, TokenValidationError, TenantAccessError) as exc:
        status_code = getattr(exc, "status_code", status.HTTP_401_UNAUTHORIZED)
        reason_code = getattr(exc, "reason_code", None)
        headers = {"X-Reason-Code": reason_code} if reason_code else None
        raise HTTPException(status_code=status_code, detail=str(exc), headers=headers) from exc

    set_chat_auth_cookies(
        response,
        settings,
        access_token=session_context.access_token,
        refresh_token=session_context.refresh_token,
    )
    response.headers["Cache-Control"] = "no-store"
    return ChatSessionResponse(
        authenticated=True,
        session_id=session_context.session_id,
        tenant_id=session_context.tenant_id,
        tenant_code=session_context.tenant_code,
        tenant_display_name=session_context.tenant_display_name,
        username=session_context.username,
        display_name=session_context.display_name,
        expires_at=session_context.expires_at,
    )


@router.post("/refresh", response_model=ChatSessionResponse)
async def refresh(
    raw_request: Request,
    response: Response,
    service: AuthService = Depends(get_auth_service),
    settings: Settings = Depends(get_settings),
) -> ChatSessionResponse:
    refresh_token = raw_request.cookies.get(settings.chat_refresh_cookie_name)
    if not refresh_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token mancante.")
    try:
        session_context = await service.refresh_chat_session(refresh_token)
    except (ChatAuthenticationError, TokenValidationError, TenantAccessError) as exc:
        status_code = getattr(exc, "status_code", status.HTTP_401_UNAUTHORIZED)
        reason_code = getattr(exc, "reason_code", None)
        headers = {"X-Reason-Code": reason_code} if reason_code else None
        raise HTTPException(status_code=status_code, detail=str(exc), headers=headers) from exc

    set_chat_auth_cookies(
        response,
        settings,
        access_token=session_context.access_token,
        refresh_token=session_context.refresh_token,
    )
    response.headers["Cache-Control"] = "no-store"
    return ChatSessionResponse(
        authenticated=True,
        session_id=session_context.session_id,
        tenant_id=session_context.tenant_id,
        tenant_code=session_context.tenant_code,
        tenant_display_name=session_context.tenant_display_name,
        username=session_context.username,
        display_name=session_context.display_name,
        expires_at=session_context.expires_at,
    )


@router.get("/me", response_model=ChatSessionInfoResponse)
def me(
    principal: SessionPrincipal = Depends(require_session_principal),
    session: Session = Depends(get_db_session),
) -> ChatSessionInfoResponse:
    tenant_user = TenantUsersRepository(session).get_active_user(principal.tenant_id, principal.user_id)
    return _session_info(
        principal,
        display_name=tenant_user.display_name if tenant_user is not None else principal.user_id,
    )


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    raw_request: Request,
    response: Response,
    service: AuthService = Depends(get_auth_service),
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
) -> None:
    principal = None
    access_token = raw_request.cookies.get(settings.chat_session_cookie_name)
    if access_token:
        try:
            principal = service.principal_from_session_token(access_token)
        except (TokenValidationError, TenantAccessError):
            principal = None
    refresh_claims = await service.revoke_refresh(
        raw_request.cookies.get(settings.chat_refresh_cookie_name),
    )
    session_id = principal.session_id if principal is not None else (refresh_claims.sid if refresh_claims else None)
    sessions = ChatSessionRepository(session)
    chat_session = sessions.get_session(session_id) if session_id else None
    if chat_session is not None:
        sessions.close_session(chat_session)
        session.commit()
    clear_chat_auth_cookies(response, settings)
    response.headers["Cache-Control"] = "no-store"
    return None
