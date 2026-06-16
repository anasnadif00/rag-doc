---
title: Campi e regole del TP Sconti
doc_kind: reference
domain: commerciale
feature: fatture-vendita
keywords:
  - tp sconti
  - sconti testata
  - sconti righe
  - ricerca sconti
  - parametri commerciale
  - tipo sconto
task_tags:
  - riferimento sconti fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione
review_status: approved
module: Fatture
tab_name: Sconti
---
# Campi e regole del TP Sconti

## Regole

### Struttura del riepilogo sconti
Nel TP Sconti vengono riepilogati tutti gli sconti configurati nella tabella Parametri del Commerciale.

Gli sconti sono suddivisi in due sezioni distinte.

### Sconti di testata
La prima sezione contiene tutti i tipi di sconto per i quali nella tabella Tipo Sconto è attiva l'opzione "Sconto di testata".

Per questi sconti:

- viene visualizzata la percentuale applicata
- la percentuale viene applicata automaticamente a tutte le righe della fattura
- il valore esposto rappresenta lo sconto di testata applicato al documento

### Assenza della percentuale negli sconti di testata
Se per uno sconto di testata non viene visualizzata alcuna percentuale significa che l'applicazione dello sconto è regolata da criteri specifici per articolo.

In questi casi occorre verificare la percentuale effettivamente applicata direttamente nelle righe della fattura.

### Sconti non visibili sulle righe
La seconda sezione contiene tutti i tipi di sconto presenti nella tabella Parametri del Commerciale per i quali nella tabella Tipo Sconto non è attiva l'opzione "Visibile sulle righe".

Per questi sconti:

- viene esposto solamente il valore calcolato
- non viene mostrata la percentuale applicata
- il valore non è visibile nelle righe della fattura

### Percentuali differenziate per riga
La percentuale non viene esposta negli sconti non visibili sulle righe perché potrebbe essere differente da articolo ad articolo.

## Regole

### Ricerca automatica degli sconti
Gli sconti proposti nella fattura vengono determinati in base alle regole configurate nella tabella Ricerca Sconti.