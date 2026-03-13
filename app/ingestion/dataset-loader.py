"""Dataset loading utilities for ingestion."""

from datasets import load_dataset

from app.core.config import Settings
from app.domain.schemas import SourceDocument


class DatasetLoader:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def load_documents(self, limit: int) -> list[SourceDocument]:
        dataset = load_dataset(
            self.settings.dataset_name,
            name=self.settings.dataset_language,
            split="train",
        )

        documents: list[SourceDocument] = []

        for row in dataset.select(range(limit)):
            title = row.get("title", "").strip()
            text = row.get("text", "").strip()

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

    def _build_doc_id(self, row: dict) -> str:
        if "id" in row and row["id"] is not None:
            return str(row["id"])

        return row.get("title", "unknown-document").strip().lower().replace(" ", "-")