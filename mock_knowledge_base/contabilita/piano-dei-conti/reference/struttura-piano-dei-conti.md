---
title: Struttura del piano dei conti
doc_kind: reference
domain: contabilita
feature: piano-dei-conti
keywords:
  - piano dei conti
  - struttura conto
  - mastro
  - partitario
  - codice conto
  - conto
  - progressivo conto
task_tags:
  - riferimento struttura piano dei conti
  - classificazione conti
  - codifica conti
erp_versions:
  - v.1.0
role_scope:
  - amministrazione
  - contabilità
review_status: approved
module: Contabilita
screen_title: Conti
aliases:
  - struttura conti
  - codifica conti
field_labels:
  - Conto
  - Tipo conto
---
# Struttura del piano dei conti

Il piano dei conti in Magia è strutturato con codici numerici di 9 caratteri.

## Campi
### Conto
Il codice conto è formato da 9 caratteri numerici:
- i primi 5 caratteri sono relativi al mastro
- i 4 caratteri finali sono relativi al partitario

### Tipo conto
Identifica la tipologia del conto all'interno del piano dei conti.

## Regole
### Struttura del mastro
Il mastro può essere inteso come il capogruppo di una serie di conti successivi.

Un codice mastro ha:
- un valore nei primi 5 caratteri numerici
- gli ultimi 4 caratteri impostati a 0000

### Struttura del partitario
I conti di tipo partitario riportano:
- nei primi 5 caratteri il codice del mastro
- nei successivi 4 caratteri un progressivo numerico univoco

Il progressivo del partitario può essere:
- calcolato automaticamente da Magia
- digitato manualmente dall'operatore

### Applicazione di gestione
Il piano dei conti è gestito in Magia attraverso l'applicazione Conti.

L'applicazione Conti permette di gestire i dati strutturati nei seguenti pannelli:
- Dati anagrafici
- Dati pagamenti
- Dati fiscali
- Dati commerciali
- Dati storici e di inserimento
- Attributi
- Dati Magia90
- Clienti di fatturazione
- Clienti di spedizione
- Luoghi di destinazione
- Note
- Note commerciali clienti
- Contatto
- Dichiarazioni di intento o conti collegati
- Allegati
- Mail inviate
- Scheda