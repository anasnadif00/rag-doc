"""Qdrant-backed retrieval implementation."""

from __future__ import annotations

from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient

from app.core.config import Settings
from app.domain.schemas import QuerySource


class QdrantRetriever:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = QdrantClient(url=settings.qdrant_url)
        self.embeddings = OpenAIEmbeddings(
            model=settings.embedding_model,
            api_key=settings.openai_api_key,
        )
        self.vector_store = Qdrant(
            client=self.client,
            collection_name=settings.qdrant_collection,
            embeddings=self.embeddings,
        )

    def search(self, question: str, limit: int) -> list[QuerySource]:
        matches = self.vector_store.similarity_search_with_score(question, k=limit)
        sources: list[QuerySource] = []

        for document, score in matches:
            metadata = document.metadata or {}
            sources.append(
                QuerySource(
                    doc_id=str(metadata.get("doc_id", "")),
                    title=str(metadata.get("title", "")),
                    source=str(metadata.get("source", "")),
                    language=str(metadata.get("language", "")),
                    category=metadata.get("category"),
                    text=document.page_content,
                    score=float(score),
                )
            )

        return sources
