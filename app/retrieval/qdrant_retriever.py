"""Qdrant-backed retrieval implementation."""

from __future__ import annotations

from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.exceptions import UnexpectedResponse
from qdrant_client.http.models import Filter

from app.core.config import Settings
from app.domain.schemas import QuerySource


class QdrantRetriever:
    def __init__(self, settings: Settings, collection_name: str | None = None) -> None:
        self.settings = settings
        self.collection_name = collection_name or settings.qdrant_collection
        self.client = QdrantClient(url=settings.qdrant_url)
        self.embeddings = OpenAIEmbeddings(
            model=settings.embedding_model,
            api_key=settings.openai_api_key,
        )
        self._vector_stores: dict[str, QdrantVectorStore] = {}

    def _get_vector_store(self, collection_name: str | None = None) -> QdrantVectorStore:
        active_collection = collection_name or self.collection_name
        store = self._vector_stores.get(active_collection)
        if store is None:
            store = QdrantVectorStore(
                client=self.client,
                collection_name=active_collection,
                embedding=self.embeddings,
            )
            self._vector_stores[active_collection] = store
        return store

    def search(
        self,
        query_text: str,
        limit: int,
        metadata_filter: Filter | None = None,
        score_threshold: float | None = None,
        collection_name: str | None = None,
    ) -> list[QuerySource]:
        active_collection = collection_name or self.collection_name
        try:
            matches = self._get_vector_store(active_collection).similarity_search_with_relevance_scores(
                query_text,
                k=limit,
                filter=metadata_filter,
                score_threshold=score_threshold,
            )
        except UnexpectedResponse as exc:
            status_code = getattr(exc, "status_code", None)
            if status_code == 404:
                return []
            raise
        sources: list[QuerySource] = []

        for document, score in matches:
            metadata = document.metadata or {}
            sources.append(
                QuerySource(
                    chunk_id=str(metadata.get("chunk_id", metadata.get("doc_id", ""))),
                    doc_id=str(metadata.get("doc_id", "")),
                    title=str(metadata.get("title", "")),
                    source=str(metadata.get("source", "")),
                    language=str(metadata.get("language", "")),
                    text=document.page_content,
                    score=float(score),
                    doc_type=str(metadata.get("doc_type", metadata.get("doc_kind", "overview"))),
                    doc_kind=str(metadata.get("doc_kind", metadata.get("doc_type", "overview"))),
                    kb_path=metadata.get("kb_path"),
                    domain=metadata.get("domain"),
                    feature=metadata.get("feature"),
                    module=metadata.get("module"),
                    submenu=metadata.get("submenu"),
                    screen_id=metadata.get("screen_id"),
                    screen_title=metadata.get("screen_title"),
                    tab_name=metadata.get("tab_name"),
                    section_title=metadata.get("section_title"),
                    heading_path=list(metadata.get("heading_path", [])),
                    chunk_kind=metadata.get("chunk_kind"),
                    step_start=metadata.get("step_start"),
                    step_end=metadata.get("step_end"),
                    task_tags=list(metadata.get("task_tags", [])),
                    keywords=list(metadata.get("keywords", [])),
                    aliases=list(metadata.get("aliases", [])),
                    error_codes=list(metadata.get("error_codes", [])),
                    role_scope=list(metadata.get("role_scope", [])),
                    erp_versions=list(metadata.get("erp_versions", [])),
                    review_status=str(metadata.get("review_status", "approved")),
                    source_uri=metadata.get("source_uri"),
                )
            )

        return sources
