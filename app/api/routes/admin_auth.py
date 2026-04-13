"""Admin authentication routes for the web panel."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from app.auth.admin_service import AdminAuthService, AdminAuthenticationError
from app.auth.dependencies import get_admin_auth_service, require_provider_admin
from app.auth.schemas import AdminLoginRequest, AdminSessionInfoResponse, AdminSessionResponse
from app.core.config import Settings, get_settings
from app.tenancy.models import AdminPrincipal

router = APIRouter(prefix="/v1/admin-auth", tags=["admin-auth"])


def _set_session_cookie(response: Response, settings: Settings, token: str) -> None:
    response.set_cookie(
        key=settings.admin_session_cookie_name,
        value=token,
        max_age=settings.admin_session_ttl_seconds,
        httponly=True,
        samesite="strict",
        secure=settings.web_cookie_secure,
        path="/",
    )


def _clear_session_cookie(response: Response, settings: Settings) -> None:
    response.delete_cookie(
        key=settings.admin_session_cookie_name,
        httponly=True,
        samesite="strict",
        secure=settings.web_cookie_secure,
        path="/",
    )


@router.post("/login", response_model=AdminSessionResponse)
def login(
    request: AdminLoginRequest,
    response: Response,
    service: AdminAuthService = Depends(get_admin_auth_service),
    settings: Settings = Depends(get_settings),
) -> AdminSessionResponse:
    try:
        principal, token = service.login(request.username, request.password)
    except AdminAuthenticationError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc

    _set_session_cookie(response, settings, token)
    return AdminSessionResponse(
        username=principal.username,
        display_name=principal.display_name,
        expires_in=settings.admin_session_ttl_seconds,
    )


@router.get("/me", response_model=AdminSessionInfoResponse)
def me(principal: AdminPrincipal = Depends(require_provider_admin)) -> AdminSessionInfoResponse:
    return AdminSessionInfoResponse(username=principal.username, display_name=principal.display_name)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    response: Response,
    raw_request: Request,
    service: AdminAuthService = Depends(get_admin_auth_service),
    settings: Settings = Depends(get_settings),
) -> None:
    cookie_token = raw_request.cookies.get(settings.admin_session_cookie_name)
    if cookie_token:
        try:
            principal = service.principal_from_session_token(cookie_token)
        except AdminAuthenticationError:
            principal = None
        if principal is not None:
            service.record_logout(principal)

    _clear_session_cookie(response, settings)
    return None
