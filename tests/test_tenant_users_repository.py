from datetime import datetime, timedelta

import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from app.persistence.db import Base
from app.persistence.models import Tenant
from app.persistence.repositories import TenantUsersRepository


def _new_session():
    engine = create_engine("sqlite:///:memory:", future=True)
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine, expire_on_commit=False)
    return session_factory()


def _create_tenant(session, *, tenant_code: str = "acme") -> Tenant:
    tenant = Tenant(
        tenant_code=tenant_code,
        display_name=f"{tenant_code.upper()} SPA",
        issuer=f"urn:{tenant_code}:erp",
        allowed_origins=[],
    )
    session.add(tenant)
    session.flush()
    return tenant


def test_tenant_users_repository_uses_tenant_user_model_fields():
    session = _new_session()
    try:
        tenant = _create_tenant(session)
        repo = TenantUsersRepository(session)
        expires_at = datetime.utcnow() + timedelta(days=1)

        user = repo.create_user(
            tenant_id=tenant.id,
            username="mario.rossi",
            display_name="Mario Rossi",
            password_hash="hash-v1",
            expires_at=expires_at,
        )

        assert user.tenant_id == tenant.id
        assert user.username == "mario.rossi"
        assert user.display_name == "Mario Rossi"
        assert user.password_hash == "hash-v1"
        assert user.status == "active"
        assert user.expires_at == expires_at
        assert repo.get_by_id(tenant.id, user.id) == user
        assert repo.get_by_username(tenant.id, "mario.rossi") == user
        assert repo.get_user(tenant.id, "mario.rossi") == user
        assert repo.get_active_user(tenant.id, "mario.rossi") == user
        assert repo.list_users(tenant.id) == [user]

        repo.update_user(user, display_name="Mario R.")
        assert user.display_name == "Mario R."

        repo.rotate_password(user, password_hash="hash-v2")
        assert user.password_hash == "hash-v2"
        assert user.rotated_at is not None

        repo.set_status(user, "suspended")
        assert user.status == "suspended"
        assert repo.get_active_user(tenant.id, "mario.rossi") is None
    finally:
        session.close()


def test_tenant_users_repository_rejects_duplicate_username_per_tenant():
    session = _new_session()
    try:
        tenant = _create_tenant(session)
        repo = TenantUsersRepository(session)
        repo.create_user(
            tenant_id=tenant.id,
            username="mario.rossi",
            display_name="Mario Rossi",
            password_hash="hash-v1",
        )
        other_tenant = _create_tenant(session, tenant_code="beta")
        other_user = repo.create_user(
            tenant_id=other_tenant.id,
            username="mario.rossi",
            display_name="Mario Rossi",
            password_hash="hash-v1",
        )

        assert other_user.tenant_id == other_tenant.id

        with pytest.raises(IntegrityError):
            repo.create_user(
                tenant_id=tenant.id,
                username="mario.rossi",
                display_name="Mario Rossi 2",
                password_hash="hash-v2",
            )
    finally:
        session.close()
