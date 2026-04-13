"""Database models and repositories for the multi-tenant copilot."""

from app.persistence.db import Base, get_db_session, get_engine, get_session_factory, init_db
from app.persistence.models import AdminUser, AuditEvent, ChatSession, Tenant, TenantAuthKey, TenantLicense, UsageDaily, UsageEvent
from app.persistence.repositories import AdminUserRepository, AuditRepository, ChatSessionRepository, TenantRepository, UsageRepository

__all__ = [
    "AdminUser",
    "AdminUserRepository",
    "AuditEvent",
    "AuditRepository",
    "Base",
    "ChatSession",
    "ChatSessionRepository",
    "Tenant",
    "TenantAuthKey",
    "TenantLicense",
    "TenantRepository",
    "UsageDaily",
    "UsageEvent",
    "UsageRepository",
    "get_db_session",
    "get_engine",
    "get_session_factory",
    "init_db",
]
