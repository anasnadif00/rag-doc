---
title: TP Agenti della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - tp agenti fattura
  - provvigioni fattura
  - agente fattura
  - riduzione provvigione
  - provvigione calcolata
task_tags:
  - riferimento provvigioni riga fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Agenti
field_labels:
  - Numero
  - Codice agente
  - Nome agente
  - Importo provvigione
  - Percentuale
  - Riduzione
  - Provvigione calcolata
---
# TP Agenti della riga fattura

## Campi

### Numero
Indica il progressivo della riga provvigionale.

### Codice agente
Identifica l'agente collegato alla riga.

### Nome agente
Riporta il nome dell'agente.

### Importo provvigione
Indica l'importo su cui viene calcolata la provvigione.

### Percentuale
Indica la percentuale provvigionale applicata.

### Riduzione
Indica l'eventuale riduzione applicata alla provvigione.

### Provvigione calcolata
Indica la provvigione calcolata dal programma.

## Regole

### Origine delle provvigioni
Le provvigioni applicate sulla riga derivano dalle impostazioni presenti in:
- anagrafica cliente
- anagrafica articolo
- listini di vendita
- tabella ricerca provvigioni
- ricerca riduzioni provvigioni
- riduzione provvigione per pagamenti
- riduzione provvigioni per porto
- riduzione provvigioni per sconto
- Parametri del Commerciale

### Riepilogo sulla riga
Nel TP Agenti vengono riepilogate le provvigioni calcolate per la riga fattura.