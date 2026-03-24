"""Prompt templates and formatting helpers for the ERP copilot."""

from __future__ import annotations

from app.domain.schemas import QueryPlan, QuerySource, ScreenContext

ERP_SYSTEM_PROMPT = """Sei un assistente ERP in sola lettura.
Rispondi sempre in italiano.
Usa prima di tutto il contesto della schermata e le fonti recuperate.
Mantieni esattamente le etichette ERP visibili all'utente.
Privilegia istruzioni operative passo-passo.
Se le fonti non supportano una risposta sicura, non inventare click-path o nomi campo specifici.
Se devi integrare con inferenza generale, dichiaralo esplicitamente dentro inference_notice.
Se il contesto non basta o le fonti non supportano una risposta sicura, fai una sola domanda di chiarimento.
Non promettere automazioni o azioni dirette nel gestionale.
Restituisci solo JSON valido con questa struttura:
{
  "answer": "string",
  "steps": ["string"],
  "follow_up_question": "string o null",
  "confidence": 0.0,
  "answer_mode": "grounded | partial_inference | clarification",
  "inference_notice": "string o null"
}
"""


def _format_fields(screen_context: ScreenContext) -> str:
    lines: list[str] = []
    for field in screen_context.fields:
        value = field.value if field.value is not None else field.masked_value
        parts = [field.label]
        if value:
            parts.append(f"valore={value}")
        if field.validation_error:
            parts.append(f"errore={field.validation_error}")
        if field.is_required:
            parts.append("obbligatorio")
        if not field.is_editable:
            parts.append("sola lettura")
        lines.append(" - " + ", ".join(parts))
    return "\n".join(lines) or " - Nessun campo disponibile"


def _format_sources(sources: list[QuerySource], max_context_chars: int) -> str:
    rendered: list[str] = []
    budget = max_context_chars
    for index, source in enumerate(sources, start=1):
        excerpt = source.text[: min(len(source.text), 900)]
        block = "\n".join(
            [
                f"[Fonte {index}]",
                f"Titolo: {source.title}",
                f"Tipo: {source.doc_kind}",
                f"Dominio: {source.domain or '-'}",
                f"Feature: {source.feature or '-'}",
                f"Modulo: {source.module or '-'}",
                f"Schermata: {source.screen_title or '-'}",
                f"Tab: {source.tab_name or '-'}",
                f"Sezione: {source.section_title or '-'}",
                f"Heading path: {' > '.join(source.heading_path) if source.heading_path else '-'}",
                f"Perche selezionata: {'; '.join(source.retrieval_reasons) or '-'}",
                f"Contenuto: {excerpt}",
            ]
        )
        if len(block) > budget:
            break
        rendered.append(block)
        budget -= len(block)
    return "\n\n".join(rendered)


def build_user_prompt(
    message: str,
    screen_context: ScreenContext,
    query_plan: QueryPlan,
    sources: list[QuerySource],
    max_context_chars: int,
) -> str:
    breadcrumb = " > ".join(screen_context.breadcrumb) if screen_context.breadcrumb else "-"
    errors = "\n".join(f" - {item}" for item in screen_context.error_messages) or " - Nessun errore"
    source_context = _format_sources(sources, max_context_chars)

    return "\n\n".join(
        [
            f"Messaggio utente:\n{message}",
            "Contesto schermata:\n"
            f"Applicazione: {screen_context.application or '-'}\n"
            f"Modulo: {screen_context.module or '-'}\n"
            f"Sottomenu: {screen_context.submenu or '-'}\n"
            f"Schermata: {screen_context.screen_title or '-'}\n"
            f"Screen ID: {screen_context.screen_id or '-'}\n"
            f"Tab: {screen_context.tab_name or '-'}\n"
            f"Breadcrumb: {breadcrumb}\n"
            f"Azione corrente: {screen_context.current_action or '-'}\n"
            f"Contesto libero: {screen_context.free_text_context or '-'}",
            f"Campi visibili:\n{_format_fields(screen_context)}",
            f"Errori visibili:\n{errors}",
            "Piano di retrieval:\n"
            f"Intento: {query_plan.intent_label}\n"
            f"Doc kind preferiti: {', '.join(query_plan.preferred_doc_kinds) or '-'}\n"
            f"Termini lessicali: {', '.join(query_plan.lexical_query_terms) or '-'}\n"
            f"Segnali morbidi: {query_plan.soft_signals}",
            f"Fonti recuperate:\n{source_context or 'Nessuna fonte recuperata'}",
        ]
    )
