"""Bootstrap auth routes for ERP clients."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, Response

from app.auth.dependencies import get_auth_service
from app.auth.schemas import BootstrapRequest, BootstrapResponse
from app.auth.services import AuthService
from app.auth.tokens import TokenValidationError
from app.core.config import Settings, get_settings
from app.tenancy.services import TenantAccessError

router = APIRouter(prefix="/v1/auth", tags=["auth"])


def _set_chat_session_cookie(response: Response, settings: Settings, token: str) -> None:
    response.set_cookie(
        key=settings.chat_session_cookie_name,
        value=token,
        max_age=settings.session_ttl_seconds,
        httponly=True,
        samesite="strict",
        secure=settings.web_cookie_secure,
        path="/",
    )


@router.post("/bootstrap", response_model=BootstrapResponse)
async def bootstrap(
    request: BootstrapRequest,
    raw_request: Request,
    response: Response,
    auth_service: AuthService = Depends(get_auth_service),
    settings: Settings = Depends(get_settings),
) -> BootstrapResponse:
    try:
        bootstrap_response = await auth_service.bootstrap(request, origin=raw_request.headers.get("origin"))
    except (TokenValidationError, TenantAccessError) as exc:
        status_code = getattr(exc, "status_code", 401)
        raise HTTPException(status_code=status_code, detail=str(exc)) from exc

    _set_chat_session_cookie(response, settings, bootstrap_response.access_token)
    return bootstrap_response
