"""Tenant access and quota helpers built on the persistence layer."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime

from sqlalchemy.orm import Session

from app.core.config import Settings
from app.persistence.models import Tenant
from app.persistence.repositories import AuditRepository, TenantRepository, UsageRepository
from app.tenancy.cache import AsyncStateStore
from app.tenancy.models import SessionPrincipal, TenantContext


class TenantAccessError(RuntimeError):
    def __init__(self, message: str, *, reason_code: str = "tenant_blocked", status_code: int = 403) -> None:
        super().__init__(message)
        self.reason_code = reason_code
        self.status_code = status_code


@dataclass
class UsageSnapshot:
    usage_date: date
    messages_in: int = 0
    messages_out: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    ws_connects: int = 0


class TenantAccessService:
    def __init__(
        self,
        session: Session,
        settings: Settings,
        audit_repository: AuditRepository | None = None,
    ) -> None:
        self.session = session
        self.settings = settings
        self.tenants = TenantRepository(session, settings)
        self.usage = UsageRepository(session)
        self.audit = audit_repository or AuditRepository(session)

    def require_active_tenant(self, tenant_id: str) -> Tenant:
        tenant = self.tenants.get_tenant(tenant_id)
        if tenant is None:
            raise TenantAccessError("Tenant non trovato.", reason_code="tenant_not_found", status_code=404)
        if tenant.status not in {"active"}:
            raise TenantAccessError(
                "Tenant non abilitato all'uso del chatbot.",
                reason_code=f"tenant_{tenant.status}",
                status_code=403,
            )
        if tenant.license and tenant.license.status not in {"active"}:
            raise TenantAccessError(
                "Licenza tenant non attiva.",
                reason_code="license_inactive",
                status_code=403,
            )
        return tenant

    def require_tenant_allowed(self, tenant_id: str) -> TenantContext:
        tenant = self.require_active_tenant(tenant_id)
        context = self.tenants.to_context(tenant)
        usage_row = self.usage.get_daily_usage(tenant.id, datetime.utcnow().date())
        if usage_row and context.daily_message_limit and usage_row.messages_in >= context.daily_message_limit:
            tenant.status = "quota_exceeded"
            self.session.add(tenant)
            self.session.commit()
            raise TenantAccessError(
                "Quota giornaliera messaggi esaurita per il tenant.",
                reason_code="daily_message_limit",
                status_code=429,
            )
        if usage_row:
            total_tokens = usage_row.prompt_tokens + usage_row.completion_tokens
            if context.daily_token_limit and total_tokens >= context.daily_token_limit:
                tenant.status = "quota_exceeded"
                self.session.add(tenant)
                self.session.commit()
                raise TenantAccessError(
                    "Quota giornaliera token esaurita per il tenant.",
                    reason_code="daily_token_limit",
                    status_code=429,
                )
        return context


class QuotaService:
    def __init__(
        self,
        session: Session,
        settings: Settings,
        state_store: AsyncStateStore,
    ) -> None:
        self.session = session
        self.settings = settings
        self.state_store = state_store
        self.tenants = TenantRepository(session, settings)
        self.usage = UsageRepository(session)

    async def enforce_burst_limit(self, principal: SessionPrincipal) -> None:
        if principal.tenant.burst_rps_limit <= 0:
            return
        second_window = int(datetime.utcnow().timestamp())
        key = f"rate:tenant:{principal.tenant_id}:{second_window}"
        value = await self.state_store.increment(key, ttl_seconds=2, amount=1)
        if value > principal.tenant.burst_rps_limit:
            raise TenantAccessError(
                "Limite di burst superato per il tenant.",
                reason_code="burst_limit",
                status_code=429,
            )

    def record_ws_connect(self, principal: SessionPrincipal) -> UsageSnapshot:
        row = self.usage.record_daily_usage(
            tenant_id=principal.tenant_id,
            usage_date=datetime.utcnow().date(),
            ws_connects=1,
        )
        self.usage.record_usage_event(
            tenant_id=principal.tenant_id,
            session_id=principal.session_id,
            user_ref_hash=principal.user_ref_hash,
            event_type="ws_connect",
        )
        self.session.commit()
        return UsageSnapshot(
            usage_date=row.usage_date,
            ws_connects=row.ws_connects,
            messages_in=row.messages_in,
            messages_out=row.messages_out,
            prompt_tokens=row.prompt_tokens,
            completion_tokens=row.completion_tokens,
        )

    def record_turn(
        self,
        principal: SessionPrincipal,
        *,
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
    ) -> UsageSnapshot:
        row = self.usage.record_daily_usage(
            tenant_id=principal.tenant_id,
            usage_date=datetime.utcnow().date(),
            messages_in=1,
            messages_out=1,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
        )
        self.usage.record_usage_event(
            tenant_id=principal.tenant_id,
            session_id=principal.session_id,
            user_ref_hash=principal.user_ref_hash,
            event_type="chat_turn",
            message_count=1,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
        )
        tenant = self.tenants.get_tenant(principal.tenant_id)
        if tenant and tenant.license:
            total_tokens = row.prompt_tokens + row.completion_tokens
            if (
                tenant.license.daily_message_limit
                and row.messages_in >= tenant.license.daily_message_limit
            ) or (
                tenant.license.daily_token_limit
                and total_tokens >= tenant.license.daily_token_limit
            ):
                tenant.status = "quota_exceeded"
                self.session.add(tenant)
        self.session.commit()
        return UsageSnapshot(
            usage_date=row.usage_date,
            messages_in=row.messages_in,
            messages_out=row.messages_out,
            prompt_tokens=row.prompt_tokens,
            completion_tokens=row.completion_tokens,
            ws_connects=row.ws_connects,
        )
