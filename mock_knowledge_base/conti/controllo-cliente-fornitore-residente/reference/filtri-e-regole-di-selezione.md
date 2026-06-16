---
title: Filtri e regole di selezione di Controllo cliente fornitore residente
doc_kind: reference
domain: conti
feature: controllo-cliente-fornitore-residente
keywords:
  - controllo cliente fornitore residente
  - controllo residente
  - clienti fornitori residenti
  - elaborazioni conti
  - filtro residente
  - filtro stato
  - filtro cliente
  - filtro fornitore
  - nazione
  - residenza
  - italia
  - estero
task_tags:
  - riferimento filtri controllo cliente fornitore residente
  - riferimento regole controllo cliente fornitore residente
  - controllo clienti fornitori residenti
erp_versions:
  - v.1.0
role_scope:
  - operatore
review_status: approved
module: Conti
submenu: Elaborazioni
screen_title: Controllo cliente fornitore residente
aliases:
  - conti-elaborazioni-controllo cliente fornitore residente
  - controllo cliente fornitore residente
field_labels:
  - Conto
  - Cliente
  - Fornitore
  - Residente
  - Stato
---
# Filtri e regole di selezione di Controllo cliente fornitore residente

All'interno del menu **Elaborazioni** della gestione **Conti** è presente l'applicazione **Controllo cliente fornitore residente**. La procedura è una stampa che consente di controllare e visualizzare, per tutti i clienti e i fornitori, le impostazioni registrate all'interno di Magia relative alla nazione e alla residenza.

## Campi
### Conto
Consente di impostare un intervallo di selezione da un valore iniziale a un valore finale sul campo **Conto**.

### Cliente
Il filtro **Cliente** consente di discriminare i conti in base all'impostazione cliente.

Le opzioni disponibili sono:
- tutti
- sì
- no

### Fornitore
Il filtro **Fornitore** consente di discriminare i conti in base all'impostazione fornitore.

Le opzioni disponibili sono:
- tutti
- sì
- no

### Residente
Il filtro **Residente** consente di discriminare i conti in base all'impostazione residente.

L'impostazione **Residente** è presente nel pannello **Dati fiscali** della gestione dei conti per i percipienti.

Le opzioni disponibili sono:
- tutti
- sì
- no

### Stato
Il filtro **Stato** consente di discriminare i conti in base alla classificazione Italia o estero.

Le opzioni disponibili sono:
- tutti
- Italia
- estero

## Regole
### Ambito della procedura
La procedura consente di controllare e visualizzare le impostazioni relative a nazione e residenza registrate per clienti e fornitori.

### Filtri disponibili
La stampa mette a disposizione i seguenti filtri:
- intervallo conto
- impostazione cliente
- impostazione fornitore
- impostazione residente
- classificazione dello stato

### Regola di classificazione Italia
Per **Italia** si intendono tutti i clienti e i fornitori che:
- non hanno una nazione impostata in anagrafica nel pannello **Dati commerciali**
- oppure hanno una nazione impostata con codice **ISO2** pari a **IT**

### Regola di classificazione estero
Per **estero** si intendono i clienti e i fornitori che hanno una nazione impostata in anagrafica nel pannello **Dati commerciali** con codice **ISO2** diverso da **IT**.