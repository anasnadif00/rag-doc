"""Database-backed overrides for settings that can change while the API is running."""

from __future__ import annotations

from dataclasses import replace

from sqlalchemy.orm import Session

from app.core.config import Settings
from app.persistence.repositories import ModelConfigurationRepository


def get_runtime_settings(session: Session, base_settings: Settings) -> Settings:
    """Return immutable settings with the persisted model selection applied."""
    configuration = ModelConfigurationRepository(session).get()
    if configuration is None:
        return base_settings
    return replace(
        base_settings,
        generation_model=configuration.generation_model,
        rerank_model=configuration.rerank_model,
    )
