"""Provider-admin control-plane routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.admin.schemas import (
    ModelSettingsResponse,
    ModelSettingsUpdateRequest,
    TenantCreateRequest,
    TenantKeyRotateRequest,
    TenantLicenseUpdateRequest,
    TenantResponse,
    TenantUpdateRequest,
    TenantUserCreateRequest,
    TenantUserResponse,
    TenantUserSecretResponse,
    TenantUsageDay,
)
from app.admin.services import ModelSettingsService, TenantAdminConflictError, TenantAdminService
from app.auth.dependencies import require_provider_admin
from app.core.config import Settings, get_settings
from app.persistence.db import get_db_session
from app.tenancy.models import AdminPrincipal

router = APIRouter(prefix="/v1/admin", tags=["admin"])


def get_tenant_admin_service(
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
) -> TenantAdminService:
    return TenantAdminService(session=session, settings=settings)


def get_model_settings_service(
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
) -> ModelSettingsService:
    return ModelSettingsService(session=session, settings=settings)


@router.get("/model-settings", response_model=ModelSettingsResponse)
def get_model_settings(
    _: AdminPrincipal = Depends(require_provider_admin),
    service: ModelSettingsService = Depends(get_model_settings_service),
) -> ModelSettingsResponse:
    return service.get()


@router.put("/model-settings", response_model=ModelSettingsResponse)
def update_model_settings(
    request: ModelSettingsUpdateRequest,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: ModelSettingsService = Depends(get_model_settings_service),
) -> ModelSettingsResponse:
    return service.update(request)


@router.get("/tenants", response_model=list[TenantResponse])
def list_tenants(
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> list[TenantResponse]:
    return service.list_tenants()


@router.post("/tenants", response_model=TenantResponse)
def create_tenant(
    request: TenantCreateRequest,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantResponse:
    return service.create_tenant(request)


@router.get("/tenants/{tenant_id}", response_model=TenantResponse)
def get_tenant(
    tenant_id: str,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantResponse:
    try:
        return service.get_tenant(tenant_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.patch("/tenants/{tenant_id}", response_model=TenantResponse)
def patch_tenant(
    tenant_id: str,
    request: TenantUpdateRequest,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantResponse:
    try:
        return service.patch_tenant(tenant_id, request)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.patch("/tenants/{tenant_id}/license", response_model=TenantResponse)
def update_license(
    tenant_id: str,
    request: TenantLicenseUpdateRequest,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantResponse:
    try:
        return service.update_license(tenant_id, request)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/tenants/{tenant_id}/suspend", response_model=TenantResponse)
def suspend_tenant(
    tenant_id: str,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantResponse:
    try:
        return service.set_tenant_status(tenant_id, "suspended")
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/tenants/{tenant_id}/activate", response_model=TenantResponse)
def activate_tenant(
    tenant_id: str,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantResponse:
    try:
        return service.set_tenant_status(tenant_id, "active")
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/tenants/{tenant_id}/keys/rotate", response_model=TenantResponse)
def rotate_key(
    tenant_id: str,
    request: TenantKeyRotateRequest,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantResponse:
    try:
        return service.rotate_key(tenant_id, request)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/tenants/{tenant_id}/usage", response_model=list[TenantUsageDay])
def tenant_usage(
    tenant_id: str,
    days: int = Query(default=7, ge=1, le=31),
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> list[TenantUsageDay]:
    try:
        return service.usage_summary(tenant_id, days=days)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/tenants/{tenant_id}/users", response_model=list[TenantUserResponse])
def list_tenant_users(
    tenant_id: str,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> list[TenantUserResponse]:
    try:
        return service.list_tenant_users(tenant_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/tenants/{tenant_id}/users", response_model=TenantUserSecretResponse)
def create_tenant_user(
    tenant_id: str,
    request: TenantUserCreateRequest,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantUserSecretResponse:
    try:
        return service.create_tenant_user(tenant_id, request)
    except TenantAdminConflictError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post(
    "/tenants/{tenant_id}/users/{user_id}/password/regenerate",
    response_model=TenantUserSecretResponse,
)
def regenerate_tenant_user_password(
    tenant_id: str,
    user_id: str,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> TenantUserSecretResponse:
    try:
        return service.regenerate_tenant_user_password(tenant_id, user_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.delete(
    "/tenants/{tenant_id}/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_tenant_user(
    tenant_id: str,
    user_id: str,
    _: AdminPrincipal = Depends(require_provider_admin),
    service: TenantAdminService = Depends(get_tenant_admin_service),
) -> None:
    try:
        service.delete_tenant_user(tenant_id, user_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
