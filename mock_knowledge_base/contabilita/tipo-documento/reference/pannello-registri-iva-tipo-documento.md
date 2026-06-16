---
title: Pannello Registri IVA della tabella Tipo documento
doc_kind: reference
domain: contabilita
feature: tipo-documento
keywords:
  - tipo documento
  - registri IVA
  - pannello registri IVA
  - conto IVA
  - split payment
  - registro SDI
  - fatture di fine anno
task_tags:
  - riferimento registri iva tipo documento
  - configurazione registri iva tipo documento
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità
screen_title: Tipo documento
tab_name: Registri IVA
aliases:
  - registri IVA tipo documento
field_labels:
  - Conto IVA
  - Registro IVA
  - Conto IVA split payment
  - Registro SDI per le fatture di fine anno
---
# Pannello Registri IVA della tabella Tipo documento

Il pannello **Registri IVA** della tabella **Tipo documento** consente di indicare, per ogni società gestita, i dati IVA da utilizzare nella registrazione.

## Campi

### Conto IVA
Indica il conto dell'IVA da utilizzare nella registrazione.

### Registro IVA
Indica il registro IVA da utilizzare nella registrazione.

### Conto IVA split payment
Indica il conto dell'IVA da utilizzare per la gestione dello split payment.

### Registro SDI per le fatture di fine anno
Indica il registro SDI da utilizzare per le fatture di fine anno.

## Regole

### Gestione per società
I dati del pannello **Registri IVA** vengono configurati per ogni società gestita.

### Attivazione del pannello
Il pannello **Registri IVA** si attiva solo se il campo **Tipo IVA** del tipo documento è impostato con un valore diverso da **Non gestito**.

### Utilizzo nella registrazione
I valori configurati nel pannello vengono utilizzati nella registrazione del movimento contabile per determinare i conti e i registri IVA associati al tipo documento.