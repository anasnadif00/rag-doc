"""Service layer for grounded question answering."""

from __future__ import annotations

from app.core.config import Settings
from app.domain.schemas import QueryRequest, QueryResponse
from app.llm import AnswerGenerator
from app.retrieval import QdrantRetriever


class QueryService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._validate_settings()
        self.retriever = QdrantRetriever(settings=settings)
        self.generator = AnswerGenerator(settings=settings)

    def run(self, request: QueryRequest) -> QueryResponse:
        limit = request.top_k or self.settings.top_k
        sources = self.retriever.search(question=request.question, limit=limit)

        if not sources:
            return QueryResponse(
                question=request.question,
                answer="I could not find relevant context in the vector store for that question.",
                collection_name=self.settings.qdrant_collection,
                sources=[],
            )

        answer = self.generator.generate(question=request.question, sources=sources)
        return QueryResponse(
            question=request.question,
            answer=answer,
            collection_name=self.settings.qdrant_collection,
            sources=sources,
        )

    def _validate_settings(self) -> None:
        missing = self.settings.missing_required_env
        if missing:
            raise RuntimeError(
                "Missing required configuration: " + ", ".join(missing)
            )
