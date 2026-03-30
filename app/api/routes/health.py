"""Health check routes."""

from pathlib import Path

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, object]:
    """Return basic service health and missing required environment variables."""
    knowledge_base_path = Path(settings.knowledge_base_path)
    lexical_index_path = Path(settings.lexical_index_path)
    return {
        "status": "ok",
        "service": "rag-doc",
        "erp_version": settings.erp_version,
        "knowledge_base_path": settings.knowledge_base_path,
        "knowledge_base_exists": knowledge_base_path.exists(),
        "lexical_index_path": settings.lexical_index_path,
        "lexical_index_exists": lexical_index_path.exists(),
        "missing_env": settings.missing_required_env,
    }
