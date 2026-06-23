import json
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from app.api.main import app
from app.domain.schemas import IngestRequest, IngestResponse
from app.services.ingest_service import IngestService

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


def test_recreate_empty_knowledge_base_removes_collection_and_clears_lexical_index(tmp_path):
    lexical_index_path = tmp_path / ".artifacts" / "lexical_index.json"
    lexical_index_path.parent.mkdir(parents=True)
    lexical_index_path.write_text('[{"chunk_id":"stale"}]', encoding="utf-8")

    service = IngestService.__new__(IngestService)
    service.settings = Mock(
        knowledge_base_path=str(tmp_path),
        qdrant_url="http://localhost:6333",
        qdrant_collection="mock_collection",
        lexical_index_path=str(lexical_index_path),
        erp_version="REL231",
    )
    service.knowledge_loader = Mock()
    service.knowledge_loader.load_documents_with_report.return_value = ([], [], 0)

    with patch("app.services.ingest_service.QdrantClient") as qdrant_client_class:
        response = service.run(IngestRequest(recreate_collection=True, rebuild_lexical_index=True))

    qdrant_client_class.return_value.delete_collection.assert_called_once_with(
        collection_name="mock_collection"
    )
    assert json.loads(lexical_index_path.read_text(encoding="utf-8")) == []
    assert response.documents_processed == 0
    assert response.chunks_created == 0
