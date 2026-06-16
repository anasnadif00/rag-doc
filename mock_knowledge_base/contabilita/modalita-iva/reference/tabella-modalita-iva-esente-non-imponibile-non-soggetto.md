---
title: Tabella Modalità IVA esente, non imponibile, non soggetto
doc_kind: reference
domain: contabilita
feature: modalita-iva
keywords:
  - modalità iva esente
  - modalità iva non imponibile
  - modalità iva non soggetto
  - elenco clienti fornitori
  - blacklist
  - esente
task_tags:
  - riferimento modalità iva
  - configurazione iva
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
screen_title: Modalità IVA esente, non imponibile, non soggetto
aliases:
  - modalità iva esente non imponibile non soggetto
field_labels:
  - Non Imponibile
  - Esente
  - Non Soggetto
  - Esente
---
# Tabella Modalità IVA esente, non imponibile, non soggetto

La tabella Modalità IVA esente, non imponibile, non soggetto viene utilizzata per associare una classificazione alle modalità IVA definite nella relativa tabella.

## Campi

### Classificazione
La tabella consente di assegnare uno dei seguenti valori alla modalità IVA:
- Non Imponibile
- Esente
- Non Soggetto

### Modalità IVA collegata
La classificazione viene associata alle modalità IVA definite nella relativa tabella Modalità IVA.

## Regole

### Modalità IVA selezionabili
Possono essere classificate in questa tabella solo le modalità IVA che nella relativa tabella hanno attivato il parametro Esente.

### Utilizzo nelle elaborazioni
L'impostazione della tabella è necessaria ai fini delle seguenti elaborazioni:
- Stampa elenco clienti fornitori
- Generazione elenco clienti fornitori
- Elaborazioni relative agli adempimenti black list
- Stampe relative agli adempimenti black list

### Finalità della classificazione
La tabella permette di distinguere, per le elaborazioni che la utilizzano, se una modalità IVA deve essere considerata come Non Imponibile, Esente oppure Non Soggetto.