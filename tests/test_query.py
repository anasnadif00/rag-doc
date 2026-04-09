import json
from pathlib import Path
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from app.api.main import app
from app.core.config import Settings
from app.domain.schemas import (
    FieldContext,
    GeneratedAnswer,
    KnowledgeCitation,
    QueryPlan,
    QueryRequest,
    QueryResponse,
    QuerySource,
    RetrievalDiagnostics,
    RetrievalOptions,
    ScreenContext,
    ScreenContextSummary,
)
from app.ingestion.knowledge_loader import KnowledgeBaseLoader
from app.ingestion.markdown_chunker import MarkdownChunker
from app.retrieval.router import RetrievalRouter
from app.services.query_service import QueryService
from app.security.redaction import redact_screen_context

client = TestClient(app)


def make_settings(**overrides) -> Settings:
    base = Settings(
        openai_api_key="test-key",
        qdrant_url="http://localhost:6333",
        qdrant_collection="erp_copilot",
        embedding_model="text-embedding-3-small",
        generation_model="gpt-4o-mini",
        knowledge_base_path="knowledge-base",
        default_locale="it",
        erp_version="REL231",
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


def make_query_source(**overrides) -> QuerySource:
    payload = {
        "chunk_id": "fatture-how-to::procedura.steps-1-2",
        "doc_id": "contabilita/fatture/how_to/crea_fattura.md",
        "title": "Crea fattura",
        "source": "crea_fattura.md",
        "language": "it",
        "text": "1. Apri Fatture. 2. Compila Cliente e Data documento.",
        "score": 0.92,
        "doc_type": "how_to",
        "doc_kind": "how_to",
        "kb_path": "contabilita/fatture/how_to/crea_fattura.md",
        "domain": "contabilita",
        "feature": "fatture",
        "module": "Contabilita",
        "submenu": "Fatture",
        "screen_id": "FAT-001",
        "screen_title": "Fatture",
        "tab_name": "Testata",
        "section_title": "Procedura",
        "heading_path": ["Procedura"],
        "chunk_kind": "procedure",
        "step_start": 1,
        "step_end": 2,
        "task_tags": ["creazione fattura"],
        "keywords": ["fattura", "cliente"],
        "aliases": ["fatture clienti"],
        "error_codes": [],
        "role_scope": ["accounting"],
        "erp_versions": ["REL231"],
        "review_status": "approved",
        "source_uri": "contabilita/fatture/how_to/crea_fattura.md",
        "retrieval_reasons": ["match semantico su scope screen"],
    }
    payload.update(overrides)
    return QuerySource(**payload)


def make_query_request(**overrides) -> QueryRequest:
    payload = {
        "message": "Come creo una nuova fattura?",
        "conversation_id": "conv-1",
        "user_locale": "it",
        "screen_context": ScreenContext(
            application="ERP",
            module="Contabilita",
            submenu="Fatture",
            screen_id="FAT-001",
            screen_title="Fatture",
            tab_name="Testata",
            breadcrumb=["ERP", "Contabilita", "Fatture"],
            current_action="Creazione",
            error_messages=["Contatta mario.rossi@example.com per il dettaglio"],
            free_text_context="Sto creando una fattura per IBAN IT60X0542811101000000123456",
            fields=[
                FieldContext(label="Cliente", value="ACME"),
                FieldContext(label="IBAN cliente", value="IT60X0542811101000000123456"),
            ],
        ),
        "retrieval_options": RetrievalOptions(),
    }
    payload.update(overrides)
    return QueryRequest(**payload)


def make_query_plan(**overrides) -> QueryPlan:
    payload = {
        "intent_label": "how_to",
        "preferred_doc_kinds": ["how_to", "reference", "overview"],
        "semantic_query": "Come creo una nuova fattura? | Contabilita | Fatture | FAT-001",
        "lexical_query_terms": ["creo", "fattura", "contabilita", "fatture"],
        "hard_filters": {
            "review_status": ["approved"],
            "erp_versions": ["REL231"],
            "role_scope": ["accounting"],
            "doc_kinds": ["how_to", "reference", "overview"],
        },
        "soft_signals": {
            "module": ["Contabilita"],
            "submenu": ["Fatture"],
            "screen_id": ["FAT-001"],
            "screen_title": ["Fatture"],
            "tab_name": ["Testata"],
            "field_labels": ["Cliente"],
            "error_codes": [],
            "aliases": ["ERP", "Contabilita", "Fatture"],
        },
        "scope_order": ["screen", "module", "global"],
    }
    payload.update(overrides)
    return QueryPlan(**payload)


def write_lexical_index(path: Path, entries: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")


def test_query_endpoint_success():
    expected = QueryResponse(
        answer="Apri Fatture e compila Cliente e Data documento.",
        steps=["Apri Fatture", "Compila Cliente e Data documento"],
        citations=[
            KnowledgeCitation(
                chunk_id="fatture-how-to::procedura.steps-1-2",
                title="Crea fattura",
                section_title="Procedura",
                source_uri="contabilita/fatture/how_to/crea_fattura.md",
                doc_type="how_to",
                doc_kind="how_to",
                domain="contabilita",
                feature="fatture",
                module="Contabilita",
                screen_title="Fatture",
                tab_name="Testata",
                score=0.92,
            )
        ],
        follow_up_question=None,
        confidence=0.88,
        used_screen_context=ScreenContextSummary(
            application="ERP",
            module="Contabilita",
            submenu="Fatture",
            screen_id="FAT-001",
            screen_title="Fatture",
            tab_name="Testata",
            current_action="Creazione",
            breadcrumb=["ERP", "Contabilita", "Fatture"],
            error_messages=["Contatta mario.rossi@example.com per il dettaglio"],
            field_count=2,
            sensitive_field_count=1,
        ),
        redaction_notice="Alcuni valori sensibili della schermata sono stati mascherati prima di inviare il contesto al modello.",
        answer_mode="grounded",
        inference_notice=None,
    )

    with patch("app.api.routes.query.QueryService") as mock_service_class:
        mock_instance = mock_service_class.return_value
        mock_instance.run.return_value = expected

        response = client.post("/query", json=make_query_request().model_dump())

        assert response.status_code == 200
        data = response.json()
        assert data["answer"].startswith("Apri Fatture")
        assert data["citations"][0]["doc_kind"] == "how_to"
        assert data["answer_mode"] == "grounded"


def test_query_service_redacts_sensitive_fields_before_generation():
    settings = make_settings()
    source = make_query_source(role_scope=[])

    with patch("app.services.query_service.QdrantRetriever"), patch(
        "app.services.query_service.RetrievalRouter"
    ) as mock_router_class, patch("app.services.query_service.AnswerGenerator") as mock_generator_class:
        mock_router = mock_router_class.return_value
        mock_router.search.return_value = (make_query_plan(), [source])

        mock_generator = mock_generator_class.return_value
        mock_generator.generate.return_value = GeneratedAnswer(
            answer="Compila Cliente e Data documento.",
            steps=["Compila Cliente e Data documento"],
            confidence=0.9,
            answer_mode="grounded",
        )

        service = QueryService(settings=settings)
        response = service.run(make_query_request())

        generator_context = mock_generator.generate.call_args.kwargs["screen_context"]
        sensitive_field = next(field for field in generator_context.fields if "IBAN" in field.label)
        assert sensitive_field.value is None
        assert sensitive_field.masked_value is not None
        assert "@" not in generator_context.error_messages[0]
        assert "IT60X0542811101000000123456" not in (generator_context.free_text_context or "")
        assert response.redaction_notice is not None


def test_query_service_returns_partial_inference_when_generator_flags_it():
    settings = make_settings()
    source = make_query_source(score=0.24)

    with patch("app.services.query_service.QdrantRetriever"), patch(
        "app.services.query_service.RetrievalRouter"
    ) as mock_router_class, patch("app.services.query_service.AnswerGenerator") as mock_generator_class:
        mock_router_class.return_value.search.return_value = (make_query_plan(), [source])
        mock_generator_class.return_value.generate.return_value = GeneratedAnswer(
            answer="La procedura sembra richiedere la compilazione della testata prima del salvataggio.",
            steps=["Compila la testata"],
            confidence=0.4,
            answer_mode="partial_inference",
        )

        service = QueryService(settings=settings)
        response = service.run(make_query_request())

        assert response.answer_mode == "partial_inference"
        assert response.inference_notice is not None


def test_query_service_includes_retrieval_diagnostics_when_requested():
    settings = make_settings()
    source = make_query_source(role_scope=[])
    request = make_query_request(retrieval_options=RetrievalOptions(include_debug_info=True))

    with patch("app.services.query_service.QdrantRetriever"), patch(
        "app.services.query_service.RetrievalRouter"
    ) as mock_router_class, patch("app.services.query_service.AnswerGenerator") as mock_generator_class:
        mock_router = mock_router_class.return_value
        mock_router.search.return_value = (make_query_plan(), [source])
        mock_router.last_diagnostics = RetrievalDiagnostics(
            query_plan=make_query_plan(),
            active_filters=make_query_plan().hard_filters,
            semantic_query=make_query_plan().semantic_query,
            lexical_index_path="knowledge-base/.artifacts/lexical_index.json",
            candidate_count=1,
            returned_count=1,
            score_floor=0.2,
            returned_chunk_ids=[source.chunk_id],
            candidates=[],
        )
        mock_generator_class.return_value.generate.return_value = GeneratedAnswer(
            answer="Compila Cliente e Data documento.",
            steps=["Compila Cliente e Data documento"],
            confidence=0.9,
            answer_mode="grounded",
        )

        service = QueryService(settings=settings)
        response = service.run(request)

        assert response.retrieval_diagnostics is not None
        assert response.retrieval_diagnostics.returned_chunk_ids == [source.chunk_id]


def test_query_service_forces_clarification_when_inference_not_allowed():
    settings = make_settings()
    source = make_query_source(score=0.22)
    request = make_query_request(retrieval_options=RetrievalOptions(allow_inferred_guidance=False))

    with patch("app.services.query_service.QdrantRetriever"), patch(
        "app.services.query_service.RetrievalRouter"
    ) as mock_router_class, patch("app.services.query_service.AnswerGenerator") as mock_generator_class:
        mock_router_class.return_value.search.return_value = (make_query_plan(), [source])
        mock_generator_class.return_value.generate.return_value = GeneratedAnswer(
            answer="Potrebbe esserci una validazione sulla testata.",
            steps=["Controlla la testata"],
            confidence=0.35,
            answer_mode="partial_inference",
        )

        service = QueryService(settings=settings)
        response = service.run(request)

        assert response.answer_mode == "clarification"
        assert response.steps == []
        assert response.follow_up_question is not None


def test_retrieval_router_prefers_screen_how_to_over_global_doc(tmp_path: Path):
    lexical_path = tmp_path / ".artifacts" / "lexical_index.json"
    write_lexical_index(lexical_path, [])
    retriever = Mock()
    retriever.settings = make_settings(lexical_index_path=str(lexical_path))
    retriever.search.side_effect = [
        [make_query_source(chunk_id="screen", score=0.8, retrieval_reasons=[])],
        [],
        [make_query_source(chunk_id="global", score=0.75, screen_id=None, screen_title=None, tab_name=None, retrieval_reasons=[])],
    ]
    router = RetrievalRouter(settings=retriever.settings, retriever=retriever)

    _, results = router.search(request=make_query_request(), screen_context=make_query_request().screen_context)

    assert results[0].chunk_id == "screen"
    assert retriever.search.call_count == 3


def test_retrieval_router_applies_relative_score_cutoff(tmp_path: Path):
    lexical_path = tmp_path / ".artifacts" / "lexical_index.json"
    write_lexical_index(lexical_path, [])
    retriever = Mock()
    settings = make_settings(lexical_index_path=str(lexical_path))
    retriever.settings = settings
    retriever.search.side_effect = [
        [make_query_source(chunk_id="top", score=0.95, retrieval_reasons=[])],
        [],
        [make_query_source(chunk_id="tail", score=0.35, screen_id=None, screen_title=None, tab_name=None, retrieval_reasons=[])],
    ]
    router = RetrievalRouter(settings=settings, retriever=retriever)

    _, results = router.search(request=make_query_request(), screen_context=make_query_request().screen_context)

    assert [result.chunk_id for result in results] == ["top"]
    assert router.last_diagnostics is not None
    excluded = next(item for item in router.last_diagnostics.candidates if item.chunk_id == "tail")
    assert excluded.selected is False
    assert "below floor" in (excluded.selection_reason or "")


def test_retrieval_router_exact_error_code_prioritizes_troubleshooting(tmp_path: Path):
    lexical_path = tmp_path / ".artifacts" / "lexical_index.json"
    write_lexical_index(
        lexical_path,
        [
            make_query_source(
                chunk_id="ts",
                doc_type="troubleshooting",
                doc_kind="troubleshooting",
                text="Errore ART-VAL-001: verifica cliente e data documento.",
                error_codes=["ART-VAL-001"],
                retrieval_reasons=[],
            ).model_dump(),
            make_query_source(
                chunk_id="hw",
                screen_id=None,
                screen_title=None,
                tab_name=None,
                text="Guida generica alla creazione fattura.",
                retrieval_reasons=[],
            ).model_dump(),
        ],
    )
    settings = make_settings(lexical_index_path=str(lexical_path))
    retriever = Mock()
    retriever.settings = settings
    retriever.search.side_effect = [
        [],
        [],
        [make_query_source(chunk_id="hw", screen_id=None, screen_title=None, tab_name=None, score=0.2, retrieval_reasons=[])],
    ]
    router = RetrievalRouter(settings=settings, retriever=retriever)

    request = make_query_request(
        message="Ricevo errore ART-VAL-001 durante il salvataggio",
        screen_context=ScreenContext(
            module="Contabilita",
            submenu="Fatture",
            screen_id="FAT-001",
            screen_title="Fatture",
            error_messages=["Errore ART-VAL-001"],
            fields=[],
        ),
    )
    _, results = router.search(request=request, screen_context=request.screen_context)

    assert results[0].doc_kind == "troubleshooting"


def test_knowledge_base_loader_parses_valid_v2_markdown(tmp_path: Path):
    file_path = tmp_path / "contabilita" / "fatture" / "how_to" / "crea_fattura.md"
    file_path.parent.mkdir(parents=True)
    file_path.write_text(
        """---
title: Crea fattura
doc_kind: how_to
domain: contabilita
feature: fatture
keywords: [fattura, cliente]
task_tags: [creazione fattura]
erp_versions: [REL231]
role_scope: [accounting]
review_status: approved
module: Contabilita
submenu: Fatture
screen_id: FAT-001
screen_title: Fatture
tab_name: Testata
---
# Crea fattura
## Prerequisiti
Verifica il cliente.
## Procedura
1. Apri Fatture.
2. Compila Cliente e Data documento.
## Verifiche finali
Controlla il totale.
""",
        encoding="utf-8",
    )

    loader = KnowledgeBaseLoader(settings=make_settings(knowledge_base_path=str(tmp_path)))
    documents, errors, skipped = loader.load_documents_with_report()

    assert not errors
    assert skipped == 0
    assert len(documents) == 1
    assert documents[0].doc_kind == "how_to"
    assert documents[0].domain == "contabilita"


def test_knowledge_base_loader_accepts_hyphenated_how_to_paths_and_normalized_versions(tmp_path: Path):
    file_path = tmp_path / "commerciale" / "offerte" / "how-to" / "crea-ordine-da-offerta.md"
    file_path.parent.mkdir(parents=True)
    file_path.write_text(
        """---
title: Creare un ordine da un'offerta
doc_kind: how_to
domain: commerciale
feature: offerte
keywords: [crea ordine, ordine da offerta]
task_tags: [creazione ordine]
erp_versions: [v.1.0]
role_scope: [sales]
review_status: approved
module: Offerte
submenu: Navigazione offerta
screen_title: Crea Ordine
---
# Creare un ordine da un'offerta
## Procedura
1. Aprire l'offerta confermata.
2. Selezionare Crea Ordine.
""",
        encoding="utf-8",
    )

    loader = KnowledgeBaseLoader(settings=make_settings(knowledge_base_path=str(tmp_path), erp_version="v1.0"))
    documents, errors, skipped = loader.load_documents_with_report(erp_version="v1.0")

    assert not errors
    assert skipped == 0
    assert len(documents) == 1
    assert documents[0].doc_kind == "how_to"
    assert documents[0].source_uri == "commerciale/offerte/how-to/crea-ordine-da-offerta.md"


def test_knowledge_base_loader_rejects_path_yaml_mismatch(tmp_path: Path):
    file_path = tmp_path / "contabilita" / "fatture" / "how_to" / "crea_fattura.md"
    file_path.parent.mkdir(parents=True)
    file_path.write_text(
        """---
title: Crea fattura
doc_kind: troubleshooting
domain: contabilita
feature: fatture
keywords: [fattura]
task_tags: [creazione fattura]
erp_versions: [REL231]
role_scope: [accounting]
review_status: approved
---
# Crea fattura
## Procedura
1. Apri Fatture.
""",
        encoding="utf-8",
    )

    loader = KnowledgeBaseLoader(settings=make_settings(knowledge_base_path=str(tmp_path)))
    documents, errors, skipped = loader.load_documents_with_report()

    assert documents == []
    assert skipped == 1
    assert any("does not match" in error.message for error in errors)


def test_knowledge_base_loader_maps_legacy_doc_types(tmp_path: Path):
    file_path = tmp_path / "manuals" / "articoli.md"
    file_path.parent.mkdir(parents=True)
    file_path.write_text(
        """---
title: Articoli
doc_type: manual
keywords: [articolo]
task_tags: [creazione articolo]
erp_versions: [REL231]
role_scope: [warehouse]
review_status: approved
---
# Articoli
## Procedura
1. Apri Articoli.
""",
        encoding="utf-8",
    )

    loader = KnowledgeBaseLoader(settings=make_settings(knowledge_base_path=str(tmp_path)))
    documents = loader.load_documents(review_statuses=["approved"])

    assert len(documents) == 1
    assert documents[0].doc_kind == "how_to"


def test_knowledge_base_loader_skips_unapproved_documents(tmp_path: Path):
    file_path = tmp_path / "contabilita" / "fatture" / "how_to" / "bozza.md"
    file_path.parent.mkdir(parents=True)
    file_path.write_text(
        """---
title: Bozza
doc_kind: how_to
domain: contabilita
feature: fatture
keywords: [fattura]
task_tags: [creazione fattura]
erp_versions: [REL231]
role_scope: [accounting]
review_status: review
---
# Bozza
## Procedura
1. Apri Fatture.
""",
        encoding="utf-8",
    )

    loader = KnowledgeBaseLoader(settings=make_settings(knowledge_base_path=str(tmp_path)))
    documents, errors, skipped = loader.load_documents_with_report(review_statuses=["approved"])

    assert not errors
    assert documents == []
    assert skipped == 1


def test_markdown_chunker_preserves_how_to_step_ranges():
    document = make_query_source().model_dump()
    source_document = KnowledgeBaseLoader(settings=make_settings())._entry_to_documents(
        {
            "doc_id": "contabilita/fatture/how_to/crea_fattura.md",
            "title": "Crea fattura",
            "doc_kind": "how_to",
            "domain": "contabilita",
            "feature": "fatture",
            "module": "Contabilita",
            "submenu": "Fatture",
            "screen_id": "FAT-001",
            "screen_title": "Fatture",
            "tab_name": "Testata",
            "keywords": ["fattura"],
            "task_tags": ["creazione fattura"],
            "erp_versions": ["REL231"],
            "role_scope": ["accounting"],
            "review_status": "approved",
            "text": "# Crea fattura\n## Procedura\n1. Apri Fatture.\n2. Compila Cliente.\n3. Salva.",
        },
        Path("knowledge-base/contabilita/fatture/how_to/crea_fattura.json"),
        0,
    )[0]

    chunker = MarkdownChunker()
    chunks = chunker.chunk_document(source_document, ingested_at="2026-03-24T00:00:00Z")

    procedure_chunk = next(chunk for chunk in chunks if chunk.chunk_kind == "procedure")
    assert procedure_chunk.step_start == 1
    assert procedure_chunk.step_end == 3


def test_retrieval_router_matches_normalized_erp_versions(tmp_path: Path):
    lexical_path = tmp_path / ".artifacts" / "lexical_index.json"
    write_lexical_index(lexical_path, [])
    settings = make_settings(lexical_index_path=str(lexical_path), erp_version="v1.0")
    retriever = Mock()
    retriever.settings = settings
    retriever.search.side_effect = [
        [
            make_query_source(
                chunk_id="ordine-da-offerta",
                title="Creare un ordine da un'offerta",
                source="crea-ordine-da-offerta.md",
                source_uri="commerciale/offerte/how-to/crea-ordine-da-offerta.md",
                domain="commerciale",
                feature="offerte",
                module="Offerte",
                submenu="Navigazione offerta",
                screen_id=None,
                screen_title="Crea Ordine",
                tab_name=None,
                erp_versions=["v.1.0"],
                retrieval_reasons=[],
                score=0.82,
            )
        ],
        [],
        [],
    ]
    router = RetrievalRouter(settings=settings, retriever=retriever)
    request = make_query_request(
        message="Come si crea un ordine cliente da offerta cliente",
        screen_context=ScreenContext(),
    )

    _, results = router.search(request=request, screen_context=request.screen_context)

    assert [result.chunk_id for result in results] == ["ordine-da-offerta"]


def test_redaction_masks_free_text_and_error_messages():
    result = redact_screen_context(
        make_query_request().screen_context,
        denylist=("iban", "email"),
    )

    assert "@" not in result.screen_context.error_messages[0]
    assert "IT60X0542811101000000123456" not in (result.screen_context.free_text_context or "")
    assert "free_text_context" in result.redacted_fields
