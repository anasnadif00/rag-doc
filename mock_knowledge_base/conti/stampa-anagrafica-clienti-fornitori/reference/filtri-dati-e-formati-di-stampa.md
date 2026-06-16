---
title: Filtri, dati e formati di stampa di Stampa anagrafica clienti/fornitori
doc_kind: reference
domain: conti
feature: stampa-anagrafica-clienti-fornitori
keywords:
  - stampa anagrafica clienti fornitori
  - anagrafica clienti fornitori
  - conti stampa anagrafica clienti fornitori
  - filtri anagrafica clienti fornitori
  - selezione conti
  - selezione obsoleti
  - ordinamento
  - dati da stampare
  - clienti
  - fornitori
  - percipienti
  - categoria amministrativa
  - categoria commerciale
  - tipo listino
  - contatti
  - dati fiscali
  - dati commerciali
  - dati bancari
task_tags:
  - riferimento filtri stampa anagrafica clienti fornitori
  - riferimento dati da stampare anagrafica clienti fornitori
  - riferimento formati stampa anagrafica clienti fornitori
erp_versions:
  - v.1.0
role_scope:
  - operatore
review_status: approved
module: Conti
submenu: Stampa
screen_title: Stampa anagrafica clienti/fornitori
aliases:
  - conti-stampa-stampa anagrafica clienti fornitori
  - anagrafica clienti fornitori
field_labels:
  - Conto
  - Agente
  - Zona
  - Tipo listino
  - Categoria amministrativa
  - Categoria commerciale
  - Selezione conti
  - Ordinamento
  - Dati da stampare
  - Obsoleto
---
# Filtri, dati e formati di stampa di Stampa anagrafica clienti/fornitori

All'interno del menu **Stampa** della gestione **Conti** è presente l'applicazione **Stampa anagrafica clienti/fornitori**, attraverso la quale è possibile stampare le voci del piano dei conti identificate come clienti e/o fornitori selezionandole mediante appositi filtri.

## Campi
### Conto
Consente di impostare un intervallo di selezione da un valore iniziale a un valore finale sul campo **Conto**.

### Agente
Consente di impostare un intervallo di selezione da un valore iniziale a un valore finale sul campo **Agente**.

### Zona
Consente di impostare un intervallo di selezione da un valore iniziale a un valore finale sul campo **Zona**.

### Tipo listino
Consente di impostare un intervallo di selezione da un valore iniziale a un valore finale sul campo **Tipo listino**.

### Categoria amministrativa
Consente di impostare un intervallo di selezione da un valore iniziale a un valore finale sul campo **Categoria amministrativa**.

### Categoria commerciale
Consente di impostare un intervallo di selezione da un valore iniziale a un valore finale sul campo **Categoria commerciale**.

### Selezione conti
Il campo **Selezione conti** consente di discriminare il tipo di conti da estrarre nella stampa.

Le opzioni disponibili sono:
- tutti
- clienti
- fornitori
- percipienti

### Obsoleto
La procedura prevede due tipologie di filtro **Obsoleto**.

La prima tipologia di filtro presenta le opzioni:
- tutti
- escludi obsoleti
- solo obsoleti

Questo filtro serve per chi utilizza l'impostazione dell'obsoleto dalle **categorie amministrative** associate al conto.

La seconda tipologia di filtro presenta le opzioni:
- tutti
- si
- no
- blocca inserimento

Questo filtro serve per chi utilizza l'impostazione dell'obsoleto direttamente dall'**anagrafica del conto**.

### Ordinamento
Il campo **Ordinamento** consente di ordinare il risultato della stampa secondo uno dei criteri disponibili.

Le opzioni disponibili sono:
- codice
- ragione sociale

### Dati da stampare
Il riquadro **Dati da stampare** consente di selezionare quali informazioni includere nel PDF o nel file Excel.

È possibile selezionare **tutto** oppure, in alternativa, scegliere singolarmente i gruppi di dati in base alla suddivisione presente nella maschera dell'anagrafica conti.

I gruppi selezionabili sono:
- dati anagrafici
- dati commerciali
- dati bancari
- dati fiscali
- note
- attributi
- clienti di fatturazione e spedizione e luoghi di destinazione
- contatti

## Regole
### Ambito della stampa
La stampa è dedicata alle voci del piano dei conti identificate come clienti e/o fornitori.

### Filtri disponibili
La procedura mette a disposizione filtri di selezione per:
- intervallo conto
- intervallo agente
- intervallo zona
- intervallo tipo listino
- intervallo categoria amministrativa
- intervallo categoria commerciale
- selezione della tipologia di conto
- selezione dello stato obsoleto
- criterio di ordinamento

### Gestione del filtro obsoleto
Sono previsti due diversi criteri di filtro dell'obsoleto, da utilizzare in funzione della modalità adottata dall'installazione:
- obsoleto derivato dalla categoria amministrativa associata al conto
- obsoleto gestito direttamente nell'anagrafica del conto

### Selezione dei dati in stampa
Il riquadro **Dati da stampare** consente di produrre una stampa completa oppure una stampa limitata a specifici gruppi informativi dell'anagrafica conti.

### Formati di stampa disponibili
Sono disponibili due formati di stampa:
- **Anagrafica clienti/fornitori** con output **PDF**
- **Anagrafica clienti/fornitori Excel** con output **Excel**