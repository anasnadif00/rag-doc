"""Lexical retrieval over the chunk manifest generated during ingest."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

from app.context.normalizer import normalize_search_text, tokenize_search_text
from app.core.config import Settings
from app.domain.schemas import QueryPlan, QuerySource, RetrievalCandidate, ResolvedSearchScope


class LexicalRetriever:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.index_path = Path(settings.lexical_index_path)

    def search(
        self,
        plan: QueryPlan,
        scope: ResolvedSearchScope,
        limit: int,
    ) -> list[RetrievalCandidate]:
        entries = [entry for entry in self._load_entries() if self._matches_filters(entry, plan, scope)]
        if not entries or not plan.lexical_query_terms:
            return []

        document_frequencies = self._document_frequencies(entries)
        average_length = sum(self._document_length(entry) for entry in entries) / max(len(entries), 1)

        candidates: list[RetrievalCandidate] = []
        for entry in entries:
            term_frequencies = self._term_frequencies(entry)
            score = self._bm25_score(
                term_frequencies=term_frequencies,
                query_terms=plan.lexical_query_terms,
                document_frequencies=document_frequencies,
                total_documents=len(entries),
                average_length=average_length,
            )
            if score <= 0:
                continue
            candidate = RetrievalCandidate(
                source=self._to_source(entry, score=score),
                lexical_score=score,
                scope=scope,
                retrieval_reasons=[f"match lessicale su scope {scope}"],
            )
            candidates.append(candidate)

        candidates.sort(key=lambda item: item.lexical_score, reverse=True)
        return candidates[:limit]

    def exact_match(
        self,
        plan: QueryPlan,
        scope: ResolvedSearchScope,
        limit: int,
    ) -> list[RetrievalCandidate]:
        entries = [entry for entry in self._load_entries() if self._matches_filters(entry, plan, scope)]
        signals = {
            "error_codes": self._normalized_set(plan.soft_signals.get("error_codes", [])),
            "screen_id": self._normalized_set(plan.soft_signals.get("screen_id", [])),
            "screen_title": self._normalized_set(plan.soft_signals.get("screen_title", [])),
            "tab_name": self._normalized_set(plan.soft_signals.get("tab_name", [])),
            "aliases": self._normalized_set(plan.soft_signals.get("aliases", [])),
        }

        candidates: list[RetrievalCandidate] = []
        for entry in entries:
            reasons: list[str] = []
            exact_score = 0.0
            for field_name, expected_values in signals.items():
                if not expected_values:
                    continue
                actual_values = entry.get(field_name)
                if isinstance(actual_values, list):
                    normalized_actual = self._normalized_set(actual_values)
                else:
                    normalized_value = normalize_search_text(str(actual_values)) if actual_values else None
                    normalized_actual = {normalized_value} if normalized_value else set()
                matched = expected_values & normalized_actual
                if matched:
                    exact_score += 0.5 if field_name in {"screen_title", "tab_name", "aliases"} else 1.0
                    reasons.append(f"match esatto {field_name}: {', '.join(sorted(matched))}")
            if exact_score <= 0:
                continue
            candidates.append(
                RetrievalCandidate(
                    source=self._to_source(entry, score=exact_score),
                    exact_match_score=exact_score,
                    scope=scope,
                    retrieval_reasons=reasons,
                )
            )

        candidates.sort(key=lambda item: item.exact_match_score, reverse=True)
        return candidates[:limit]

    def _load_entries(self) -> list[dict[str, Any]]:
        if not self.index_path.exists():
            return []
        payload = json.loads(self.index_path.read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            return []
        return [entry for entry in payload if isinstance(entry, dict)]

    def _matches_filters(
        self,
        entry: dict[str, Any],
        plan: QueryPlan,
        scope: ResolvedSearchScope,
    ) -> bool:
        if not self._matches_hard_filters(entry, plan):
            return False
        return self._matches_scope(entry, plan, scope)

    def _matches_hard_filters(self, entry: dict[str, Any], plan: QueryPlan) -> bool:
        review_statuses = {value.lower() for value in self._as_list(plan.hard_filters.get("review_status"))}
        if review_statuses and str(entry.get("review_status", "")).lower() not in review_statuses:
            return False

        doc_kinds = {value.lower() for value in self._as_list(plan.hard_filters.get("doc_kinds"))}
        if doc_kinds and str(entry.get("doc_kind", entry.get("doc_type", ""))).lower() not in doc_kinds:
            return False

        requested_versions = {value.lower() for value in self._as_list(plan.hard_filters.get("erp_versions"))}
        entry_versions = {value.lower() for value in self._as_list(entry.get("erp_versions"))}
        if requested_versions and entry_versions and not (requested_versions & entry_versions):
            return False

        role_scope = {value.lower() for value in self._as_list(plan.hard_filters.get("role_scope"))}
        entry_roles = {value.lower() for value in self._as_list(entry.get("role_scope"))}
        if role_scope and entry_roles and not (role_scope & entry_roles):
            return False
        return True

    def _matches_scope(
        self,
        entry: dict[str, Any],
        plan: QueryPlan,
        scope: ResolvedSearchScope,
    ) -> bool:
        if scope == "global":
            return True

        module_values = self._normalized_set(plan.soft_signals.get("module", []))
        submenu_values = self._normalized_set(plan.soft_signals.get("submenu", []))
        screen_ids = self._normalized_set(plan.soft_signals.get("screen_id", []))
        screen_titles = self._normalized_set(plan.soft_signals.get("screen_title", []))
        tab_names = self._normalized_set(plan.soft_signals.get("tab_name", []))

        entry_module = normalize_search_text(str(entry.get("module") or ""))
        entry_submenu = normalize_search_text(str(entry.get("submenu") or ""))
        entry_screen_id = normalize_search_text(str(entry.get("screen_id") or ""))
        entry_screen_title = normalize_search_text(str(entry.get("screen_title") or ""))
        entry_tab = normalize_search_text(str(entry.get("tab_name") or ""))

        if scope == "module":
            if module_values and entry_module and entry_module in module_values:
                return True
            if submenu_values and entry_submenu and entry_submenu in submenu_values:
                return True
            return not module_values and not submenu_values

        if screen_ids and entry_screen_id and entry_screen_id not in screen_ids:
            return False
        if not screen_ids and screen_titles and entry_screen_title and entry_screen_title not in screen_titles:
            return False
        if tab_names and entry_tab and entry_tab not in tab_names:
            return False
        if module_values and entry_module and entry_module not in module_values:
            return False
        return bool(screen_ids or screen_titles or tab_names or module_values)

    def _document_frequencies(self, entries: list[dict[str, Any]]) -> dict[str, int]:
        frequencies: dict[str, int] = {}
        for entry in entries:
            unique_terms = set(self._term_frequencies(entry))
            for term in unique_terms:
                frequencies[term] = frequencies.get(term, 0) + 1
        return frequencies

    def _term_frequencies(self, entry: dict[str, Any]) -> dict[str, int]:
        frequencies: dict[str, int] = {}
        for token in self._document_tokens(entry):
            frequencies[token] = frequencies.get(token, 0) + 1
        return frequencies

    def _document_tokens(self, entry: dict[str, Any]) -> list[str]:
        values: list[str] = [
            str(entry.get("title") or ""),
            str(entry.get("section_title") or ""),
            str(entry.get("text") or ""),
            " ".join(self._as_list(entry.get("keywords"))),
            " ".join(self._as_list(entry.get("aliases"))),
            " ".join(self._as_list(entry.get("task_tags"))),
            " ".join(self._as_list(entry.get("error_codes"))),
        ]
        tokens: list[str] = []
        for value in values:
            tokens.extend(tokenize_search_text(value, dedupe=False))
        return tokens

    def _document_length(self, entry: dict[str, Any]) -> int:
        return max(1, len(self._document_tokens(entry)))

    def _bm25_score(
        self,
        term_frequencies: dict[str, int],
        query_terms: list[str],
        document_frequencies: dict[str, int],
        total_documents: int,
        average_length: float,
    ) -> float:
        score = 0.0
        document_length = max(sum(term_frequencies.values()), 1)
        k1 = 1.5
        b = 0.75
        for term in query_terms:
            frequency = term_frequencies.get(term, 0)
            if frequency <= 0:
                continue
            document_frequency = document_frequencies.get(term, 0)
            idf = math.log(1 + ((total_documents - document_frequency + 0.5) / (document_frequency + 0.5)))
            numerator = frequency * (k1 + 1)
            denominator = frequency + k1 * (1 - b + b * (document_length / max(average_length, 1.0)))
            score += idf * (numerator / denominator)
        return score

    def _to_source(self, entry: dict[str, Any], score: float) -> QuerySource:
        return QuerySource(**(entry | {"score": score}))

    def _as_list(self, value: Any) -> list[str]:
        if value is None:
            return []
        if isinstance(value, (list, tuple, set)):
            return [str(item) for item in value if str(item).strip()]
        return [str(value)]

    def _normalized_set(self, values: list[str] | tuple[str, ...] | set[str] | Any) -> set[str]:
        normalized: set[str] = set()
        for value in self._as_list(values):
            item = normalize_search_text(value)
            if item:
                normalized.add(item)
        return normalized
