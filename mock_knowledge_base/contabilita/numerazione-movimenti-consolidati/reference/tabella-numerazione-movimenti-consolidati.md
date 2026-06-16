---
title: Tabella Numerazione movimenti consolidati
doc_kind: reference
domain: contabilita
feature: numerazione-movimenti-consolidati
keywords:
  - numerazione movimenti consolidati
  - numerazione annuale movimenti consolidati
  - versioni di contabilità
  - consolidamento movimenti
  - ultimo numero annuale consolidato
  - esercizio infrannuale
  - civilistico
  - internazionale
  - ifrs
task_tags:
  - riferimento tabella
  - configurazione contabilita
  - consolidamento movimenti
  - gestione bilancio ifrs
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
screen_title: Numerazione movimenti consolidati
aliases:
  - numerazione movimenti consolidati
field_labels:
  - numerazione annuale movimenti consolidati
  - ultimo numero annuale consolidato
  - anno
  - tipo destinazione contabile
---
# Tabella Numerazione movimenti consolidati

La tabella Numerazione movimenti consolidati contiene l'indicazione dell'ultimo numero annuale consolidato memorizzato attraverso la funzione Consolidamento movimenti.

## Campi

### Ultimo numero annuale consolidato
Contiene l'ultimo numero annuale consolidato registrato dalla funzione Consolidamento movimenti.

### Anno
Indica l'anno a cui si riferisce la numerazione annuale dei movimenti consolidati.

Nel caso di esercizio infrannuale, l'anno indicato è quello di inizio esercizio.

### Tipo destinazione contabile
Identifica l'ambito di numerazione dei movimenti consolidati.

La numerazione è separata tra:
- Civilistico
- Internazionale

Questa distinzione è utilizzata per la gestione del bilancio IFRS.

## Regole

### Condizione di utilizzo
La tabella viene utilizzata se nella tabella Versioni di contabilità è attivato il flag numerazione annuale movimenti consolidati.

### Aggiornamento della numerazione
L'ultimo numero annuale consolidato viene memorizzato attraverso la funzione Consolidamento movimenti.

### Gestione degli esercizi infrannuali
Se l'esercizio è infrannuale, l'anno memorizzato nella tabella è quello di inizio esercizio e non quello di chiusura.

### Separazione della numerazione per destinazione contabile
La numerazione dei movimenti consolidati è gestita separatamente per il tipo destinazione contabile Civilistico e Internazionale.

Questa separazione consente la gestione distinta della numerazione nell'ambito del bilancio IFRS.