"""Pydantic models for tenant and principal context."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class TenantContext(BaseModel):
    tenant_id: str
    tenant_code: str
    display_name: str
    status: str
    license_tier: str = "standard"
    allowed_origins: list[str] = Field(default_factory=list)
    overlay_collection: str | None = None
    overlay_kb_enabled: bool = False
    daily_message_limit: int
    daily_token_limit: int
    burst_rps_limit: int
    erp_tools_enabled: bool = False


class SessionPrincipal(BaseModel):
    tenant_id: str
    tenant_code: str
    session_id: str
    user_id: str
    user_ref_hash: str
    roles: list[str] = Field(default_factory=list)
    mask_id: str | None = None
    mask_permissions: list[str] = Field(default_factory=list)
    company_code: str | None = None
    session_expires_at: datetime
    tenant: TenantContext


class AdminPrincipal(BaseModel):
    subject: str = "provider-admin"
    user_id: str | None = None
    username: str = "admin"
    display_name: str = "Amministratore"
    authentication_method: str = "session"
    issued_at: datetime = Field(default_factory=datetime.utcnow)
