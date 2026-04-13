import asyncio
import time
import uuid
from pathlib import Path
from unittest.mock import patch

import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi.testclient import TestClient
from starlette.websockets import WebSocketDisconnect

from app.api.main import create_app
from app.core.config import get_settings
from app.domain.schemas import QueryResponse, ScreenContext, ScreenContextSummary
from app.persistence.db import get_engine, get_session_factory
from app.tenancy.cache import get_state_store
from app.tenancy.security import hash_user_reference

ADMIN_PASSWORD = "dPP23@@12312dS"


def _configure_platform(monkeypatch, tmp_path: Path, *, web_chat_default_tenant_code: str = "") -> TestClient:
    database_url = f"sqlite:///{(tmp_path / 'platform.db').resolve().as_posix()}"
    redis_url = f"memory://{uuid.uuid4()}"
    monkeypatch.setenv("DATABASE_URL", database_url)
    monkeypatch.setenv("REDIS_URL", redis_url)
    monkeypatch.setenv("REDIS_NAMESPACE", f"test-{uuid.uuid4()}")
    monkeypatch.setenv("SESSION_JWT_SECRET", "test-session-secret-with-32-bytes!")
    monkeypatch.setenv("USER_HASH_SALT", "tenant-hash-salt-with-32-bytes!!")
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("ADMIN_INITIAL_USERNAME", "admin")
    monkeypatch.setenv("ADMIN_INITIAL_DISPLAY_NAME", "Amministratore")
    monkeypatch.setenv("ADMIN_INITIAL_PASSWORD", ADMIN_PASSWORD)
    if web_chat_default_tenant_code:
        monkeypatch.setenv("WEB_CHAT_DEFAULT_TENANT_CODE", web_chat_default_tenant_code)
    else:
        monkeypatch.delenv("WEB_CHAT_DEFAULT_TENANT_CODE", raising=False)
    get_settings.cache_clear()
    get_engine.cache_clear()
    get_session_factory.cache_clear()
    return TestClient(create_app())


def _login_admin(client: TestClient, username: str = "admin", password: str = ADMIN_PASSWORD) -> dict:
    response = client.post("/v1/admin-auth/login", json={"username": username, "password": password})
    assert response.status_code == 200, response.text
    return response.json()


def _generate_keypair() -> tuple[str, str]:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")
    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("utf-8")
    return private_pem, public_pem


def _create_tenant(
    client: TestClient,
    public_key_pem: str | None = None,
    *,
    tenant_code: str = "acme",
    display_name: str = "ACME SPA",
    issuer: str = "urn:acme:erp",
    allowed_origins: list[str] | None = None,
) -> dict:
    response = client.post(
        "/v1/admin/tenants",
        json={
            "tenant_code": tenant_code,
            "display_name": display_name,
            "issuer": issuer,
            "allowed_origins": allowed_origins or [],
            "license_tier": "standard",
            "public_key_pem": public_key_pem,
            "public_key_kid": "kid-1" if public_key_pem else None,
            "license": {
                "status": "active",
                "daily_message_limit": 20,
                "daily_token_limit": 20000,
                "burst_rps_limit": 5,
                "concurrent_sessions_limit": 5,
                "overlay_kb_enabled": True,
                "erp_tools_enabled": False,
            },
        },
    )
    assert response.status_code == 200, response.text
    return response.json()


def _bootstrap_token(private_key_pem: str, tenant: dict, user_id: str = "mario.rossi") -> str:
    now = int(time.time())
    payload = {
        "iss": tenant["issuer"],
        "aud": "rag-doc-bootstrap",
        "tid": tenant["id"],
        "sub": user_id,
        "jti": str(uuid.uuid4()),
        "iat": now,
        "exp": now + 120,
        "roles": ["accounting"],
        "mask_id": "FAT-001",
        "mask_permissions": ["chat:use"],
        "company_code": "IT01",
    }
    return jwt.encode(payload, private_key_pem, algorithm="RS256", headers={"kid": "kid-1"})


def _bootstrap(client: TestClient, private_key_pem: str, tenant: dict, user_id: str = "mario.rossi") -> dict:
    token = _bootstrap_token(private_key_pem, tenant, user_id=user_id)
    response = client.post("/v1/auth/bootstrap", json={"bootstrap_token": token})
    assert response.status_code == 200, response.text
    return response.json()


def _sample_query_response() -> QueryResponse:
    return QueryResponse(
        answer="Apri Fatture e compila la testata.",
        steps=["Apri Fatture", "Compila la testata"],
        citations=[],
        follow_up_question=None,
        confidence=0.91,
        used_screen_context=ScreenContextSummary(
            application="ERP",
            module="Contabilita",
            submenu="Fatture",
            screen_id="FAT-001",
            screen_title="Fatture",
            tab_name="Testata",
            current_action="Creazione",
            breadcrumb=["ERP", "Contabilita", "Fatture"],
            error_messages=[],
            field_count=0,
            sensitive_field_count=0,
        ),
        redaction_notice=None,
        answer_mode="grounded",
        inference_notice=None,
    )


def test_bootstrap_auth_and_admin_lifecycle(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        _login_admin(client)
        private_key_pem, public_key_pem = _generate_keypair()
        tenant = _create_tenant(client, public_key_pem)

        bootstrap = _bootstrap(client, private_key_pem, tenant)
        assert bootstrap["tenant_code"] == "acme"

        ws_ticket = client.post(
            "/v1/chat/ws-ticket",
            headers={"Authorization": f"Bearer {bootstrap['access_token']}"},
        )
        assert ws_ticket.status_code == 200

        suspended = client.post(f"/v1/admin/tenants/{tenant['id']}/suspend")
        assert suspended.status_code == 200
        assert suspended.json()["status"] == "suspended"

        blocked_ticket = client.post(
            "/v1/chat/ws-ticket",
            headers={"Authorization": f"Bearer {bootstrap['access_token']}"},
        )
        assert blocked_ticket.status_code == 403

        activated = client.post(f"/v1/admin/tenants/{tenant['id']}/activate")
        assert activated.status_code == 200
        assert activated.json()["status"] == "active"

        inspect_tenant = client.get(f"/v1/admin/tenants/{tenant['id']}")
        assert inspect_tenant.status_code == 200
        assert inspect_tenant.json()["active_kid"] == "kid-1"


def test_bootstrap_token_replay_is_rejected(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        _login_admin(client)
        private_key_pem, public_key_pem = _generate_keypair()
        tenant = _create_tenant(client, public_key_pem)
        token = _bootstrap_token(private_key_pem, tenant)

        first = client.post("/v1/auth/bootstrap", json={"bootstrap_token": token})
        second = client.post("/v1/auth/bootstrap", json={"bootstrap_token": token})

        assert first.status_code == 200
        assert second.status_code == 401
        assert "gia utilizzato" in second.json()["detail"]


def test_websocket_ticket_is_single_use_and_memory_is_tenant_scoped(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        _login_admin(client)
        private_key_pem, public_key_pem = _generate_keypair()
        tenant = _create_tenant(client, public_key_pem)
        bootstrap = _bootstrap(client, private_key_pem, tenant)
        ticket_response = client.post(
            "/v1/chat/ws-ticket",
            headers={"Authorization": f"Bearer {bootstrap['access_token']}"},
        )
        assert ticket_response.status_code == 200
        ticket = ticket_response.json()["ticket"]
        captured_request = {}

        def _fake_run(query_request, conversation_history=None):
            captured_request["request"] = query_request
            return _sample_query_response()

        with patch("app.chat.service.TenantAwareRAGService.run_chat_request", side_effect=_fake_run):
            with client.websocket_connect(f"/v1/chat/ws?ticket={ticket}") as websocket:
                ready = websocket.receive_json()
                assert ready["type"] == "ready"
                websocket.send_json(
                    {
                        "type": "user_message",
                        "message": "Come creo una fattura?",
                        "retrieval_options": {"role_scope": ["sales"]},
                        "user_context": {"username": "evil-user", "roles": ["sales"], "company_code": "IT99"},
                        "screen_context": ScreenContext(
                            application="ERP",
                            module="Contabilita",
                            submenu="Fatture",
                            screen_id="FAT-001",
                            screen_title="Fatture",
                            tab_name="Testata",
                            breadcrumb=["ERP", "Contabilita", "Fatture"],
                            current_action="Creazione",
                            error_messages=[],
                            fields=[],
                        ).model_dump(),
                    }
                )
                payload = websocket.receive_json()
                assert payload["type"] == "final"
                assert payload["answer"] == "Apri Fatture e compila la testata."
                assert captured_request["request"].user_context.roles == ["accounting"]
                assert captured_request["request"].retrieval_options.role_scope == ["accounting"]

        with pytest.raises(WebSocketDisconnect):
            with client.websocket_connect(f"/v1/chat/ws?ticket={ticket}"):
                pass

        settings = get_settings()
        user_ref_hash = hash_user_reference(tenant["id"], "mario.rossi", settings.user_hash_salt)
        state_store = get_state_store(settings)
        history = asyncio.run(
            state_store.read_list(f"chat:memory:{tenant['id']}:{user_ref_hash}:{bootstrap['session_id']}")
        )
        assert [item["role"] for item in history] == ["user", "assistant"]

        usage = client.get(f"/v1/admin/tenants/{tenant['id']}/usage")
        assert usage.status_code == 200
        assert usage.json()[-1]["messages_in"] == 1
        assert usage.json()[-1]["ws_connects"] == 1


def test_open_websocket_blocks_after_tenant_suspension(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        _login_admin(client)
        private_key_pem, public_key_pem = _generate_keypair()
        tenant = _create_tenant(client, public_key_pem)
        bootstrap = _bootstrap(client, private_key_pem, tenant)
        ticket = client.post(
            "/v1/chat/ws-ticket",
            headers={"Authorization": f"Bearer {bootstrap['access_token']}"},
        ).json()["ticket"]

        with client.websocket_connect(f"/v1/chat/ws?ticket={ticket}") as websocket:
            ready = websocket.receive_json()
            assert ready["type"] == "ready"

            suspended = client.post(f"/v1/admin/tenants/{tenant['id']}/suspend")
            assert suspended.status_code == 200

            websocket.send_json(
                {
                    "type": "user_message",
                    "message": "Posso continuare?",
                    "screen_context": ScreenContext(
                        application="ERP",
                        module="Contabilita",
                        submenu="Fatture",
                        screen_id="FAT-001",
                        screen_title="Fatture",
                        tab_name="Testata",
                        breadcrumb=["ERP", "Contabilita", "Fatture"],
                        current_action="Creazione",
                        error_messages=[],
                        fields=[],
                    ).model_dump(),
                }
            )
            error = websocket.receive_json()
            assert error["type"] == "error"
            assert "tenant" in error["detail"].lower()


def test_allowed_origins_are_enforced_when_origin_header_is_present(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        _login_admin(client)
        private_key_pem, public_key_pem = _generate_keypair()
        tenant = _create_tenant(client, public_key_pem, allowed_origins=["https://erp.acme.local"])
        token = _bootstrap_token(private_key_pem, tenant)

        blocked = client.post(
            "/v1/auth/bootstrap",
            headers={"Origin": "https://evil.example"},
            json={"bootstrap_token": token},
        )
        assert blocked.status_code == 401

        allowed = client.post(
            "/v1/auth/bootstrap",
            headers={"Origin": "https://erp.acme.local"},
            json={"bootstrap_token": token},
        )
        assert allowed.status_code == 200

        denied_ticket = client.post(
            "/v1/chat/ws-ticket",
            headers={
                "Authorization": f"Bearer {allowed.json()['access_token']}",
                "Origin": "https://evil.example",
            },
        )
        assert denied_ticket.status_code == 403


def test_admin_login_protects_admin_routes(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        denied = client.get("/v1/admin/tenants")
        assert denied.status_code == 401

        login = client.post("/v1/admin-auth/login", json={"username": "admin", "password": ADMIN_PASSWORD})
        assert login.status_code == 200
        assert login.json()["display_name"] == "Amministratore"
        assert get_settings().admin_session_cookie_name in client.cookies

        me = client.get("/v1/admin-auth/me")
        assert me.status_code == 200
        assert me.json()["username"] == "admin"

        allowed = client.get("/v1/admin/tenants")
        assert allowed.status_code == 200
        assert allowed.json() == []

        logout = client.post("/v1/admin-auth/logout")
        assert logout.status_code == 204

        denied_again = client.get("/v1/admin/tenants")
        assert denied_again.status_code == 401


def test_admin_login_rejects_invalid_password(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        response = client.post("/v1/admin-auth/login", json={"username": "admin", "password": "password-sbagliata"})
        assert response.status_code == 401
        assert response.json()["detail"] == "Credenziali non valide."


def test_web_chat_session_uses_default_tenant_cookie(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path, web_chat_default_tenant_code="web-chat") as client:
        _login_admin(client)
        tenant = _create_tenant(
            client,
            tenant_code="web-chat",
            display_name="Assistenza clienti",
            issuer="urn:web-chat",
        )

        started = client.post("/v1/chat/web/session")
        assert started.status_code == 200, started.text
        session_payload = started.json()
        assert session_payload["display_name"] == "Assistenza clienti"
        assert session_payload["session_id"]
        assert get_settings().chat_session_cookie_name in client.cookies

        ticket = client.post("/v1/chat/ws-ticket")
        assert ticket.status_code == 200
        assert ticket.json()["ticket"]

        closed = client.post(f"/v1/chat/session/{session_payload['session_id']}/close")
        assert closed.status_code == 204

        after_close = client.post("/v1/chat/ws-ticket")
        assert after_close.status_code == 401


def test_web_chat_session_returns_graceful_message_when_default_tenant_is_missing(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path, web_chat_default_tenant_code="web-chat") as client:
        response = client.post("/v1/chat/web/session")
        assert response.status_code == 503
        assert response.json()["detail"] == "Servizio momentaneamente non disponibile."


def test_chat_ui_is_not_served_by_api(monkeypatch, tmp_path: Path):
    with _configure_platform(monkeypatch, tmp_path) as client:
        response = client.get("/chat")
        assert response.status_code == 404
