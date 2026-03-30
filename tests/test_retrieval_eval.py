from pathlib import Path

from app.context.normalizer import tokenize_search_text
from app.core.config import Settings
from app.evaluation import build_lexical_index, run_retrieval_eval


def make_settings(**overrides) -> Settings:
    base = Settings(
        openai_api_key="test-key",
        qdrant_url="http://localhost:6333",
        qdrant_collection="erp_copilot",
        embedding_model="text-embedding-3-small",
        generation_model="gpt-4o-mini",
        knowledge_base_path="knowledge-base",
        default_locale="it",
        erp_version="v1.0",
        top_k=5,
        max_context_chars=6000,
        lexical_index_path="knowledge-base/.artifacts/lexical_index.json",
        dense_candidate_limit=20,
        lexical_candidate_limit=20,
        retrieval_min_score=0.2,
        retrieval_relative_score_floor=0.75,
        redaction_allowlist=(),
        redaction_denylist=("iban", "email"),
    )
    return Settings(**(base.__dict__ | overrides))


def test_tokenize_search_text_handles_apostrophes_accents_and_stems():
    tokens = tokenize_search_text("Cos'è il controllo dei movimenti in contabilita?")

    assert "il" not in tokens
    assert "contabilita" in tokens
    assert "contabilit" in tokens
    assert "movimenti" in tokens
    assert "moviment" in tokens


def test_curated_retrieval_eval_cases_match_expected_sources(tmp_path: Path):
    repo_root = Path(__file__).resolve().parents[1]
    knowledge_base_path = repo_root / "evals" / "fixtures" / "knowledge_base"
    cases_path = repo_root / "evals" / "retrieval_cases.json"
    lexical_index_path = tmp_path / ".artifacts" / "lexical_index.json"
    settings = make_settings(
        knowledge_base_path=str(knowledge_base_path),
        lexical_index_path=str(lexical_index_path),
    )

    chunks_created = build_lexical_index(settings)
    summary = run_retrieval_eval(settings=settings, cases_path=cases_path, top_k=5)

    assert chunks_created > 0
    assert summary["top1_hits"] == summary["total_cases"]
    assert summary["hit_at_k"] == summary["total_cases"]
