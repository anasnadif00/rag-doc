from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

import app.core.config as config
from app.api.main import app
from app.core.config import Settings

client = TestClient(app)


def make_settings(**overrides) -> Settings:
    base = Settings(
        openai_api_key="test-key",
        qdrant_url="http://localhost:6333",
        qdrant_collection="erp_copilot",
        embedding_model="text-embedding-3-small",
        generation_model="gpt-4o-mini",
        knowledge_base_path=str(Path("knowledge-base").resolve()),
        default_locale="it",
        erp_version="REL231",
        top_k=5,
        max_context_chars=6000,
        lexical_index_path=str((Path("knowledge-base") / ".artifacts" / "lexical_index.json").resolve()),
        dense_candidate_limit=20,
        lexical_candidate_limit=20,
        redaction_allowlist=(),
        redaction_denylist=("iban", "email"),
    )
    return Settings(**(base.__dict__ | overrides))


def test_get_settings_resolves_relative_paths_from_project_root(monkeypatch, tmp_path: Path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("KNOWLEDGE_BASE_PATH", "mock_knowledge_base")
    monkeypatch.delenv("LEXICAL_INDEX_PATH", raising=False)
    config.get_settings.cache_clear()

    settings = config.get_settings()
    project_root = Path(config.__file__).resolve().parents[2]

    assert settings.knowledge_base_path == str((project_root / "mock_knowledge_base").resolve())
    assert settings.lexical_index_path == str(
        (project_root / "mock_knowledge_base" / ".artifacts" / "lexical_index.json").resolve()
    )

    config.get_settings.cache_clear()


def test_health_endpoint_reports_path_diagnostics(tmp_path: Path):
    knowledge_base_path = tmp_path / "kb"
    knowledge_base_path.mkdir()
    lexical_index_path = knowledge_base_path / ".artifacts" / "lexical_index.json"
    lexical_index_path.parent.mkdir(parents=True)
    lexical_index_path.write_text("[]", encoding="utf-8")

    with patch(
        "app.api.routes.health.settings",
        make_settings(
            knowledge_base_path=str(knowledge_base_path),
            lexical_index_path=str(lexical_index_path),
        ),
    ):
        response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["knowledge_base_path"] == str(knowledge_base_path)
    assert data["knowledge_base_exists"] is True
    assert data["lexical_index_path"] == str(lexical_index_path)
    assert data["lexical_index_exists"] is True
