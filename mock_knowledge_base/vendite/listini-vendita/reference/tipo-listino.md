---
title: Tipo listino
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - tipo listino
  - prezzi VAT
  - listino VAT
  - scorporo IVA
  - listini vendita
task_tags:
  - riferimento tipo listino
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
field_labels:
  - Codice
  - Descrizione
  - Prezzi VAT
---
# Tipo listino

## Campi

### Codice
Identifica la tipologia di listino da creare in Magia.

### Descrizione
Descrive la tipologia di listino.

### Prezzi ivati
Se il flag Prezzi ivati è attivato, il listino inserito viene considerato con prezzi ivati.

Nei documenti in cui il listino viene richiamato, il sistema effettua lo scorporo dell'IVA.

## Regole

### Codifica delle tipologie di listino
La tabella Tipo listino consente di codificare le tipologie di listino che si vogliono creare all'interno di Magia.

Ogni tipologia può essere identificata da un codice e da una descrizione.

### Listini con prezzi ivati
Quando il flag Prezzi ivati è attivo, i prezzi del listino sono trattati come comprensivi di IVA.

Il calcolo dello scorporo IVA viene effettuato nei documenti in cui il listino viene utilizzato.