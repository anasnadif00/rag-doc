---
title: Campi e blocchi della tabella Categorie Amministrative
doc_kind: reference
domain: configurazione
feature: categorie-amministrative
keywords:
  - tabella categorie amministrative
  - categoria amministrativa
  - codice categoria amministrativa
  - descrizione categoria amministrativa
  - blocco inserimento offerte
  - offerte bloccate
  - blocco inserimento ordini
  - ordini bloccati
  - blocco flusso spedizione
  - blocco inserimento ddt
  - obsoleta
task_tags:
  - riferimento campi categorie amministrative
  - configurazione blocchi amministrativi
erp_versions:
  - v.1.0
role_scope:
  - admin
review_status: approved
module: Tabelle
screen_title: Categorie Amministrative
field_labels:
  - Codice
  - Descrizione
  - Obsoleta
  - Blocco inserimento offerte
  - Offerte bloccate
  - Blocco inserimento ordini
  - Ordini bloccati
  - Blocco flusso spedizione
  - Blocco inserimento DDT
---
# Campi e blocchi della tabella Categorie Amministrative

## Campi
### Codice
Contiene il codice univoco della Categoria Amministrativa. Il codice è composto da al massimo tre caratteri.

### Descrizione
Contiene la descrizione della Categoria Amministrativa.

### Obsoleta
Indica una categoria amministrativa non più in uso.

### Blocco inserimento offerte
Impedisce l'inserimento delle offerte per i clienti che hanno associata questa categoria amministrativa.

### Offerte bloccate
Consente il caricamento delle offerte per i clienti che hanno associata questa categoria amministrativa in stato bloccato.

### Blocco inserimento ordini
Impedisce il caricamento degli ordini per i clienti che hanno associata questa categoria amministrativa.

### Ordini bloccati
Consente l'inserimento di un ordine per i clienti che hanno associata questa categoria amministrativa in stato bloccato.

### Blocco flusso spedizione
Impedisce il caricamento dei documenti relativi ai flussi di spedizione per i clienti che hanno associata questa categoria amministrativa.

### Blocco inserimento DDT
Impedisce l'inserimento dei documenti di trasporto per i clienti che hanno impostata questa categoria amministrativa.

## Regole
### Unicità del codice
Ogni Categoria Amministrativa deve essere identificata da un codice univoco di al massimo tre caratteri.

### Gestione dei blocchi amministrativi
Per ogni categoria amministrativa codificata nel sistema è possibile impostare una o più tipologie di blocco amministrativo.

### Combinazione dei blocchi
Possono essere impostati più blocchi per ogni singola Categoria Amministrativa.