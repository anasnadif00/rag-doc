"""Pydantic schemas used by the ERP copilot API and service layer."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, model_validator

DocType = Literal["how_to", "troubleshooting", "reference", "faq", "overview"]
ReviewStatus = Literal["draft", "review", "approved", "deprecated"]
AnswerMode = Literal["grounded", "partial_inference", "clarification"]
IntentLabel = Literal["how_to", "troubleshooting", "reference", "navigation", "general"]
SearchScope = Literal["auto", "screen", "module", "global"]
ResolvedSearchScope = Literal["screen", "module", "global"]


class IngestRequest(BaseModel):
    limit: int | None = Field(default=None, ge=1, le=5000)
    recreate_collection: bool = False
    doc_types: list[DocType] | None = None
    erp_version: str | None = None
    review_statuses: list[ReviewStatus] = Field(default_factory=lambda: ["approved"])
    strict_validation: bool = False
    rebuild_lexical_index: bool = True


class IngestResponse(BaseModel):
    status: str
    knowledge_base_path: str
    collection_name: str
    erp_version: str
    documents_loaded: int
    documents_processed: int
    documents_skipped: int
    chunks_created: int
    validation_errors_count: int
    doc_types: list[DocType]
    doc_kinds: list[DocType]


class SourceDocument(BaseModel):
    doc_id: str
    title: str
    text: str
    source: str
    language: str
    doc_type: DocType | None = None
    doc_kind: DocType | None = None
    kb_path: str | None = None
    domain: str | None = None
    feature: str | None = None
    module: str | None = None
    submenu: str | None = None
    screen_id: str | None = None
    screen_title: str | None = None
    tab_name: str | None = None
    section_title: str | None = None
    heading_path: list[str] = Field(default_factory=list)
    chunk_kind: str | None = None
    step_start: int | None = None
    step_end: int | None = None
    field_labels: list[str] = Field(default_factory=list)
    task_tags: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    aliases: list[str] = Field(default_factory=list)
    error_codes: list[str] = Field(default_factory=list)
    role_scope: list[str] = Field(default_factory=list)
    erp_version: str | None = None
    erp_versions: list[str] = Field(default_factory=list)
    review_status: ReviewStatus = "approved"
    source_uri: str | None = None
    source_transcript_id: str | None = None
    source_audio_uri: str | None = None

    @model_validator(mode="after")
    def _sync_metadata(self) -> "SourceDocument":
        kind = self.doc_kind or self.doc_type or "overview"
        self.doc_kind = kind
        self.doc_type = kind
        if not self.erp_versions and self.erp_version:
            self.erp_versions = [self.erp_version]
        if not self.erp_version and self.erp_versions:
            self.erp_version = self.erp_versions[0]
        return self


class FieldContext(BaseModel):
    field_id: str | None = None
    label: str
    value: str | None = None
    masked_value: str | None = None
    is_sensitive: bool = False
    is_required: bool = False
    is_editable: bool = True
    validation_error: str | None = None


class RecordContext(BaseModel):
    record_id: str | None = None
    primary_label: str | None = None
    values: dict[str, str | int | float | bool | None] = Field(default_factory=dict)


class TableContext(BaseModel):
    table_id: str | None = None
    title: str | None = None
    visible_columns: list[str] = Field(default_factory=list)
    selected_row_index: int | None = None
    row_count: int | None = None


class ScreenContext(BaseModel):
    application: str | None = None
    module: str | None = None
    submenu: str | None = None
    screen_id: str | None = None
    screen_title: str | None = None
    tab_name: str | None = None
    breadcrumb: list[str] = Field(default_factory=list)
    current_action: str | None = None
    error_messages: list[str] = Field(default_factory=list)
    free_text_context: str | None = None
    fields: list[FieldContext] = Field(default_factory=list)
    selected_record: RecordContext | None = None
    table_context: TableContext | None = None


class UserContext(BaseModel):
    username: str | None = None
    roles: list[str] = Field(default_factory=list)
    company_code: str | None = None
    division: str | None = None


class RetrievalOptions(BaseModel):
    top_k: int | None = Field(default=None, ge=1, le=20)
    doc_types: list[DocType] = Field(default_factory=list)
    role_scope: list[str] = Field(default_factory=list)
    search_scope: SearchScope = "auto"
    score_threshold: float | None = None
    allow_inferred_guidance: bool = True
    include_debug_info: bool = False


class TaskIntent(BaseModel):
    label: str
    search_terms: list[str] = Field(default_factory=list)
    hints: list[str] = Field(default_factory=list)


class QueryRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    conversation_id: str | None = None
    user_locale: str = Field(default="it", min_length=2, max_length=10)
    screen_context: ScreenContext
    user_context: UserContext | None = None
    retrieval_options: RetrievalOptions | None = None


class QuerySource(BaseModel):
    chunk_id: str
    doc_id: str
    title: str
    source: str
    language: str
    text: str
    score: float
    doc_type: DocType | None = None
    doc_kind: DocType | None = None
    kb_path: str | None = None
    domain: str | None = None
    feature: str | None = None
    module: str | None = None
    submenu: str | None = None
    screen_id: str | None = None
    screen_title: str | None = None
    tab_name: str | None = None
    section_title: str | None = None
    heading_path: list[str] = Field(default_factory=list)
    chunk_kind: str | None = None
    step_start: int | None = None
    step_end: int | None = None
    task_tags: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    aliases: list[str] = Field(default_factory=list)
    error_codes: list[str] = Field(default_factory=list)
    role_scope: list[str] = Field(default_factory=list)
    erp_versions: list[str] = Field(default_factory=list)
    review_status: ReviewStatus = "approved"
    source_uri: str | None = None
    retrieval_reasons: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _sync_metadata(self) -> "QuerySource":
        kind = self.doc_kind or self.doc_type or "overview"
        self.doc_kind = kind
        self.doc_type = kind
        return self


class KnowledgeCitation(BaseModel):
    chunk_id: str
    title: str
    section_title: str | None = None
    source_uri: str | None = None
    doc_type: DocType | None = None
    doc_kind: DocType | None = None
    domain: str | None = None
    feature: str | None = None
    module: str | None = None
    screen_title: str | None = None
    tab_name: str | None = None
    score: float

    @model_validator(mode="after")
    def _sync_metadata(self) -> "KnowledgeCitation":
        kind = self.doc_kind or self.doc_type or "overview"
        self.doc_kind = kind
        self.doc_type = kind
        return self


class ScreenContextSummary(BaseModel):
    application: str | None = None
    module: str | None = None
    submenu: str | None = None
    screen_id: str | None = None
    screen_title: str | None = None
    tab_name: str | None = None
    current_action: str | None = None
    breadcrumb: list[str] = Field(default_factory=list)
    error_messages: list[str] = Field(default_factory=list)
    field_count: int = 0
    sensitive_field_count: int = 0


class GeneratedAnswer(BaseModel):
    answer: str
    steps: list[str] = Field(default_factory=list)
    follow_up_question: str | None = None
    confidence: float | None = None
    answer_mode: AnswerMode = "grounded"
    inference_notice: str | None = None
    prompt_tokens: int = 0
    completion_tokens: int = 0


class RedactionResult(BaseModel):
    screen_context: ScreenContext
    redacted_fields: list[str] = Field(default_factory=list)
    notice: str | None = None


class RetrievalCandidateDebug(BaseModel):
    chunk_id: str
    title: str
    doc_kind: DocType | None = None
    source_uri: str | None = None
    scope: ResolvedSearchScope
    score: float
    dense_score: float
    lexical_score: float
    exact_match_score: float
    normalized_dense: float
    normalized_lexical: float
    normalized_exact: float
    doc_kind_match: float
    scope_specificity: float
    role_match: float
    version_match: float
    selected: bool
    selection_reason: str | None = None
    retrieval_reasons: list[str] = Field(default_factory=list)


class RetrievalDiagnostics(BaseModel):
    query_plan: QueryPlan
    active_filters: dict[str, list[str] | str] = Field(default_factory=dict)
    semantic_query: str
    lexical_index_path: str | None = None
    candidate_count: int = 0
    returned_count: int = 0
    score_floor: float | None = None
    returned_chunk_ids: list[str] = Field(default_factory=list)
    candidates: list[RetrievalCandidateDebug] = Field(default_factory=list)


class QueryResponse(BaseModel):
    answer: str
    steps: list[str]
    citations: list[KnowledgeCitation]
    follow_up_question: str | None
    confidence: float | None
    used_screen_context: ScreenContextSummary
    redaction_notice: str | None
    answer_mode: AnswerMode = "grounded"
    inference_notice: str | None = None
    retrieval_diagnostics: RetrievalDiagnostics | None = None


class KBValidationError(BaseModel):
    kb_path: str
    message: str


class ChunkRecord(BaseModel):
    chunk_id: str
    doc_id: str
    title: str
    text: str
    source: str
    language: str
    doc_type: DocType | None = None
    doc_kind: DocType | None = None
    kb_path: str | None = None
    domain: str | None = None
    feature: str | None = None
    module: str | None = None
    submenu: str | None = None
    screen_id: str | None = None
    screen_title: str | None = None
    tab_name: str | None = None
    section_title: str | None = None
    heading_path: list[str] = Field(default_factory=list)
    chunk_kind: str | None = None
    step_start: int | None = None
    step_end: int | None = None
    field_labels: list[str] = Field(default_factory=list)
    task_tags: list[str] = Field(default_factory=list)
    keywords: list[str] = Field(default_factory=list)
    aliases: list[str] = Field(default_factory=list)
    error_codes: list[str] = Field(default_factory=list)
    role_scope: list[str] = Field(default_factory=list)
    erp_versions: list[str] = Field(default_factory=list)
    review_status: ReviewStatus = "approved"
    source_uri: str | None = None
    token_estimate: int = 0
    ingested_at: str

    @model_validator(mode="after")
    def _sync_metadata(self) -> "ChunkRecord":
        kind = self.doc_kind or self.doc_type or "overview"
        self.doc_kind = kind
        self.doc_type = kind
        return self


class QueryPlan(BaseModel):
    intent_label: IntentLabel
    preferred_doc_kinds: list[DocType] = Field(default_factory=list)
    semantic_query: str
    lexical_query_terms: list[str] = Field(default_factory=list)
    hard_filters: dict[str, list[str] | str] = Field(default_factory=dict)
    soft_signals: dict[str, list[str]] = Field(default_factory=dict)
    scope_order: list[ResolvedSearchScope] = Field(default_factory=lambda: ["screen", "module", "global"])


class RetrievalCandidate(BaseModel):
    source: QuerySource
    dense_score: float = 0.0
    lexical_score: float = 0.0
    exact_match_score: float = 0.0
    normalized_dense: float = 0.0
    normalized_lexical: float = 0.0
    normalized_exact: float = 0.0
    doc_kind_match: float = 0.0
    scope_specificity: float = 0.0
    role_match: float = 0.0
    version_match: float = 0.0
    final_score: float = 0.0
    scope: ResolvedSearchScope = "global"
    selected: bool = False
    selection_reason: str | None = None
    retrieval_reasons: list[str] = Field(default_factory=list)
