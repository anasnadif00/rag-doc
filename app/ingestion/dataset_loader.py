"""Backward-compatible alias to the ERP knowledge-base loader."""

from app.ingestion.knowledge_loader import KnowledgeBaseLoader as DatasetLoader

__all__ = ["DatasetLoader"]
