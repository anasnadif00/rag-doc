---
title: Gestione quantità e unità di misura nelle righe fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - quantità fattura
  - unità misura vendita
  - unità misura prezzo
  - quantità gestionale
  - colli
task_tags:
  - riferimento quantità fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
field_labels:
  - Quantità
  - Quantità vendita
  - Quantità prezzo
  - Quantità gestionale
  - Colli
---
# Gestione quantità e unità di misura nelle righe fattura

## Campi

### Quantità gestionale
Rappresenta l'unità di misura principale dell'articolo ed è quella utilizzata per la movimentazione di magazzino.

È la quantità obbligatoria della riga.

### Quantità vendita
Rappresenta l'unità di misura utilizzata dal cliente.

Viene proposta in base all'unità di misura di vendita definita nell'anagrafica articolo.

### Quantità prezzo
Rappresenta l'unità di misura a cui è riferito il prezzo e il listino.

Viene proposta in base all'unità di misura prezzo definita nell'anagrafica articolo.

### Colli
Permette di indicare il numero dei colli associati alla riga.

## Regole

### Proposta delle unità di misura
Se non sono definite unità specifiche:

- quantità vendita
- quantità prezzo

vengono proposte uguali all'unità di misura gestionale.

### Conversioni automatiche
Le quantità vengono convertite automaticamente utilizzando i fattori di conversione definiti nell'anagrafica articolo.

### Aggiornamento delle quantità
Indicando:

- quantità vendita
- quantità prezzo

viene calcolata automaticamente la quantità gestionale.

Indicando la quantità gestionale vengono aggiornate automaticamente le altre quantità in base alle conversioni disponibili.

### Quantità sincronizzate
Se nell'anagrafica articolo è attiva l'opzione "Quantità sincronizzate", la modifica di una quantità aggiorna automaticamente tutte le altre.

### Gestione colli
All'inserimento o modifica del numero colli viene proposta la quantità gestionale quando:

- la quantità non è già valorizzata
- nei dati tecnici dell'articolo sono presenti impostazioni collegate ai colli