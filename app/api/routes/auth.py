"""Bootstrap auth routes for ERP clients."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request

from app.auth.dependencies import get_auth_service
from app.auth.schemas import BootstrapRequest, BootstrapResponse
from app.auth.services import AuthService
from app.auth.tokens import TokenValidationError
from app.tenancy.services import TenantAccessError

router = APIRouter(prefix="/v1/auth", tags=["auth"])


@router.post("/bootstrap", response_model=BootstrapResponse)
async def bootstrap(
    request: BootstrapRequest,
    raw_request: Request,
    auth_service: AuthService = Depends(get_auth_service),
) -> BootstrapResponse:
    try:
        return await auth_service.bootstrap(request, origin=raw_request.headers.get("origin"))
    except (TokenValidationError, TenantAccessError) as exc:
        status_code = getattr(exc, "status_code", 401)
        raise HTTPException(status_code=status_code, detail=str(exc)) from exc
