import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from app.api.main import app
from app.domain.schemas import IngestResponse

# The TestClient bypasses the network layer and hooks directly into the FastAPI ASGI app!
client = TestClient(app)

def test_ingest_endpoint_success():
    """Test the POST /ingest endpoint without actually invoking heavy processing."""
    
    # We patch the IngestService inside the route so it doesn't trigger the real Heavy AI operations
    with patch("app.api.routes.ingest.IngestService") as MockService:
        
        # Fake the response that the service would typically return
        mock_instance = MockService.return_value
        mock_instance.run.return_value = IngestResponse(
            status="success",
            dataset_name="mock_dataset",
            dataset_language="en",
            collection_name="mock_collection",
            documents_loaded=5,
            documents_processed=5,
            chunks_created=15
        )
        
        # Dispatch the HTTP payload locally through TestClient
        payload = {"limit": 5, "recreate_collection": True}
        response = client.post("/ingest", json=payload)
        
        # Make assertions!
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "success"
        assert data["documents_loaded"] == 5
        assert data["chunks_created"] == 15
        
        # Verify our mock intercepted the logic properly
        MockService.assert_called_once()
        mock_instance.run.assert_called_once()
