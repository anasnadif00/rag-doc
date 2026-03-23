"""Pydantic schemas used by the API and service layer."""

from pydantic import BaseModel, Field


class IngestRequest(BaseModel):
    limit: int = Field(default=10, ge=1, le=1000)
    recreate_collection: bool = False


class IngestResponse(BaseModel):
    status: str
    dataset_name: str
    dataset_language: str
    collection_name: str
    documents_loaded: int
    documents_processed: int
    chunks_created: int


class SourceDocument(BaseModel):
    doc_id: str
    title: str
    text: str
    source: str
    language: str
    category: str | None = None


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    top_k: int | None = Field(default=None, ge=1, le=20)


class QuerySource(BaseModel):
    doc_id: str
    title: str
    source: str
    language: str
    text: str
    score: float
    category: str | None = None


class QueryResponse(BaseModel):
    question: str
    answer: str
    collection_name: str
    sources: list[QuerySource]
