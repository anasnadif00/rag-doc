"""Configuration loading for the ERP copilot application."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _parse_csv_env(name: str) -> tuple[str, ...]:
    value = os.getenv(name, "")
    if not value:
        return ()
    return tuple(item.strip() for item in value.split(",") if item.strip())


def _resolve_project_path(value: str) -> str:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return str(path.resolve())


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    qdrant_url: str
    qdrant_collection: str
    embedding_model: str
    generation_model: str
    knowledge_base_path: str
    default_locale: str
    erp_version: str
    top_k: int
    max_context_chars: int
    lexical_index_path: str
    dense_candidate_limit: int
    lexical_candidate_limit: int
    retrieval_min_score: float
    retrieval_relative_score_floor: float
    redaction_allowlist: tuple[str, ...]
    redaction_denylist: tuple[str, ...]
    database_url: str = "sqlite:///./.tmp/rag_doc_platform.db"
    database_auto_create: bool = True
    redis_url: str = "memory://rag-doc"
    redis_namespace: str = "rag-doc"
    bootstrap_jwt_audience: str = "rag-doc-bootstrap"
    session_jwt_audience: str = "rag-doc-api"
    session_jwt_issuer: str = "rag-doc-api"
    session_jwt_algorithm: str = "HS256"
    session_jwt_secret: str = ""
    session_ttl_seconds: int = 900
    admin_session_jwt_audience: str = "rag-doc-admin"
    admin_session_jwt_issuer: str = "rag-doc-admin"
    admin_session_ttl_seconds: int = 43200
    admin_session_cookie_name: str = "ragdoc_admin_session"
    chat_session_cookie_name: str = "ragdoc_chat_session"
    ws_ticket_ttl_seconds: int = 60
    memory_ttl_seconds: int = 28800
    memory_message_limit: int = 12
    bootstrap_replay_ttl_seconds: int = 180
    provider_admin_token: str = ""
    user_hash_salt: str = ""
    admin_initial_username: str = "admin"
    admin_initial_display_name: str = "Amministratore"
    admin_initial_password: str = ""
    web_cookie_secure: bool = False
    web_chat_default_tenant_code: str = ""
    default_daily_message_limit: int = 500
    default_daily_token_limit: int = 500000
    default_burst_rps_limit: int = 5
    tenant_overlay_collection_prefix: str = "tenant_overlay_"
    overlay_score_boost: float = 0.05
    chat_ui_title: str = "ERP Copilot"
    chat_ui_csp: str = (
        "default-src 'self' 'unsafe-inline'; "
        "connect-src 'self' https: http: ws: wss:; "
        "img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
        "script-src 'self' 'unsafe-inline'"
    )

    @property
    def missing_required_env(self) -> list[str]:
        missing: list[str] = []
        if not self.openai_api_key:
            missing.append("OPENAI_API_KEY")
        if not self.qdrant_url:
            missing.append("QDRANT_URL")
        if not self.qdrant_collection:
            missing.append("QDRANT_COLLECTION")
        return missing

    @property
    def missing_security_env(self) -> list[str]:
        warnings: list[str] = []
        if not self.session_jwt_secret:
            warnings.append("SESSION_JWT_SECRET")
        if not self.user_hash_salt:
            warnings.append("USER_HASH_SALT")
        if not self.admin_initial_password:
            warnings.append("ADMIN_INITIAL_PASSWORD")
        return warnings


@lru_cache
def get_settings() -> Settings:
    knowledge_base_path = _resolve_project_path(os.getenv("KNOWLEDGE_BASE_PATH", "knowledge-base"))
    lexical_index_default = str(Path(knowledge_base_path) / ".artifacts" / "lexical_index.json")
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        qdrant_url=os.getenv("QDRANT_URL", ""),
        qdrant_collection=os.getenv("QDRANT_COLLECTION", "rag_doc_chunks"),
        embedding_model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        generation_model=os.getenv("GENERATION_MODEL", "gpt-4o-mini"),
        knowledge_base_path=knowledge_base_path,
        default_locale=os.getenv("DEFAULT_LOCALE", "it"),
        erp_version=os.getenv("ERP_VERSION", "REL231"),
        top_k=int(os.getenv("TOP_K", "5")),
        max_context_chars=int(os.getenv("MAX_CONTEXT_CHARS", "6000")),
        lexical_index_path=_resolve_project_path(
            os.getenv(
                "LEXICAL_INDEX_PATH",
                lexical_index_default,
            )
        ),
        dense_candidate_limit=int(os.getenv("DENSE_CANDIDATE_LIMIT", "20")),
        lexical_candidate_limit=int(os.getenv("LEXICAL_CANDIDATE_LIMIT", "20")),
        retrieval_min_score=float(os.getenv("RETRIEVAL_MIN_SCORE", "0.2")),
        retrieval_relative_score_floor=float(os.getenv("RETRIEVAL_RELATIVE_SCORE_FLOOR", "0.75")),
        redaction_allowlist=_parse_csv_env("REDACTION_ALLOWLIST"),
        redaction_denylist=_parse_csv_env("REDACTION_DENYLIST"),
        database_url=os.getenv("DATABASE_URL", "sqlite:///./.tmp/rag_doc_platform.db"),
        database_auto_create=os.getenv("DATABASE_AUTO_CREATE", "true").lower() in {"1", "true", "yes", "on"},
        redis_url=os.getenv("REDIS_URL", "memory://rag-doc"),
        redis_namespace=os.getenv("REDIS_NAMESPACE", "rag-doc"),
        bootstrap_jwt_audience=os.getenv("BOOTSTRAP_JWT_AUDIENCE", "rag-doc-bootstrap"),
        session_jwt_audience=os.getenv("SESSION_JWT_AUDIENCE", "rag-doc-api"),
        session_jwt_issuer=os.getenv("SESSION_JWT_ISSUER", "rag-doc-api"),
        session_jwt_algorithm=os.getenv("SESSION_JWT_ALGORITHM", "HS256"),
        session_jwt_secret=os.getenv("SESSION_JWT_SECRET", ""),
        session_ttl_seconds=int(os.getenv("SESSION_TTL_SECONDS", "900")),
        admin_session_jwt_audience=os.getenv("ADMIN_SESSION_JWT_AUDIENCE", "rag-doc-admin"),
        admin_session_jwt_issuer=os.getenv("ADMIN_SESSION_JWT_ISSUER", "rag-doc-admin"),
        admin_session_ttl_seconds=int(os.getenv("ADMIN_SESSION_TTL_SECONDS", "43200")),
        admin_session_cookie_name=os.getenv("ADMIN_SESSION_COOKIE_NAME", "ragdoc_admin_session"),
        chat_session_cookie_name=os.getenv("CHAT_SESSION_COOKIE_NAME", "ragdoc_chat_session"),
        ws_ticket_ttl_seconds=int(os.getenv("WS_TICKET_TTL_SECONDS", "60")),
        memory_ttl_seconds=int(os.getenv("MEMORY_TTL_SECONDS", "28800")),
        memory_message_limit=int(os.getenv("MEMORY_MESSAGE_LIMIT", "12")),
        bootstrap_replay_ttl_seconds=int(os.getenv("BOOTSTRAP_REPLAY_TTL_SECONDS", "180")),
        provider_admin_token=os.getenv("PROVIDER_ADMIN_TOKEN", ""),
        user_hash_salt=os.getenv("USER_HASH_SALT", ""),
        admin_initial_username=os.getenv("ADMIN_INITIAL_USERNAME", "admin"),
        admin_initial_display_name=os.getenv("ADMIN_INITIAL_DISPLAY_NAME", "Amministratore"),
        admin_initial_password=os.getenv("ADMIN_INITIAL_PASSWORD", ""),
        web_cookie_secure=os.getenv("WEB_COOKIE_SECURE", "false").lower() in {"1", "true", "yes", "on"},
        web_chat_default_tenant_code=os.getenv("WEB_CHAT_DEFAULT_TENANT_CODE", ""),
        default_daily_message_limit=int(os.getenv("DEFAULT_DAILY_MESSAGE_LIMIT", "500")),
        default_daily_token_limit=int(os.getenv("DEFAULT_DAILY_TOKEN_LIMIT", "500000")),
        default_burst_rps_limit=int(os.getenv("DEFAULT_BURST_RPS_LIMIT", "5")),
        tenant_overlay_collection_prefix=os.getenv("TENANT_OVERLAY_COLLECTION_PREFIX", "tenant_overlay_"),
        overlay_score_boost=float(os.getenv("OVERLAY_SCORE_BOOST", "0.05")),
        chat_ui_title=os.getenv("CHAT_UI_TITLE", "ERP Copilot"),
        chat_ui_csp=os.getenv(
            "CHAT_UI_CSP",
            (
                "default-src 'self' 'unsafe-inline'; "
                "connect-src 'self' https: http: ws: wss:; "
                "img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
                "script-src 'self' 'unsafe-inline'"
            ),
        ),
    )


settings = get_settings()
