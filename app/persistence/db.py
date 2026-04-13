"""Database engine and session helpers."""

from __future__ import annotations

from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import get_settings


class Base(DeclarativeBase):
    pass


@lru_cache
def get_engine(database_url: str | None = None):
    settings = get_settings()
    url = database_url or settings.database_url
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, future=True, pool_pre_ping=True, connect_args=connect_args)


@lru_cache
def get_session_factory(database_url: str | None = None) -> sessionmaker[Session]:
    return sessionmaker(bind=get_engine(database_url), autoflush=False, autocommit=False, expire_on_commit=False)


def init_db() -> None:
    from app.auth.passwords import hash_password
    from app.persistence.models import AdminUser, AuditEvent, ChatSession, Tenant, TenantAuthKey, TenantLicense, UsageDaily, UsageEvent
    from app.persistence.repositories import AdminUserRepository

    settings = get_settings()
    if not settings.database_auto_create:
        return
    Base.metadata.create_all(bind=get_engine())
    if not settings.admin_initial_username or not settings.admin_initial_password:
        return

    session = get_session_factory()()
    try:
        admin_users = AdminUserRepository(session)
        existing = admin_users.get_by_username(settings.admin_initial_username)
        if existing is None:
            admin_users.create_user(
                username=settings.admin_initial_username,
                display_name=settings.admin_initial_display_name,
                password_hash=hash_password(settings.admin_initial_password),
            )
            session.commit()
    finally:
        session.close()


def get_db_session():
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()
