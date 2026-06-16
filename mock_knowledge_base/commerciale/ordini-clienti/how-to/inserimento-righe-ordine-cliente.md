---
title: Inserimento righe ordine cliente
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - inserimento righe ordine
  - corpo ordine
  - aggiunta articolo ordine
  - righe ordine cliente
task_tags:
  - inserimento righe ordine
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Commerciale
screen_title: Ordini clienti
aliases:
  - corpo ordine
  - righe ordine
field_labels:
  - Numero riga
  - Articolo
  - Quantità e valore
  - Prezzo
  - Importo netto
source_uri: :contentReference[oaicite:0]{index=0}
---
# Inserimento righe ordine cliente

## Prerequisiti
- L’ordine cliente deve essere già stato creato in testata.
- Se l’ordine deriva da offerta, le righe sono già precompilate.

## Procedura
1. Aprire l’ordine cliente e posizionarsi nella sezione corpo.
2. Cliccare sull’icona “+” verde per aggiungere una nuova riga.
3. Compilare il campo **Numero riga** (progressivo proposto automaticamente, modificabile).
4. Inserire il campo **Articolo**:
   - Digitare il codice articolo, oppure
   - Digitare una parte della descrizione e selezionare dalla lista proposta.
5. Selezionare il campo **Quantità e valore** scegliendo:
   - “a quantità” per gestire l'evasione a quantità,
   - “a valore” per gestire l'evasione ad importo della riga.
1. Verificare o modificare la **Descrizione articolo** (editabile per articoli non codificati).
2. Inserire le quantità:
   - Quantità di vendita o di prezzo → il sistema riporta l'unità di misura gestionale
   - Oppure quantità gestionale → aggiorna la quantità di prezzo.
1.  le unità di misura vengono riportate automaticamente in relazione a quelle impostate nell'anagrafica dell'articolo, nel caso siano diverse (vendita, prezzo, gestionale), vengono calcolate in relazione ai relativi fattori di conversione presenti sempre in anagrafica dell'articolo.
2. All'inserimento o alla modifica dei **Colli** (se configurati in anagrafica articolo), che possono aggiornare la quantità gestionale.
3. Inserire o verificare il **Prezzo**:
    - Proposto automaticamente da listino o anagrafica articolo,
    - Obbligatorio se previsto dal tipo ordine o articolo.
4. Inserire eventuali **Sconti** (fino a tre percentuali con operatori + o -).
5. Verificare i valori calcolati automaticamente:
    - **Importo lordo**
    - **Importo netto**
6. Compilare eventuali campi aggiuntivi:
    - Date (richiesta, concordata, consegna)
    - Flag tassativo
7. Completare eventuali tab aggiuntivi (dati aggiuntivi, spedizione, analitica, agenti, pagamenti, sconti, note).
8. Salvare la riga.

## Verifiche finali
- Verificare che quantità, prezzo e importo siano coerenti.
- Controllare che la data di consegna sia valorizzata (obbligatoria).
- Verificare eventuali sconti e provvigioni applicate.