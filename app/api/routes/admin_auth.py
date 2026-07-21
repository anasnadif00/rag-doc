"""Admin authentication routes for the web panel."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from app.auth.admin_service import AdminAuthService, AdminAuthenticationError
from app.auth.cookies import clear_admin_auth_cookies, set_admin_auth_cookies
from app.auth.dependencies import get_admin_auth_service, require_provider_admin
from app.auth.schemas import AdminLoginRequest, AdminSessionInfoResponse, AdminSessionResponse
from app.auth.tokens import TokenValidationError
from app.core.config import Settings, get_settings
from app.tenancy.models import AdminPrincipal

router = APIRouter(prefix="/v1/admin-auth", tags=["admin-auth"])


@router.post("/login", response_model=AdminSessionResponse)
async def login(
    request: AdminLoginRequest,
    response: Response,
    service: AdminAuthService = Depends(get_admin_auth_service),
    settings: Settings = Depends(get_settings),
) -> AdminSessionResponse:
    try:
        principal, access_token, refresh_token = await service.login(request.username, request.password)
    except AdminAuthenticationError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc

    set_admin_auth_cookies(
        response,
        settings,
        access_token=access_token,
        refresh_token=refresh_token,
    )
    response.headers["Cache-Control"] = "no-store"
    return AdminSessionResponse(
        username=principal.username,
        display_name=principal.display_name,
        expires_in=settings.admin_session_ttl_seconds,
    )


@router.post("/refresh", response_model=AdminSessionResponse)
async def refresh(
    raw_request: Request,
    response: Response,
    service: AdminAuthService = Depends(get_admin_auth_service),
    settings: Settings = Depends(get_settings),
) -> AdminSessionResponse:
    refresh_token = raw_request.cookies.get(settings.admin_refresh_cookie_name)
    if not refresh_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token mancante.")
    try:
        principal, access_token, next_refresh_token = await service.refresh(refresh_token)
    except (AdminAuthenticationError, TokenValidationError) as exc:
        status_code = getattr(exc, "status_code", status.HTTP_401_UNAUTHORIZED)
        raise HTTPException(status_code=status_code, detail=str(exc)) from exc

    set_admin_auth_cookies(
        response,
        settings,
        access_token=access_token,
        refresh_token=next_refresh_token,
    )
    response.headers["Cache-Control"] = "no-store"
    return AdminSessionResponse(
        username=principal.username,
        display_name=principal.display_name,
        expires_in=settings.admin_session_ttl_seconds,
    )


@router.get("/me", response_model=AdminSessionInfoResponse)
def me(principal: AdminPrincipal = Depends(require_provider_admin)) -> AdminSessionInfoResponse:
    return AdminSessionInfoResponse(username=principal.username, display_name=principal.display_name)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    response: Response,
    raw_request: Request,
    service: AdminAuthService = Depends(get_admin_auth_service),
    settings: Settings = Depends(get_settings),
) -> None:
    principal = None
    cookie_token = raw_request.cookies.get(settings.admin_session_cookie_name)
    if cookie_token:
        try:
            principal = service.principal_from_session_token(cookie_token)
        except AdminAuthenticationError:
            principal = None
    refresh_claims = await service.revoke_refresh(
        raw_request.cookies.get(settings.admin_refresh_cookie_name),
    )
    if principal is None and refresh_claims is not None:
        try:
            principal = service.principal_from_refresh_claims(refresh_claims)
        except AdminAuthenticationError:
            principal = None
    if principal is not None:
        service.record_logout(principal)

    clear_admin_auth_cookies(response, settings)
    response.headers["Cache-Control"] = "no-store"
    return None
