"""Query planning for ERP-aware retrieval."""

from __future__ import annotations

import re

from app.context.normalizer import normalize_search_text, tokenize_search_text
from app.core.config import Settings
from app.core.normalization import normalize_erp_version
from app.domain.schemas import QueryPlan, QueryRequest, ResolvedSearchScope, ScreenContext
from app.retrieval.topic_resolver import TopicResolver

ERROR_CODE_PATTERN = re.compile(r"\b[A-Z]{2,}(?:-[A-Z0-9]+)+\b")
ACRONYM_PATTERN = re.compile(r"\b[A-Z][A-Z0-9]{1,7}\b")
FIELD_KEY_ANCHORS = {"campo", "codice", "flag", "tabella"}
KEY_TERM_BOUNDARIES = {
    "a",
    "ad",
    "all",
    "alla",
    "alle",
    "allo",
    "che",
    "come",
    "con",
    "da",
    "dal",
    "dalla",
    "de",
    "dei",
    "del",
    "della",
    "delle",
    "dello",
    "dentro",
    "di",
    "dove",
    "e",
    "il",
    "in",
    "interno",
    "la",
    "le",
    "lo",
    "magia",
    "nel",
    "nella",
    "o",
    "per",
    "quando",
    "se",
    "su",
    "un",
    "una",
}
KEY_TERM_STOPWORDS = KEY_TERM_BOUNDARIES | {
    "campo",
    "codice",
    "cosa",
    "devo",
    "fare",
    "gestionale",
    "inserire",
    "posso",
    "qual",
    "quale",
    "quali",
}


class QueryPlanner:
    def __init__(self, settings: Settings, topic_resolver: TopicResolver | None = None) -> None:
        self.settings = settings
        self.topic_resolver = topic_resolver or TopicResolver()

    def build(self, request: QueryRequest, screen_context: ScreenContext) -> QueryPlan:
        message = request.message.strip()
        lowered = normalize_search_text(message) or ""
        error_codes = self._extract_error_codes(message, screen_context)

        if (
            error_codes
            or screen_context.error_messages
            or any(field.validation_error for field in screen_context.fields)
            or any(
                token in lowered
                for token in ("errore", "problema", "anomalia", "squadrat", "risolv", "blocc", "fallisc")
            )
        ):
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
            "must_match_terms": self._extract_must_match_terms(message, screen_context),
        }
        topic_match = self.topic_resolver.resolve(message)
        if topic_match:
            soft_signals["requested_topic"] = [topic_match.topic_id]
            soft_signals["requested_topic_aliases"] = list(topic_match.matched_aliases)

        lexical_terms = tokenize_search_text(
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
        requested_version = normalize_erp_version(self.settings.erp_version)

        hard_filters = {
            "review_status": ["approved"],
            "erp_versions": [requested_version] if requested_version else [],
            "role_scope": role_scope,
            "doc_kinds": preferred_doc_kinds,
        }
        if topic_match:
            hard_filters["features"] = list(topic_match.features)
            hard_filters["topic_modules"] = list(topic_match.modules)
            hard_filters["source_uri_prefixes"] = list(topic_match.source_uri_prefixes)

        return QueryPlan(
            intent_label=intent_label,  # type: ignore[arg-type]
            preferred_doc_kinds=preferred_doc_kinds,
            semantic_query=semantic_query or message,
            lexical_query_terms=lexical_terms,
            hard_filters=hard_filters,
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

    def _extract_must_match_terms(self, message: str, screen_context: ScreenContext) -> list[str]:
        cleaned_message = ERROR_CODE_PATTERN.sub(" ", message)
        normalized_message = normalize_search_text(cleaned_message) or ""
        terms: list[str] = []

        for match in ACRONYM_PATTERN.findall(cleaned_message):
            if self._is_key_acronym(match):
                self._append_unique(terms, match)

        tokens = normalized_message.split()
        for index, token in enumerate(tokens):
            if token not in FIELD_KEY_ANCHORS:
                continue

            tail: list[str] = []
            for candidate in tokens[index + 1 : index + 5]:
                if candidate in KEY_TERM_BOUNDARIES or len(candidate) < 2:
                    break
                tail.append(candidate)
                if len(tail) >= 3:
                    break

            if not tail:
                continue

            phrase_starts_at_tail = False
            phrase_tokens = [token, *tail]
            if token == "campo" and tail[0] in FIELD_KEY_ANCHORS and len(tail) > 1:
                phrase_tokens = tail
                phrase_starts_at_tail = True
            self._append_unique(terms, " ".join(phrase_tokens))

            specific_term = tail[1] if phrase_starts_at_tail and len(tail) > 1 else tail[0]
            if self._looks_like_specific_term(specific_term):
                self._append_unique(terms, specific_term)

        for field in screen_context.fields:
            normalized_label = normalize_search_text(field.label)
            if (
                normalized_label
                and " " in normalized_label
                and normalized_label in normalized_message
            ):
                self._append_unique(terms, normalized_label)

        return terms

    def _is_key_acronym(self, value: str) -> bool:
        normalized = normalize_search_text(value) or ""
        return bool(normalized and normalized not in KEY_TERM_STOPWORDS and any(char.isalpha() for char in value))

    def _looks_like_specific_term(self, value: str) -> bool:
        return bool(value and (len(value) <= 5 or any(char.isdigit() for char in value)))

    def _append_unique(self, values: list[str], value: str) -> None:
        cleaned = " ".join(value.split()).strip()
        if cleaned and cleaned not in values:
            values.append(cleaned)

    def _compact(self, *values: str | None) -> list[str]:
        compacted: list[str] = []
        for value in values:
            text = " ".join(str(value or "").split()).strip()
            if text and text not in compacted:
                compacted.append(text)
        return compacted
