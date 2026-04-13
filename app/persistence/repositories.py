"""Repository helpers for the multi-tenant control plane."""

from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.persistence.models import AdminUser, AuditEvent, ChatSession, Tenant, TenantAuthKey, TenantLicense, UsageDaily, UsageEvent
from app.tenancy.models import TenantContext


class AdminUserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, user_id: str) -> AdminUser | None:
        return self.session.get(AdminUser, user_id)

    def get_by_username(self, username: str) -> AdminUser | None:
        return self.session.scalar(select(AdminUser).where(AdminUser.username == username))

    def create_user(
        self,
        *,
        username: str,
        display_name: str,
        password_hash: str,
        is_active: bool = True,
    ) -> AdminUser:
        user = AdminUser(
            username=username,
            display_name=display_name,
            password_hash=password_hash,
            is_active=is_active,
        )
        self.session.add(user)
        self.session.flush()
        return user

    def save(self, user: AdminUser) -> AdminUser:
        self.session.add(user)
        self.session.flush()
        return user


class TenantRepository:
    def __init__(self, session: Session, settings: Settings) -> None:
        self.session = session
        self.settings = settings

    def list_tenants(self) -> list[Tenant]:
        return list(self.session.scalars(select(Tenant).order_by(Tenant.created_at.desc())))

    def get_tenant(self, tenant_id: str) -> Tenant | None:
        return self.session.get(Tenant, tenant_id)

    def get_tenant_by_code(self, tenant_code: str) -> Tenant | None:
        return self.session.scalar(select(Tenant).where(Tenant.tenant_code == tenant_code))

    def get_tenant_by_issuer(self, issuer: str) -> Tenant | None:
        return self.session.scalar(select(Tenant).where(Tenant.issuer == issuer))

    def create_tenant(
        self,
        tenant_code: str,
        display_name: str,
        issuer: str,
        allowed_origins: list[str],
        license_tier: str,
        overlay_collection: str | None = None,
    ) -> Tenant:
        tenant = Tenant(
            tenant_code=tenant_code,
            display_name=display_name,
            issuer=issuer,
            status="active",
            license_tier=license_tier,
            allowed_origins=allowed_origins,
            overlay_collection=overlay_collection,
        )
        license_record = TenantLicense(
            tenant=tenant,
            status="active",
            daily_message_limit=self.settings.default_daily_message_limit,
            daily_token_limit=self.settings.default_daily_token_limit,
            burst_rps_limit=self.settings.default_burst_rps_limit,
        )
        tenant.license = license_record
        self.session.add(tenant)
        self.session.flush()
        return tenant

    def update_tenant(
        self,
        tenant: Tenant,
        *,
        display_name: str | None = None,
        status: str | None = None,
        allowed_origins: list[str] | None = None,
        license_tier: str | None = None,
        overlay_collection: str | None = None,
    ) -> Tenant:
        if display_name is not None:
            tenant.display_name = display_name
        if status is not None:
            tenant.status = status
        if allowed_origins is not None:
            tenant.allowed_origins = allowed_origins
        if license_tier is not None:
            tenant.license_tier = license_tier
        if overlay_collection is not None:
            tenant.overlay_collection = overlay_collection
        self.session.add(tenant)
        self.session.flush()
        return tenant

    def upsert_license(
        self,
        tenant: Tenant,
        *,
        status: str | None = None,
        daily_message_limit: int | None = None,
        daily_token_limit: int | None = None,
        burst_rps_limit: int | None = None,
        concurrent_sessions_limit: int | None = None,
        overlay_kb_enabled: bool | None = None,
        erp_tools_enabled: bool | None = None,
    ) -> TenantLicense:
        license_record = tenant.license or TenantLicense(tenant=tenant)
        if status is not None:
            license_record.status = status
        if daily_message_limit is not None:
            license_record.daily_message_limit = daily_message_limit
        if daily_token_limit is not None:
            license_record.daily_token_limit = daily_token_limit
        if burst_rps_limit is not None:
            license_record.burst_rps_limit = burst_rps_limit
        if concurrent_sessions_limit is not None:
            license_record.concurrent_sessions_limit = concurrent_sessions_limit
        if overlay_kb_enabled is not None:
            license_record.overlay_kb_enabled = overlay_kb_enabled
        if erp_tools_enabled is not None:
            license_record.erp_tools_enabled = erp_tools_enabled
        tenant.license = license_record
        self.session.add(license_record)
        self.session.flush()
        return license_record

    def rotate_public_key(
        self,
        tenant: Tenant,
        *,
        public_key_pem: str,
        kid: str | None,
        algorithm: str = "RS256",
    ) -> TenantAuthKey:
        existing = list(self.session.scalars(select(TenantAuthKey).where(TenantAuthKey.tenant_id == tenant.id)))
        for key in existing:
            key.status = "inactive"
            key.rotated_at = datetime.utcnow()
            self.session.add(key)

        key = TenantAuthKey(
            tenant_id=tenant.id,
            key_type="public_key",
            kid=kid,
            algorithm=algorithm,
            public_key_pem=public_key_pem,
            status="active",
        )
        self.session.add(key)
        self.session.flush()
        return key

    def get_active_key(self, tenant_id: str, kid: str | None = None) -> TenantAuthKey | None:
        stmt = select(TenantAuthKey).where(
            TenantAuthKey.tenant_id == tenant_id,
            TenantAuthKey.status == "active",
        )
        if kid is not None:
            stmt = stmt.where(TenantAuthKey.kid == kid)
        stmt = stmt.order_by(desc(TenantAuthKey.created_at))
        key = self.session.scalar(stmt)
        if key or kid is None:
            return key
        return self.session.scalar(
            select(TenantAuthKey)
            .where(TenantAuthKey.tenant_id == tenant_id, TenantAuthKey.status == "active")
            .order_by(desc(TenantAuthKey.created_at))
        )

    def to_context(self, tenant: Tenant) -> TenantContext:
        license_record = tenant.license or TenantLicense(
            daily_message_limit=self.settings.default_daily_message_limit,
            daily_token_limit=self.settings.default_daily_token_limit,
            burst_rps_limit=self.settings.default_burst_rps_limit,
        )
        return TenantContext(
            tenant_id=tenant.id,
            tenant_code=tenant.tenant_code,
            display_name=tenant.display_name,
            status=tenant.status,
            license_tier=tenant.license_tier,
            allowed_origins=tenant.allowed_origins,
            overlay_collection=tenant.overlay_collection,
            overlay_kb_enabled=license_record.overlay_kb_enabled,
            daily_message_limit=license_record.daily_message_limit,
            daily_token_limit=license_record.daily_token_limit,
            burst_rps_limit=license_record.burst_rps_limit,
            erp_tools_enabled=license_record.erp_tools_enabled,
        )


class ChatSessionRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_session(
        self,
        *,
        tenant_id: str,
        user_ref_hash: str,
        mask_id: str | None,
        screen_id: str | None,
        client_type: str = "embedded_chromium",
    ) -> ChatSession:
        chat_session = ChatSession(
            tenant_id=tenant_id,
            user_ref_hash=user_ref_hash,
            mask_id=mask_id,
            screen_id=screen_id,
            client_type=client_type,
        )
        self.session.add(chat_session)
        self.session.flush()
        return chat_session

    def get_session(self, session_id: str) -> ChatSession | None:
        return self.session.get(ChatSession, session_id)

    def touch_session(self, chat_session: ChatSession, *, screen_id: str | None = None) -> ChatSession:
        chat_session.last_activity_at = datetime.utcnow()
        if screen_id is not None:
            chat_session.screen_id = screen_id
        self.session.add(chat_session)
        self.session.flush()
        return chat_session

    def close_session(self, chat_session: ChatSession) -> ChatSession:
        chat_session.status = "closed"
        chat_session.ended_at = datetime.utcnow()
        chat_session.last_activity_at = chat_session.ended_at
        self.session.add(chat_session)
        self.session.flush()
        return chat_session


class UsageRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_daily_usage(self, tenant_id: str, usage_date: date) -> UsageDaily | None:
        return self.session.scalar(
            select(UsageDaily).where(UsageDaily.tenant_id == tenant_id, UsageDaily.usage_date == usage_date)
        )

    def record_daily_usage(
        self,
        *,
        tenant_id: str,
        usage_date: date,
        messages_in: int = 0,
        messages_out: int = 0,
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
        ws_connects: int = 0,
    ) -> UsageDaily:
        row = self.get_daily_usage(tenant_id, usage_date)
        if row is None:
            row = UsageDaily(
                tenant_id=tenant_id,
                usage_date=usage_date,
                messages_in=0,
                messages_out=0,
                prompt_tokens=0,
                completion_tokens=0,
                ws_connects=0,
            )
        row.messages_in += messages_in
        row.messages_out += messages_out
        row.prompt_tokens += prompt_tokens
        row.completion_tokens += completion_tokens
        row.ws_connects += ws_connects
        self.session.add(row)
        self.session.flush()
        return row

    def record_usage_event(
        self,
        *,
        tenant_id: str,
        session_id: str | None,
        user_ref_hash: str | None,
        event_type: str,
        message_count: int = 0,
        prompt_tokens: int = 0,
        completion_tokens: int = 0,
    ) -> UsageEvent:
        event = UsageEvent(
            tenant_id=tenant_id,
            session_id=session_id,
            user_ref_hash=user_ref_hash,
            event_type=event_type,
            message_count=message_count,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
        )
        self.session.add(event)
        self.session.flush()
        return event

    def usage_summary(self, tenant_id: str, *, days: int = 7) -> list[UsageDaily]:
        stmt = (
            select(UsageDaily)
            .where(UsageDaily.tenant_id == tenant_id)
            .order_by(desc(UsageDaily.usage_date))
            .limit(days)
        )
        return list(reversed(list(self.session.scalars(stmt))))


class AuditRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def record(
        self,
        *,
        tenant_id: str | None,
        session_id: str | None,
        user_ref_hash: str | None,
        actor_type: str,
        action: str,
        resource_type: str,
        resource_id: str | None,
        decision: str,
        reason_code: str | None = None,
        metadata_json: dict | None = None,
    ) -> AuditEvent:
        event = AuditEvent(
            tenant_id=tenant_id,
            session_id=session_id,
            user_ref_hash=user_ref_hash,
            actor_type=actor_type,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            decision=decision,
            reason_code=reason_code,
            metadata_json=metadata_json,
        )
        self.session.add(event)
        self.session.flush()
        return event
