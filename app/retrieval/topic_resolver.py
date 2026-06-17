"""Runtime topic resolution for retrieval filters."""

from __future__ import annotations

from dataclasses import dataclass

from app.context.normalizer import normalize_search_text


@dataclass(frozen=True)
class TopicDefinition:
    topic_id: str
    aliases: tuple[str, ...]
    features: tuple[str, ...]
    modules: tuple[str, ...] = ()
    source_uri_prefixes: tuple[str, ...] = ()
    context_terms: tuple[str, ...] = ()


@dataclass(frozen=True)
class TopicMatch:
    topic_id: str
    matched_aliases: tuple[str, ...]
    features: tuple[str, ...]
    modules: tuple[str, ...]
    source_uri_prefixes: tuple[str, ...]


TOPIC_DEFINITIONS: tuple[TopicDefinition, ...] = (
    TopicDefinition(
        topic_id="ordini-clienti",
        aliases=(
            "ordine",
            "ordini",
            "ordine cliente",
            "ordini clienti",
            "evasione ordine",
            "evasione ordini",
            "evadere ordine",
            "evadere ordini",
            "evadi ordine",
            "evadi ordini",
        ),
        features=("ordini-clienti",),
        modules=("Ordini clienti", "Ordini"),
        source_uri_prefixes=("commerciale/ordini-clienti/", "vendite/ordini-clienti/"),
        context_terms=(
            "cliente",
            "clienti",
            "consegna",
            "evadere",
            "evadi",
            "evasione",
            "evaso",
            "forzatamente",
            "inserire",
            "parzialmente",
            "portafoglio",
            "residuo",
            "riga",
            "righe",
            "scadenzario",
            "sblocca",
            "situazione",
            "stampa",
            "stato",
            "tipo",
        ),
    ),
    TopicDefinition(
        topic_id="offerte",
        aliases=(
            "offerta",
            "offerte",
            "preventivo",
            "preventivi",
            "quotazione",
            "quotazioni",
        ),
        features=("offerte",),
        modules=("Offerte",),
        source_uri_prefixes=("commerciale/offerte/",),
        context_terms=(
            "avanzamento",
            "cliente",
            "crea",
            "creare",
            "duplica",
            "invia",
            "invio",
            "preventivo",
            "revisione",
            "riga",
            "righe",
            "stampa",
            "stato",
        ),
    ),
    TopicDefinition(
        topic_id="fatture",
        aliases=(
            "fattura",
            "fatture",
            "fattura accompagnatoria",
            "fatture vendita",
            "nota credito",
            "note credito",
        ),
        features=("fatture", "fatture-vendita"),
        modules=("Fatture",),
        source_uri_prefixes=("vendite/fatture/", "commerciale/fatture-vendita/"),
        context_terms=(
            "accompagnatoria",
            "cliente",
            "credito",
            "elettronica",
            "emissione",
            "inserire",
            "iva",
            "nota",
            "pagamento",
            "riga",
            "righe",
            "stampa",
        ),
    ),
    TopicDefinition(
        topic_id="ddt-documenti-trasporto",
        aliases=(
            "ddt",
            "documento trasporto",
            "documenti trasporto",
            "documento di trasporto",
            "documenti di trasporto",
            "bolla",
            "bolle",
        ),
        features=("ddt", "ddt-documenti-trasporto"),
        modules=("DDT", "DDT documenti di trasporto"),
        source_uri_prefixes=("vendite/ddt/", "vendite/ddt-documenti-trasporto/"),
        context_terms=(
            "bolla",
            "bolle",
            "consegna",
            "documento",
            "magazzino",
            "ripresa",
            "riprendi",
            "riga",
            "righe",
            "scarico",
            "trasporto",
        ),
    ),
)

CROSS_TOPIC_TERMS = (
    "ripresa",
    "riprendi",
    "riprendere",
    "ripreso",
    "ripresi",
    "riprese",
    "genera da",
    "generare da",
    "crea da",
    "creare da",
    "da offerta",
    "da ordine",
    "da ordini",
    "in fattura",
    "in ddt",
)


class TopicResolver:
    """Infer a single primary ERP topic from explicit user wording."""

    def __init__(self, definitions: tuple[TopicDefinition, ...] = TOPIC_DEFINITIONS) -> None:
        self.definitions = definitions

    def resolve(self, message: str) -> TopicMatch | None:
        normalized_message = normalize_search_text(message) or ""
        if not normalized_message:
            return None

        matches = self._matching_topics(normalized_message)
        if len(matches) != 1:
            return None

        if self._looks_cross_topic(normalized_message):
            return None

        return matches[0]

    def _matching_topics(self, normalized_message: str) -> list[TopicMatch]:
        matches: list[TopicMatch] = []
        for definition in self.definitions:
            matched_aliases = tuple(
                alias
                for alias in definition.aliases
                if self._contains_phrase(normalized_message, normalize_search_text(alias) or "")
            )
            if not matched_aliases:
                continue
            if not self._has_strong_topic_signal(definition, normalized_message, matched_aliases):
                continue
            matches.append(
                TopicMatch(
                    topic_id=definition.topic_id,
                    matched_aliases=matched_aliases,
                    features=definition.features,
                    modules=definition.modules,
                    source_uri_prefixes=definition.source_uri_prefixes,
                )
            )
        return matches

    def _has_strong_topic_signal(
        self,
        definition: TopicDefinition,
        normalized_message: str,
        matched_aliases: tuple[str, ...],
    ) -> bool:
        if any(" " in (normalize_search_text(alias) or "") for alias in matched_aliases):
            return True
        return any(
            self._contains_phrase(normalized_message, normalize_search_text(term) or "")
            for term in definition.context_terms
        )

    def _looks_cross_topic(self, normalized_message: str) -> bool:
        return any(
            self._contains_phrase(normalized_message, normalize_search_text(term) or "")
            for term in CROSS_TOPIC_TERMS
        )

    def _contains_phrase(self, normalized_message: str, normalized_phrase: str) -> bool:
        if not normalized_phrase:
            return False
        return f" {normalized_phrase} " in f" {normalized_message} "
