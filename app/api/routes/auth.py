"""Bootstrap auth routes for ERP clients."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, Response

from app.auth.cookies import set_chat_auth_cookies
from app.auth.dependencies import get_auth_service
from app.auth.schemas import BootstrapRequest, BootstrapResponse
from app.auth.services import AuthService
from app.auth.tokens import TokenValidationError
from app.core.config import Settings, get_settings
from app.tenancy.services import TenantAccessError

router = APIRouter(prefix="/v1/auth", tags=["auth"])


@router.post("/bootstrap", response_model=BootstrapResponse)
async def bootstrap(
    request: BootstrapRequest,
    raw_request: Request,
    response: Response,
    auth_service: AuthService = Depends(get_auth_service),
    settings: Settings = Depends(get_settings),
) -> BootstrapResponse:
    try:
        bootstrap_response, refresh_token = await auth_service.bootstrap(
            request,
            origin=raw_request.headers.get("origin"),
        )
    except (TokenValidationError, TenantAccessError) as exc:
        status_code = getattr(exc, "status_code", 401)
        raise HTTPException(status_code=status_code, detail=str(exc)) from exc

    set_chat_auth_cookies(
        response,
        settings,
        access_token=bootstrap_response.access_token,
        refresh_token=refresh_token,
    )
    response.headers["Cache-Control"] = "no-store"
    return bootstrap_response
