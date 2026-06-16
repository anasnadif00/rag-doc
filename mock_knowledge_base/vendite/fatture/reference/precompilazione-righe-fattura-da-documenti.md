---
title: Precompilazione righe fattura da ordini e DDT
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - precompilazione righe fattura
  - fattura da ordine
  - fattura da ddt
  - fattura accompagnatoria
  - fattura differita
task_tags:
  - riferimento precompilazione righe fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
field_labels:
  - Ordine
  - DDT
  - Articolo
  - Quantità
  - Prezzo
---
# Precompilazione righe fattura da ordini e DDT

## Regole

### Fattura ripresa da ordini
Quando la fattura viene generata tramite ripresa da ordini, le righe articolo vengono precompilate in base al contenuto degli ordini selezionati.

### Fattura ripresa da DDT
Quando la fattura viene generata da DDT valorizzati, le righe articolo vengono precompilate in base ai DDT richiamati.

### Fattura accompagnatoria
Nel caso di fattura accompagnatoria è possibile riprendere gli ordini del cliente dalla testata della fattura.

### Fattura differita
Nel caso di fattura differita si utilizza la funzione di valorizzazione DDT.

### Inserimento manuale
Se non si riprendono ordini o DDT, le righe articolo devono essere inserite manualmente tramite il pulsante "+" verde.