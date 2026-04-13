"""Provider-admin services for tenants, licenses, keys, and usage."""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.admin.schemas import (
    TenantCreateRequest,
    TenantKeyRotateRequest,
    TenantLicenseResponse,
    TenantLicenseUpdateRequest,
    TenantResponse,
    TenantUpdateRequest,
    TenantUsageDay,
)
from app.core.config import Settings
from app.persistence.models import Tenant, TenantAuthKey
from app.persistence.repositories import AuditRepository, TenantRepository, UsageRepository


class TenantAdminService:
    def __init__(self, session: Session, settings: Settings) -> None:
        self.session = session
        self.settings = settings
        self.tenants = TenantRepository(session, settings)
        self.usage = UsageRepository(session)
        self.audit = AuditRepository(session)

    def list_tenants(self) -> list[TenantResponse]:
        return [self._to_response(item) for item in self.tenants.list_tenants()]

    def get_tenant(self, tenant_id: str) -> TenantResponse:
        tenant = self._require_tenant(tenant_id)
        return self._to_response(tenant)

    def create_tenant(self, request: TenantCreateRequest) -> TenantResponse:
        tenant = self.tenants.create_tenant(
            tenant_code=request.tenant_code,
            display_name=request.display_name,
            issuer=request.issuer,
            allowed_origins=request.allowed_origins,
            license_tier=request.license_tier,
            overlay_collection=request.overlay_collection,
        )
        if request.license:
            self.tenants.upsert_license(tenant, **request.license.model_dump())
        if request.public_key_pem:
            self.tenants.rotate_public_key(
                tenant,
                public_key_pem=request.public_key_pem,
                kid=request.public_key_kid,
            )
        self.audit.record(
            tenant_id=tenant.id,
            session_id=None,
            user_ref_hash=None,
            actor_type="provider_admin",
            action="create_tenant",
            resource_type="tenant",
            resource_id=tenant.id,
            decision="allow",
        )
        self.session.commit()
        return self._to_response(tenant)

    def patch_tenant(self, tenant_id: str, request: TenantUpdateRequest) -> TenantResponse:
        tenant = self._require_tenant(tenant_id)
        tenant = self.tenants.update_tenant(tenant, **request.model_dump(exclude_none=True))
        self.audit.record(
            tenant_id=tenant.id,
            session_id=None,
            user_ref_hash=None,
            actor_type="provider_admin",
            action="update_tenant",
            resource_type="tenant",
            resource_id=tenant.id,
            decision="allow",
        )
        self.session.commit()
        return self._to_response(tenant)

    def set_tenant_status(self, tenant_id: str, status: str) -> TenantResponse:
        tenant = self._require_tenant(tenant_id)
        tenant = self.tenants.update_tenant(tenant, status=status)
        self.audit.record(
            tenant_id=tenant.id,
            session_id=None,
            user_ref_hash=None,
            actor_type="provider_admin",
            action=f"set_status:{status}",
            resource_type="tenant",
            resource_id=tenant.id,
            decision="allow",
        )
        self.session.commit()
        return self._to_response(tenant)

    def update_license(self, tenant_id: str, request: TenantLicenseUpdateRequest) -> TenantResponse:
        tenant = self._require_tenant(tenant_id)
        self.tenants.upsert_license(tenant, **request.model_dump(exclude_none=True))
        self.audit.record(
            tenant_id=tenant.id,
            session_id=None,
            user_ref_hash=None,
            actor_type="provider_admin",
            action="update_license",
            resource_type="tenant_license",
            resource_id=tenant.id,
            decision="allow",
        )
        self.session.commit()
        return self._to_response(tenant)

    def rotate_key(self, tenant_id: str, request: TenantKeyRotateRequest) -> TenantResponse:
        tenant = self._require_tenant(tenant_id)
        self.tenants.rotate_public_key(
            tenant,
            public_key_pem=request.public_key_pem,
            kid=request.kid,
            algorithm=request.algorithm,
        )
        self.audit.record(
            tenant_id=tenant.id,
            session_id=None,
            user_ref_hash=None,
            actor_type="provider_admin",
            action="rotate_key",
            resource_type="tenant_auth_key",
            resource_id=tenant.id,
            decision="allow",
        )
        self.session.commit()
        return self._to_response(tenant)

    def usage_summary(self, tenant_id: str, *, days: int = 7) -> list[TenantUsageDay]:
        self._require_tenant(tenant_id)
        return [
            TenantUsageDay(
                usage_date=row.usage_date,
                messages_in=row.messages_in,
                messages_out=row.messages_out,
                prompt_tokens=row.prompt_tokens,
                completion_tokens=row.completion_tokens,
                ws_connects=row.ws_connects,
            )
            for row in self.usage.usage_summary(tenant_id, days=days)
        ]

    def _require_tenant(self, tenant_id: str) -> Tenant:
        tenant = self.tenants.get_tenant(tenant_id)
        if tenant is None:
            raise ValueError("Tenant non trovato.")
        return tenant

    def _active_key(self, tenant: Tenant) -> TenantAuthKey | None:
        keys = [key for key in tenant.auth_keys if key.status == "active"]
        if not keys:
            return None
        keys.sort(key=lambda item: item.created_at, reverse=True)
        return keys[0]

    def _to_response(self, tenant: Tenant) -> TenantResponse:
        license_record = tenant.license
        if license_record is None:
            license_record = self.tenants.upsert_license(tenant)
        active_key = self._active_key(tenant)
        return TenantResponse(
            id=tenant.id,
            tenant_code=tenant.tenant_code,
            display_name=tenant.display_name,
            issuer=tenant.issuer,
            status=tenant.status,
            license_tier=tenant.license_tier,
            allowed_origins=tenant.allowed_origins,
            overlay_collection=tenant.overlay_collection,
            active_kid=active_key.kid if active_key else None,
            license=TenantLicenseResponse(
                status=license_record.status,
                daily_message_limit=license_record.daily_message_limit,
                daily_token_limit=license_record.daily_token_limit,
                burst_rps_limit=license_record.burst_rps_limit,
                concurrent_sessions_limit=license_record.concurrent_sessions_limit,
                overlay_kb_enabled=license_record.overlay_kb_enabled,
                erp_tools_enabled=license_record.erp_tools_enabled,
            ),
        )
