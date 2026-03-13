"""Service layer for dataset ingestion."""

from app.core.config import Settings
from app.domain.schemas import IngestRequest, IngestResponse


class IngestService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def run(self, request: IngestRequest) -> IngestResponse:
        raise NotImplementedError("Ingestion pipeline is not implemented yet.")
