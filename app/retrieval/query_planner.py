"""Query planning for ERP-aware retrieval."""

from __future__ import annotations

import re

from app.core.config import Settings
from app.domain.schemas import QueryPlan, QueryRequest, ResolvedSearchScope, ScreenContext

TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_]+")
ERROR_CODE_PATTERN = re.compile(r"\b[A-Z]{2,}(?:-[A-Z0-9]+)+\b")


class QueryPlanner:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def build(self, request: QueryRequest, screen_context: ScreenContext) -> QueryPlan:
        message = request.message.strip()
        lowered = message.lower()
        error_codes = self._extract_error_codes(message, screen_context)

        if error_codes or screen_context.error_messages or any(field.validation_error for field in screen_context.fields):
            intent_label = "troubleshooting"
            preferred_doc_kinds = ["troubleshooting", "reference", "how_to"]
        elif any(token in lowered for token in ("crea", "nuov", "annulla", "registra", "salva", "modifica", "aggiorna")):
            intent_label = "how_to"
            preferred_doc_kinds = ["how_to", "reference", "overview"]
        elif any(token in lowered for token in ("campo", "valore", "significa", "obbligatorio", "regola")):
            intent_label = "reference"
            preferred_doc_kinds = ["reference", "how_to", "overview"]
        elif any(token in lowered for token in ("schermata", "tab", "menu", "dove", "naviga")):
            intent_label = "navigation"
            preferred_doc_kinds = ["overview", "how_to", "reference"]
        else:
            intent_label = "general"
            preferred_doc_kinds = ["overview", "how_to", "reference", "faq"]

        retrieval_options = request.retrieval_options
        configured_doc_types = retrieval_options.doc_types if retrieval_options else []
        if configured_doc_types:
            preferred_doc_kinds = configured_doc_types

        role_scope = retrieval_options.role_scope if retrieval_options else []
        if not role_scope and request.user_context:
            role_scope = request.user_context.roles

        soft_signals = {
            "module": self._compact(screen_context.module),
            "submenu": self._compact(screen_context.submenu),
            "screen_id": self._compact(screen_context.screen_id),
            "screen_title": self._compact(screen_context.screen_title),
            "tab_name": self._compact(screen_context.tab_name),
            "field_labels": [field.label for field in screen_context.fields if field.label],
            "error_codes": error_codes,
            "aliases": self._compact(*screen_context.breadcrumb),
        }

        lexical_terms = self._tokenize(
            " ".join(
                [
                    message,
                    screen_context.module or "",
                    screen_context.submenu or "",
                    screen_context.screen_title or "",
                    screen_context.tab_name or "",
                    screen_context.current_action or "",
                    screen_context.free_text_context or "",
                    " ".join(screen_context.error_messages),
                    " ".join(field.label for field in screen_context.fields),
                    " ".join(error_codes),
                ]
            )
        )

        semantic_query = " | ".join(
            self._compact(
                message,
                screen_context.module,
                screen_context.submenu,
                screen_context.screen_title,
                screen_context.tab_name,
                screen_context.current_action,
                screen_context.free_text_context,
                *screen_context.error_messages,
            )
        )

        return QueryPlan(
            intent_label=intent_label,  # type: ignore[arg-type]
            preferred_doc_kinds=preferred_doc_kinds,
            semantic_query=semantic_query or message,
            lexical_query_terms=lexical_terms,
            hard_filters={
                "review_status": ["approved"],
                "erp_versions": [self.settings.erp_version],
                "role_scope": role_scope,
                "doc_kinds": preferred_doc_kinds,
            },
            soft_signals=soft_signals,
            scope_order=self._resolve_scope_order(request),
        )

    def _resolve_scope_order(self, request: QueryRequest) -> list[ResolvedSearchScope]:
        retrieval_options = request.retrieval_options
        search_scope = retrieval_options.search_scope if retrieval_options else "auto"
        return {
            "auto": ["screen", "module", "global"],
            "screen": ["screen", "module", "global"],
            "module": ["module", "global"],
            "global": ["global"],
        }.get(search_scope, ["screen", "module", "global"])  # type: ignore[return-value]

    def _extract_error_codes(self, message: str, screen_context: ScreenContext) -> list[str]:
        values = [message, *screen_context.error_messages]
        found: list[str] = []
        for value in values:
            for match in ERROR_CODE_PATTERN.findall(value):
                if match not in found:
                    found.append(match)
        return found

    def _tokenize(self, value: str) -> list[str]:
        tokens: list[str] = []
        for token in TOKEN_PATTERN.findall(value.lower()):
            if len(token) < 2 or token in tokens:
                continue
            tokens.append(token)
        return tokens

    def _compact(self, *values: str | None) -> list[str]:
        compacted: list[str] = []
        for value in values:
            text = " ".join(str(value or "").split()).strip()
            if text and text not in compacted:
                compacted.append(text)
        return compacted
