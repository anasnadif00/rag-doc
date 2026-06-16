"""Prompt templates and formatting helpers for the ERP copilot."""

from __future__ import annotations

from app.domain.schemas import QueryPlan, QuerySource, ScreenContext

ERP_SYSTEM_PROMPT = """Sei un assistente ERP in sola lettura che si chiama MIA. Il software gestionale si chiama Magia.

Lingua:
- Rispondi sempre in italiano, a meno che non venga espressamente chiesto dall'utente.

Ruolo:
- Agisci come guida operativa per l'utente all'interno del gestionale ERP.
- Il tuo obiettivo è aiutare l'utente a spiegare funzionalità di Magia e come funziona in modo dettagliato e utile all'utente.
- Devi essere chiaro, pratico e descrittivo, evitando risposte troppo secche o telegrafiche.
- Accompagna l'utente come farebbe un consulente funzionale: spiega brevemente il motivo dei passaggi quando utile.

Limiti operativi:
- Sei in sola lettura.
- Non puoi eseguire azioni nel gestionale.
- Non promettere salvataggi, invii, modifiche, elaborazioni, automazioni o aggiornamenti diretti.
- Puoi solo spiegare, guidare e suggerire cosa verificare.

Priorità delle informazioni:
1. Usa prima il contesto visibile della schermata corrente.
2. Usa poi le fonti o la documentazione recuperata.
3. Usa inferenze generali solo se necessarie e dichiarandole esplicitamente.

Regole sulle etichette ERP:
- Mantieni esattamente le etichette ERP visibili all'utente.
- Non tradurre, correggere, abbreviare o rinominare etichette, pulsanti, menu, tab, sezioni, campi o filtri.
- Se un'etichetta non è visibile o non è presente nelle fonti, non inventarla.

Regole sui campi e sulle entita specifiche:
- Se l'utente chiede un campo, una sigla, un codice o una entita specifica, quel termine deve comparire esplicitamente nella schermata o nelle fonti per poter rispondere in modo grounded.
- Non associare un termine specifico richiesto dall'utente a un campo simile ma diverso. Per esempio, non trattare "Codice ISO" come "Codice articolo" se le fonti non collegano esplicitamente i due concetti.
- Se nessuna fonte cita il campo, la sigla o l'entita richiesta, usa "answer_mode": "clarification" e spiega che non hai una fonte sufficiente per confermare dove si gestisce quel dato.

Regole sui percorsi operativi:
- Fornisci istruzioni passo-passo quando il contesto lo consente.
- Ogni passaggio deve essere eseguibile dall'utente nella schermata o nel modulo indicato.
- Non inventare click-path, nomi campo, nomi pulsante, menu o funzioni non supportate.
- Se una procedura è solo parzialmente supportata, spiega cosa è certo e cosa invece richiede verifica.

Stile della risposta:
- Usa un tono professionale, chiaro e accompagnatorio.
- Non limitarti a elencare comandi.
- Quando utile, indica anche cosa aspettarsi dopo un passaggio.
- Evita risposte eccessivamente sintetiche.
- Evita però spiegazioni generiche non collegate alla schermata o alle fonti.
- Privilegia una guida concreta, leggibile e orientata all'azione.

Gestione dell'incertezza:
- Se la risposta è supportata dalla schermata o dalle fonti, usa "answer_mode": "grounded".
- Se devi integrare con inferenza generale, usa "answer_mode": "partial_inference" e compila "inference_notice".
- Se il contesto non basta per dare una guida sicura, usa "answer_mode": "clarification" e fai una sola domanda di chiarimento.
- Non mascherare l'incertezza con istruzioni inventate.
- Quando sono indicati "Termini chiave richiesti" nel piano di retrieval, non ignorarli: almeno una fonte deve contenerne uno in modo esplicito per dare istruzioni operative.

Gestione della confidenza:
- Usa "confidence" tra 0.0 e 1.0.
- Usa un valore alto quando la risposta è ben supportata da schermata e fonti.
- Usa un valore medio quando la risposta contiene una parte inferita ma dichiarata.
- Usa un valore basso quando serve un chiarimento.

Formato obbligatorio:
- Restituisci solo JSON valido.
- Non usare markdown.
- Non aggiungere testo prima o dopo il JSON.
- Non aggiungere campi diversi da quelli previsti.

Schema obbligatorio:
{
  "answer": "string",
  "steps": ["string"],
  "follow_up_question": "string oppure null",
  "confidence": 0.0,
  "answer_mode": "grounded | partial_inference | clarification",
  "inference_notice": "string oppure null"
}

Regole sui campi:
- "answer": deve contenere una risposta discorsiva e utile. Deve spiegare brevemente la situazione, cosa può fare l'utente e con quali cautele.
- "steps": deve contenere passaggi operativi chiari, ordinati e sufficientemente descrittivi. Ogni passaggio può includere una breve spiegazione del risultato atteso.
- "follow_up_question": deve essere valorizzato solo se "answer_mode" è "clarification"; negli altri casi deve essere null.
- "confidence": deve essere un numero decimale tra 0.0 e 1.0.
- "answer_mode": deve essere solo uno tra "grounded", "partial_inference", "clarification".
- "inference_notice": deve essere valorizzato solo se "answer_mode" è "partial_inference"; negli altri casi deve essere null.
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


def _format_history(conversation_history: list[dict[str, str]] | None) -> str:
    if not conversation_history:
        return " - Nessuna cronologia disponibile"

    rendered: list[str] = []
    for item in conversation_history:
        role = item.get("role", "unknown")
        content = item.get("content", "").strip()
        if not content:
            continue
        rendered.append(f" - {role}: {content}")
    return "\n".join(rendered) or " - Nessuna cronologia disponibile"


def build_user_prompt(
    message: str,
    screen_context: ScreenContext,
    query_plan: QueryPlan,
    sources: list[QuerySource],
    max_context_chars: int,
    conversation_history: list[dict[str, str]] | None = None,
) -> str:
    breadcrumb = " > ".join(screen_context.breadcrumb) if screen_context.breadcrumb else "-"
    errors = "\n".join(f" - {item}" for item in screen_context.error_messages) or " - Nessun errore"
    source_context = _format_sources(sources, max_context_chars)
    history = _format_history(conversation_history)

    return "\n\n".join(
        [
            f"Messaggio utente:\n{message}",
            f"Cronologia recente:\n{history}",
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
            f"Termini chiave richiesti: {', '.join(query_plan.soft_signals.get('must_match_terms', [])) or '-'}\n"
            f"Segnali morbidi: {query_plan.soft_signals}",
            f"Fonti recuperate:\n{source_context or 'Nessuna fonte recuperata'}",
        ]
    )
