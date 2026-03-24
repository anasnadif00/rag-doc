from fastapi.testclient import TestClient
from unittest.mock import patch

from app.api.main import app
from app.domain.schemas import IngestResponse

client = TestClient(app)


def test_ingest_endpoint_success():
    with patch("app.api.routes.ingest.IngestService") as mock_service_class:
        mock_instance = mock_service_class.return_value
        mock_instance.run.return_value = IngestResponse(
            status="success",
            knowledge_base_path="knowledge-base",
            collection_name="mock_collection",
            erp_version="REL231",
            documents_loaded=5,
            documents_processed=5,
            documents_skipped=1,
            chunks_created=15,
            validation_errors_count=0,
            doc_types=["how_to", "troubleshooting"],
            doc_kinds=["how_to", "troubleshooting"],
        )

        payload = {"limit": 5, "recreate_collection": True, "review_statuses": ["approved"]}
        response = client.post("/ingest", json=payload)

        assert response.status_code == 200

        data = response.json()
        assert data["status"] == "success"
        assert data["documents_loaded"] == 5
        assert data["chunks_created"] == 15
        assert data["erp_version"] == "REL231"
        assert data["documents_skipped"] == 1
        assert data["doc_types"] == ["how_to", "troubleshooting"]
        assert data["doc_kinds"] == ["how_to", "troubleshooting"]

        mock_service_class.assert_called_once()
        mock_instance.run.assert_called_once()
