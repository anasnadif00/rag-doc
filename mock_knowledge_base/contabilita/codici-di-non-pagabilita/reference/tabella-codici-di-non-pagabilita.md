---
title: Tabella Codici di non pagabilità
doc_kind: reference
domain: contabilita
feature: codici-di-non-pagabilita
keywords:
  - codici di non pagabilità
  - causali di non pagabilità
  - blocco pagabilità
  - non sollecitabile
  - partite fornitori
  - partite clienti
  - solleciti
task_tags:
  - riferimento codici di non pagabilità
  - configurazione blocco partite
  - configurazione solleciti
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
screen_title: Codici di non pagabilità
aliases:
  - causali di non pagabilità
field_labels:
  - Codice
  - Descrizione
  - Blocco pagabilità
  - Non sollecitabile
  - Note
---
# Tabella Codici di non pagabilità

La tabella Codici di non pagabilità consente di codificare una lista di causali associabili alle singole partite.

## Campi
### Codice
Campo identificativo univoco della causale.

Può contenere al massimo 2 caratteri.

### Descrizione
Descrizione della causale di non pagabilità o di non sollecitabilità.

### Blocco pagabilità
Se attivato, le elaborazioni di chiusura delle partite non rilevano la scadenza.

### Non sollecitabile
Se attivato, l'elaborazione di emissione dei solleciti non rileva la scadenza.

### Note
Campo contenente note aggiuntive rispetto alla descrizione.

## Regole
### Associazione alle partite fornitori
Per le scadenze relative ai fornitori, il codice può essere utilizzato per impostare un blocco sulla pagabilità.

In questo caso le partite non vengono proposte in contabilità e nel modulo Pagamenti fornitori per poter essere chiuse.

### Associazione alle partite clienti
Per le scadenze relative ai clienti, il codice può essere utilizzato per impostare un'inibizione sulla sollecitabilità.

In questo caso le partite non vengono proposte nel modulo Solleciti per essere elaborate.

### Funzione della tabella
La tabella raccoglie quindi le causali che consentono di escludere selettivamente una partita:
- dalla chiusura per pagabilità
- dall'elaborazione dei solleciti