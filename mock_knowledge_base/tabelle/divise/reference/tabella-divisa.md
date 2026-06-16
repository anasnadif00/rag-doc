---
title: Tabella divisa
doc_kind: reference
domain: tabelle
feature: divise
keywords:
  - tabella divisa
  - divisa
  - valuta
  - cambio euro
  - cambio lire
  - codice ISO
  - divisa giornaliera
task_tags:
  - riferimento campi divisa
  - gestione valute
  - gestione cambi
erp_versions:
  - v.1.0
role_scope:
  - amministrazione
  - contabilità
review_status: approved
screen_title: Tabella divisa
aliases:
  - tabella valute
  - elenco valute
field_labels:
  - Codice
  - Descrizione
  - Euro
  - Area UEM
  - Cambio euro
  - Decimali
  - Lire
  - Cambio lire
  - Decimali interni
  - Decimali calcolo sconto
  - Codice ISO
  - Divisa giornaliera
---
# Tabella divisa

La tabella divisa contiene l'elenco di tutte le valute gestite all'interno del gestionale Magia.

## Campi
### Codice
Campo di 5 caratteri che identifica univocamente la valuta.

### Descrizione
Contiene la descrizione della valuta.

### Euro
Se impostato, identifica univocamente l'Euro.

### Area UEM
Identifica le valute relative all'area dell'Unione Economica Monetaria.

### Cambio euro
Contiene il cambio della valuta rispetto all'Euro.

### Decimali
Contiene il numero di decimali gestiti in Magia per la valuta.

### Lire
È impostato per la valuta corrispondente alle vecchie Lire.

### Cambio lire
Contiene il cambio della valuta rispetto alle Lire.

### Decimali interni
Contiene il numero di decimali interni gestiti.

### Decimali calcolo sconto
Contiene il numero di decimali gestiti per il calcolo degli sconti.

### Codice ISO
Contiene il codice univoco ISO della valuta.

## Regole
### Identificazione dell'euro
Il flag Euro identifica in modo univoco l'euro in moneta circolante.

### Gestione area UEM
Il flag Area UEM viene utilizzato per identificare le valute appartenenti all'area dell'Unione Economica Monetaria.

### Gestione lire
Il flag Lire viene utilizzato per la valuta corrispondente alle vecchie lire.

### Gestione dei decimali
I campi Decimali, Decimali interni e Decimali calcolo sconto regolano il numero di decimali utilizzati rispettivamente nella gestione della valuta, nei calcoli interni e nel calcolo degli sconti.

### Pannello Divisa giornaliera
Nel pannello Divisa giornaliera è possibile inserire il valore del cambio a partire da una certa data.

L'inserimento del cambio può avvenire:
- manualmente
- automaticamente tramite un'applicazione apposita di Magia