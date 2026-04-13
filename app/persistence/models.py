"""SQLAlchemy models for multi-tenant copilot state."""

from __future__ import annotations

import uuid
from datetime import date, datetime

from sqlalchemy import JSON, Boolean, Date, DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.persistence.db import Base


def _uuid() -> str:
    return str(uuid.uuid4())


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    tenant_code: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    display_name: Mapped[str] = mapped_column(String(255))
    issuer: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    status: Mapped[str] = mapped_column(String(40), default="active", index=True)
    license_tier: Mapped[str] = mapped_column(String(40), default="standard")
    allowed_origins: Mapped[list[str]] = mapped_column(JSON, default=list)
    overlay_collection: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    auth_keys: Mapped[list["TenantAuthKey"]] = relationship(back_populates="tenant", cascade="all, delete-orphan")
    license: Mapped["TenantLicense | None"] = relationship(back_populates="tenant", uselist=False, cascade="all, delete-orphan")


class AdminUser(Base):
    __tablename__ = "admin_users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    username: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    display_name: Mapped[str] = mapped_column(String(255))
    password_hash: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class TenantAuthKey(Base):
    __tablename__ = "tenant_auth_keys"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True)
    key_type: Mapped[str] = mapped_column(String(30), default="public_key")
    kid: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    algorithm: Mapped[str] = mapped_column(String(20), default="RS256")
    public_key_pem: Mapped[str | None] = mapped_column(Text, nullable=True)
    jwks_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    api_key_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    api_secret_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="active")
    rotated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False), nullable=True)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)

    tenant: Mapped["Tenant"] = relationship(back_populates="auth_keys")


class TenantLicense(Base):
    __tablename__ = "tenant_licenses"

    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), primary_key=True)
    status: Mapped[str] = mapped_column(String(40), default="active")
    daily_message_limit: Mapped[int] = mapped_column(Integer, default=500)
    daily_token_limit: Mapped[int] = mapped_column(Integer, default=500000)
    burst_rps_limit: Mapped[int] = mapped_column(Integer, default=5)
    concurrent_sessions_limit: Mapped[int] = mapped_column(Integer, default=10)
    overlay_kb_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    erp_tools_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    tenant: Mapped["Tenant"] = relationship(back_populates="license")


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True)
    user_ref_hash: Mapped[str] = mapped_column(String(64), index=True)
    mask_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    screen_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="active")
    client_type: Mapped[str] = mapped_column(String(40), default="embedded_chromium")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)
    last_activity_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False), nullable=True)


class UsageDaily(Base):
    __tablename__ = "usage_daily"
    __table_args__ = (UniqueConstraint("tenant_id", "usage_date", name="uq_usage_daily_tenant_date"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True)
    usage_date: Mapped[date] = mapped_column(Date, index=True)
    messages_in: Mapped[int] = mapped_column(Integer, default=0)
    messages_out: Mapped[int] = mapped_column(Integer, default=0)
    prompt_tokens: Mapped[int] = mapped_column(Integer, default=0)
    completion_tokens: Mapped[int] = mapped_column(Integer, default=0)
    ws_connects: Mapped[int] = mapped_column(Integer, default=0)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class UsageEvent(Base):
    __tablename__ = "usage_events"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id"), index=True)
    session_id: Mapped[str | None] = mapped_column(ForeignKey("chat_sessions.id"), nullable=True, index=True)
    user_ref_hash: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    event_type: Mapped[str] = mapped_column(String(40), index=True)
    message_count: Mapped[int] = mapped_column(Integer, default=0)
    prompt_tokens: Mapped[int] = mapped_column(Integer, default=0)
    completion_tokens: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
    tenant_id: Mapped[str | None] = mapped_column(ForeignKey("tenants.id"), nullable=True, index=True)
    session_id: Mapped[str | None] = mapped_column(ForeignKey("chat_sessions.id"), nullable=True, index=True)
    user_ref_hash: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    actor_type: Mapped[str] = mapped_column(String(40))
    action: Mapped[str] = mapped_column(String(80))
    resource_type: Mapped[str] = mapped_column(String(80))
    resource_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    decision: Mapped[str] = mapped_column(String(40), default="allow")
    reason_code: Mapped[str | None] = mapped_column(String(80), nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.utcnow)
