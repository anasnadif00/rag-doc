"""Normalization and intent heuristics for ERP copilot requests."""

from __future__ import annotations

import re
import unicodedata

from app.domain.schemas import (
    FieldContext,
    QueryRequest,
    RecordContext,
    ScreenContext,
    ScreenContextSummary,
    TableContext,
    TaskIntent,
    UserContext,
)

SEARCH_TOKEN_PATTERN = re.compile(r"[a-z0-9_]+")
ITALIAN_STOPWORDS = {
    "a",
    "ad",
    "ai",
    "al",
    "alla",
    "alle",
    "allo",
    "cosa",
    "cos",
    "da",
    "dal",
    "dalla",
    "delle",
    "dello",
    "dei",
    "del",
    "della",
    "di",
    "e",
    "ed",
    "gli",
    "i",
    "il",
    "in",
    "l",
    "la",
    "le",
    "lo",
    "nei",
    "nel",
    "nella",
    "o",
    "per",
    "su",
    "tra",
    "un",
    "una",
    "uno",
}
STEM_SUFFIXES = ("mente", "zione", "zioni")


def _clean_text(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = " ".join(str(value).split())
    return cleaned or None


def _clean_list(values: list[str]) -> list[str]:
    cleaned: list[str] = []
    for value in values:
        item = _clean_text(value)
        if item and item not in cleaned:
            cleaned.append(item)
    return cleaned


def normalize_search_text(value: str | None) -> str | None:
    cleaned = _clean_text(value)
    if cleaned is None:
        return None

    normalized = unicodedata.normalize("NFKD", cleaned.casefold())
    flattened = "".join(char for char in normalized if not unicodedata.combining(char))
    flattened = flattened.replace("’", " ").replace("'", " ")
    flattened = re.sub(r"[^a-z0-9_]+", " ", flattened)
    compacted = " ".join(flattened.split())
    return compacted or None


def tokenize_search_text(value: str | None, dedupe: bool = True) -> list[str]:
    normalized = normalize_search_text(value)
    if not normalized:
        return []

    tokens: list[str] = []
    seen: set[str] = set()
    for token in SEARCH_TOKEN_PATTERN.findall(normalized):
        if len(token) < 2 or token in ITALIAN_STOPWORDS:
            continue
        for variant in _token_variants(token):
            if dedupe:
                if variant in seen:
                    continue
                seen.add(variant)
            tokens.append(variant)
    return tokens


def normalize_search_list(values: list[str]) -> list[str]:
    normalized: list[str] = []
    for value in values:
        item = normalize_search_text(value)
        if item and item not in normalized:
            normalized.append(item)
    return normalized


def _token_variants(token: str) -> list[str]:
    variants = [token]
    stem = _stem_token(token)
    if stem and stem not in variants:
        variants.append(stem)
    return variants


def _stem_token(token: str) -> str | None:
    if len(token) < 5:
        return None

    for suffix in STEM_SUFFIXES:
        if token.endswith(suffix) and len(token) - len(suffix) >= 4:
            return token[: -len(suffix)]

    if token.endswith(("i", "e", "o", "a")) and len(token) >= 5:
        return token[:-1]

    return None


def normalize_query_request(request: QueryRequest, default_locale: str) -> QueryRequest:
    screen = request.screen_context
    fields = [
        FieldContext(
            field_id=_clean_text(field.field_id),
            label=_clean_text(field.label) or "Campo senza etichetta",
            value=_clean_text(field.value),
            masked_value=_clean_text(field.masked_value),
            is_sensitive=field.is_sensitive,
            is_required=field.is_required,
            is_editable=field.is_editable,
            validation_error=_clean_text(field.validation_error),
        )
        for field in screen.fields
    ]

    selected_record = None
    if screen.selected_record:
        selected_record = RecordContext(
            record_id=_clean_text(screen.selected_record.record_id),
            primary_label=_clean_text(screen.selected_record.primary_label),
            values={
                _clean_text(str(key)) or str(key): value
                for key, value in screen.selected_record.values.items()
            },
        )

    table_context = None
    if screen.table_context:
        table_context = TableContext(
            table_id=_clean_text(screen.table_context.table_id),
            title=_clean_text(screen.table_context.title),
            visible_columns=_clean_list(screen.table_context.visible_columns),
            selected_row_index=screen.table_context.selected_row_index,
            row_count=screen.table_context.row_count,
        )

    breadcrumb = _clean_list(screen.breadcrumb)
    if not breadcrumb:
        breadcrumb = _clean_list(
            [
                screen.application or "",
                screen.module or "",
                screen.submenu or "",
                screen.screen_title or "",
            ]
        )

    user_context = None
    if request.user_context:
        user_context = UserContext(
            username=_clean_text(request.user_context.username),
            roles=_clean_list(request.user_context.roles),
            company_code=_clean_text(request.user_context.company_code),
            division=_clean_text(request.user_context.division),
        )

    return QueryRequest(
        message=_clean_text(request.message) or "",
        conversation_id=_clean_text(request.conversation_id),
        user_locale=_clean_text(request.user_locale) or default_locale,
        screen_context=ScreenContext(
            application=_clean_text(screen.application),
            module=_clean_text(screen.module),
            submenu=_clean_text(screen.submenu),
            screen_id=_clean_text(screen.screen_id),
            screen_title=_clean_text(screen.screen_title),
            tab_name=_clean_text(screen.tab_name),
            breadcrumb=breadcrumb,
            current_action=_clean_text(screen.current_action),
            error_messages=_clean_list(screen.error_messages),
            free_text_context=_clean_text(screen.free_text_context),
            fields=fields,
            selected_record=selected_record,
            table_context=table_context,
        ),
        user_context=user_context,
        retrieval_options=request.retrieval_options,
    )


def infer_task_intent(message: str, screen_context: ScreenContext) -> TaskIntent:
    lowered = normalize_search_text(message) or ""
    label = "general_guidance"
    hints: list[str] = []

    if screen_context.error_messages or "errore" in lowered or "error" in lowered:
        label = "error_resolution"
        hints.append("risoluzione errore")
    elif any(token in lowered for token in ("crea", "inser", "nuov", "aggiung")):
        label = "record_creation"
        hints.append("creazione record")
    elif any(token in lowered for token in ("modifica", "aggiorna", "cambia")):
        label = "record_update"
        hints.append("aggiornamento record")
    elif any(token in lowered for token in ("cerca", "trova", "filtra", "ricerca")):
        label = "record_lookup"
        hints.append("ricerca record")
    elif any(token in lowered for token in ("stampa", "report", "esporta")):
        label = "reporting"
        hints.append("stampa o esportazione")

    search_terms = _clean_list(
        [
            message,
            screen_context.module or "",
            screen_context.submenu or "",
            screen_context.screen_title or "",
            screen_context.tab_name or "",
            screen_context.current_action or "",
            screen_context.free_text_context or "",
            *screen_context.error_messages,
            *(field.label for field in screen_context.fields if field.validation_error),
        ]
    )

    return TaskIntent(label=label, search_terms=search_terms, hints=hints)


def summarize_screen_context(screen_context: ScreenContext) -> ScreenContextSummary:
    sensitive_count = sum(1 for field in screen_context.fields if field.is_sensitive)
    return ScreenContextSummary(
        application=screen_context.application,
        module=screen_context.module,
        submenu=screen_context.submenu,
        screen_id=screen_context.screen_id,
        screen_title=screen_context.screen_title,
        tab_name=screen_context.tab_name,
        current_action=screen_context.current_action,
        breadcrumb=screen_context.breadcrumb,
        error_messages=screen_context.error_messages,
        field_count=len(screen_context.fields),
        sensitive_field_count=sensitive_count,
    )
