"""Ingestion routes."""

from fastapi import APIRouter

from app.core.config import settings
from app.domain.schemas import IngestRequest, IngestResponse
from app.services.ingest_service import IngestService

router = APIRouter(tags=["ingest"])


@router.post("/ingest", response_model=IngestResponse)
def ingest(request: IngestRequest) -> IngestResponse:
    """Trigger the dataset ingestion pipeline."""
    service = IngestService(settings=settings)
    return service.run(request)
