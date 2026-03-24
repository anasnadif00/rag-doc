"""Configuration loading for the ERP copilot application."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


def _parse_csv_env(name: str) -> tuple[str, ...]:
    value = os.getenv(name, "")
    if not value:
        return ()
    return tuple(item.strip() for item in value.split(",") if item.strip())


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
    redaction_allowlist: tuple[str, ...]
    redaction_denylist: tuple[str, ...]

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


@lru_cache
def get_settings() -> Settings:
    knowledge_base_path = os.getenv("KNOWLEDGE_BASE_PATH", "knowledge-base")
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
        lexical_index_path=os.getenv(
            "LEXICAL_INDEX_PATH",
            os.path.join(knowledge_base_path, ".artifacts", "lexical_index.json"),
        ),
        dense_candidate_limit=int(os.getenv("DENSE_CANDIDATE_LIMIT", "20")),
        lexical_candidate_limit=int(os.getenv("LEXICAL_CANDIDATE_LIMIT", "20")),
        redaction_allowlist=_parse_csv_env("REDACTION_ALLOWLIST"),
        redaction_denylist=_parse_csv_env("REDACTION_DENYLIST"),
    )


settings = get_settings()
