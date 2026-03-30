"""Query routes."""

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.domain.schemas import QueryRequest, QueryResponse
from app.services.query_service import QueryService

router = APIRouter(tags=["query"])

@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest) -> QueryResponse:
    """Retrieve relevant chunks and generate a grounded answer."""
    try:
        service = QueryService(settings=settings)
        return service.run(request)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc