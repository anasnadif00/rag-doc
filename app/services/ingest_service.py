"""Service layer for ERP knowledge-base ingestion."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from langchain_qdrant import QdrantVectorStore
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.http.models import PayloadSchemaType

from app.core.config import Settings
from app.domain.schemas import ChunkRecord, IngestRequest, IngestResponse
from app.ingestion.knowledge_loader import KnowledgeBaseLoader
from app.ingestion.markdown_chunker import MarkdownChunker


class IngestService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.knowledge_loader = KnowledgeBaseLoader(settings=settings)
        self.chunker = MarkdownChunker()
        self.embeddings = OpenAIEmbeddings(
            model=self.settings.embedding_model,
            api_key=self.settings.openai_api_key,
        )

    def run(self, request: IngestRequest) -> IngestResponse:
        source_documents, validation_errors, skipped_documents = self.knowledge_loader.load_documents_with_report(
            limit=request.limit,
            doc_types=request.doc_types,
            erp_version=request.erp_version,
            review_statuses=request.review_statuses,
        )

        if request.strict_validation and validation_errors:
            raise RuntimeError(
                "KB validation failed: " + "; ".join(error.message for error in validation_errors[:5])
            )

        if not source_documents:
            return IngestResponse(
                status="success",
                knowledge_base_path=self.settings.knowledge_base_path,
                collection_name=self.settings.qdrant_collection,
                erp_version=request.erp_version or self.settings.erp_version,
                documents_loaded=skipped_documents,
                documents_processed=0,
                documents_skipped=skipped_documents,
                chunks_created=0,
                validation_errors_count=len(validation_errors),
                doc_types=sorted(set(request.doc_types or [])),
                doc_kinds=sorted(set(request.doc_types or [])),
            )

        ingested_at = datetime.now(timezone.utc).isoformat()
        chunk_records = self.chunker.chunk_documents(source_documents, ingested_at=ingested_at)
        langchain_documents = self._to_langchain_documents(chunk_records)
        QdrantVectorStore.from_documents(
            langchain_documents,
            self.embeddings,
            url=self.settings.qdrant_url,
            collection_name=self.settings.qdrant_collection,
            force_recreate=request.recreate_collection,
        )
        self._create_payload_indexes()
        if request.rebuild_lexical_index:
            self._write_lexical_index(chunk_records)

        doc_kinds = sorted({document.doc_kind for document in source_documents if document.doc_kind})
        return IngestResponse(
            status="success",
            knowledge_base_path=self.settings.knowledge_base_path,
            collection_name=self.settings.qdrant_collection,
            erp_version=request.erp_version or self.settings.erp_version,
            documents_loaded=len(source_documents) + skipped_documents,
            documents_processed=len(source_documents),
            documents_skipped=skipped_documents,
            chunks_created=len(chunk_records),
            validation_errors_count=len(validation_errors),
            doc_types=doc_kinds,
            doc_kinds=doc_kinds,
        )

    def _to_langchain_documents(self, chunks: list[ChunkRecord]) -> list[Document]:
        documents: list[Document] = []
        for chunk in chunks:
            documents.append(
                Document(
                    page_content=chunk.text,
                    metadata=chunk.model_dump(exclude={"text"}),
                )
            )
        return documents

    def _write_lexical_index(self, chunks: list[ChunkRecord]) -> None:
        index_path = Path(self.settings.lexical_index_path)
        index_path.parent.mkdir(parents=True, exist_ok=True)
        serialized = [chunk.model_dump() for chunk in chunks]
        index_path.write_text(json.dumps(serialized, ensure_ascii=False, indent=2), encoding="utf-8")

    def _create_payload_indexes(self) -> None:
        client = QdrantClient(url=self.settings.qdrant_url)
        fields = (
            "metadata.doc_kind",
            "metadata.domain",
            "metadata.feature",
            "metadata.screen_id",
            "metadata.screen_title",
            "metadata.tab_name",
            "metadata.role_scope",
            "metadata.erp_versions",
            "metadata.review_status",
            "metadata.error_codes",
        )
        for field_name in fields:
            try:
                client.create_payload_index(
                    collection_name=self.settings.qdrant_collection,
                    field_name=field_name,
                    field_schema=PayloadSchemaType.KEYWORD,
                )
            except Exception:
                continue
