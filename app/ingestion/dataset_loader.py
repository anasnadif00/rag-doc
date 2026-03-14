"""Dataset loading utilities for ingestion."""

from __future__ import annotations

from datasets import load_dataset

from app.core.config import Settings
from app.domain.schemas import SourceDocument


class DatasetLoader:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def load_documents(self, limit: int) -> list[SourceDocument]:
        dataset = self._load_dataset_split()
        max_rows = min(limit, len(dataset))
        documents: list[SourceDocument] = []

        for row in dataset.select(range(max_rows)):
            title = str(row.get("title", "")).strip()
            text = str(row.get("text", "")).strip()

            if not title or not text:
                continue

            documents.append(
                SourceDocument(
                    doc_id=self._build_doc_id(row),
                    title=title,
                    text=text,
                    source=self.settings.dataset_name,
                    language=self.settings.dataset_language,
                    category=None,
                )
            )

        return documents

    def _load_dataset_split(self):
        try:
            return load_dataset(
                self.settings.dataset_name,
                name=self.settings.dataset_language,
                split="train",
            )
        except Exception:
            try:
                return load_dataset(
                    self.settings.dataset_name,
                    split="train",
                )
            except Exception as fallback_error:
                raise RuntimeError(
                    "Failed to load dataset split using either the configured "
                    f"language '{self.settings.dataset_language}' or the default "
                    f"dataset configuration for '{self.settings.dataset_name}'."
                ) from fallback_error

    def _build_doc_id(self, row: dict) -> str:
        if "id" in row and row["id"] is not None:
            return str(row["id"])

        return str(row.get("title", "unknown-document")).strip().lower().replace(" ", "-")
