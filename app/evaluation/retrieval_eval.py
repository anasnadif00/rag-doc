"""Utilities for deterministic retrieval evaluation over curated KB fixtures."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from app.core.config import Settings
from app.domain.schemas import DocType, QueryRequest, RetrievalOptions, ScreenContext
from app.ingestion.knowledge_loader import KnowledgeBaseLoader
from app.ingestion.markdown_chunker import MarkdownChunker
from app.retrieval.router import RetrievalRouter


class RetrievalEvalCase(BaseModel):
    case_id: str = Field(alias="id")
    message: str
    user_locale: str = "it"
    screen_context: ScreenContext = Field(default_factory=ScreenContext)
    retrieval_options: RetrievalOptions = Field(default_factory=RetrievalOptions)
    expected_source_uri: str
    expected_doc_kind: DocType | None = None


class RetrievalEvalResult(BaseModel):
    case_id: str
    expected_source_uri: str
    expected_doc_kind: DocType | None = None
    top_source_uri: str | None = None
    top_doc_kind: DocType | None = None
    matched_top1: bool
    matched_in_top_k: bool
    returned_chunk_ids: list[str] = Field(default_factory=list)
    returned_source_uris: list[str] = Field(default_factory=list)


class EmptyDenseRetriever:
    def search(self, *args: Any, **kwargs: Any) -> list[Any]:
        return []


def clone_settings(settings: Settings, **overrides: Any) -> Settings:
    return Settings(**(settings.__dict__ | overrides))


def build_lexical_index(settings: Settings) -> int:
    loader = KnowledgeBaseLoader(settings=settings)
    documents = loader.load_documents(
        review_statuses=["approved"],
        erp_version=settings.erp_version,
    )
    chunker = MarkdownChunker()
    chunk_records = chunker.chunk_documents(
        documents,
        ingested_at=datetime.now(timezone.utc).isoformat(),
    )
    index_path = Path(settings.lexical_index_path)
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps([chunk.model_dump() for chunk in chunk_records], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return len(chunk_records)


def load_eval_cases(cases_path: str | Path) -> list[RetrievalEvalCase]:
    payload = json.loads(Path(cases_path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("Evaluation cases must be a JSON array.")
    return [RetrievalEvalCase.model_validate(item) for item in payload]


def run_retrieval_eval(
    settings: Settings,
    cases_path: str | Path,
    top_k: int | None = None,
) -> dict[str, Any]:
    cases = load_eval_cases(cases_path)
    router = RetrievalRouter(settings=settings, retriever=EmptyDenseRetriever())  # type: ignore[arg-type]

    results: list[RetrievalEvalResult] = []
    top1_hits = 0
    hit_at_k = 0
    for case in cases:
        retrieval_options = case.retrieval_options
        if top_k is not None and retrieval_options.top_k is None:
            retrieval_options = retrieval_options.model_copy(update={"top_k": top_k})

        request = QueryRequest(
            message=case.message,
            user_locale=case.user_locale,
            screen_context=case.screen_context,
            retrieval_options=retrieval_options,
        )
        _, sources = router.search(request=request, screen_context=request.screen_context)

        returned_source_uris = [source.source_uri for source in sources if source.source_uri]
        top_source_uri = returned_source_uris[0] if returned_source_uris else None
        top_doc_kind = sources[0].doc_kind if sources else None
        matched_top1 = top_source_uri == case.expected_source_uri
        matched_in_top_k = case.expected_source_uri in returned_source_uris

        if matched_top1:
            top1_hits += 1
        if matched_in_top_k:
            hit_at_k += 1

        results.append(
            RetrievalEvalResult(
                case_id=case.case_id,
                expected_source_uri=case.expected_source_uri,
                expected_doc_kind=case.expected_doc_kind,
                top_source_uri=top_source_uri,
                top_doc_kind=top_doc_kind,
                matched_top1=matched_top1,
                matched_in_top_k=matched_in_top_k,
                returned_chunk_ids=[source.chunk_id for source in sources],
                returned_source_uris=returned_source_uris,
            )
        )

    return {
        "total_cases": len(cases),
        "top1_hits": top1_hits,
        "hit_at_k": hit_at_k,
        "top1_accuracy": round(top1_hits / len(cases), 4) if cases else 0.0,
        "hit_at_k_accuracy": round(hit_at_k / len(cases), 4) if cases else 0.0,
        "results": [result.model_dump() for result in results],
    }
