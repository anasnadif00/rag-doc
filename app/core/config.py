"""Configuration loading for the application."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    qdrant_url: str
    qdrant_collection: str
    embedding_model: str
    dataset_name: str
    dataset_language: str
    top_k: int

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
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        qdrant_url=os.getenv("QDRANT_URL", ""),
        qdrant_collection=os.getenv("QDRANT_COLLECTION", "rag_doc_chunks"),
        embedding_model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        dataset_name=os.getenv("DATASET_NAME", "wikimedia/wikipedia"),
        dataset_language=os.getenv("DATASET_LANGUAGE", "en"),
        top_k=int(os.getenv("TOP_K", "5")),
    )


settings = get_settings()
