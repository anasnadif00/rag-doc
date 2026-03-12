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
    )


settings = get_settings()
