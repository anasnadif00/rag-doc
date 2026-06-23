"""Query routes."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import Settings, get_settings
from app.core.runtime_config import get_runtime_settings
from app.domain.schemas import QueryRequest, QueryResponse
from app.persistence.db import get_db_session
from app.services.query_service import QueryService

router = APIRouter(tags=["query"])

@router.post("/query", response_model=QueryResponse)
def query(
    request: QueryRequest,
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
) -> QueryResponse:
    """Retrieve relevant chunks and generate a grounded answer."""
    try:
        service = QueryService(settings=get_runtime_settings(session, settings))
        return service.run(request)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
