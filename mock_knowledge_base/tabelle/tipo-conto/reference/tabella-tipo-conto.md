---
title: Tabella Tipo_conto
doc_kind: reference
domain: tabelle
feature: tipo-conto
keywords:
  - tabella tipo_conto
  - tipo conto
  - tipi conto
  - piano dei conti
  - mastro
  - partitario
  - clienti
  - fornitori
  - partitario iva
  - effetti
task_tags:
  - riferimento tipi conto
  - classificazione conto
  - piano dei conti
erp_versions:
  - v.1.0
role_scope:
  - amministrazione
  - contabilità
review_status: approved
screen_title: Tabella Tipo_conto
aliases:
  - tabella tipo conto
  - tipi conto
field_labels:
  - Codice
  - Descrizione
---
# Tabella Tipo_conto

La tabella Tipo_conto contiene la lista delle tipologie che un codice del piano dei conti può assumere.

## Campi
### Codice
Identifica univocamente il tipo conto.

### Descrizione
Contiene la descrizione della tipologia associata al codice.

## Regole
### Tipi conto fissi
I tipi conto sono fissi.

### Elenco tipi conto disponibili
I tipi conto previsti sono i seguenti:

#### Codice 01
Mastro.

#### Codice 10
Partitario.

#### Codice 15
Clienti non gestiti a partite.

#### Codice 20
Clienti.

#### Codice 25
Fornitori non gestiti a partite.

#### Codice 30
Fornitori.

#### Codice 81
Effetti.

#### Codice 91
Partitario IVA.