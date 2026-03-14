"""Service layer for dataset ingestion."""

from app.core.config import Settings
from app.domain.schemas import IngestRequest, IngestResponse
from app.ingestion.dataset_loader import DatasetLoader


class IngestService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.dataset_loader = DatasetLoader(settings=settings)

    def run(self, request: IngestRequest) -> IngestResponse:
        documents = self.dataset_loader.load_documents(limit=request.limit)

        return IngestResponse(
            status="success",
            dataset_name=self.settings.dataset_name,
            dataset_language=self.settings.dataset_language,
            collection_name=self.settings.qdrant_collection,
            documents_loaded=len(documents),
            documents_processed=0,
            chunks_created=0,
        )
