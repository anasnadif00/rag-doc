---
title: TP Dati agenti degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - TP Dati agenti
  - agente ordine cliente
  - capo area
  - provvigioni ordine
  - ricerca provvigioni
task_tags:
  - riferimento TP Dati agenti ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP Dati agenti
field_labels:
  - Agente
  - Capo area
  - Percentuale provvigione
  - Totale provvigioni
---
# TP Dati agenti degli Ordini clienti

## Campi

### Agente
Viene proposto l'agente presente nel tab dati commerciali dell'anagrafica del conto intestatario dell'ordine.

### Capo area
Se all'agente è collegato un capo area, questo viene ripreso come secondo agente.

### Percentuale provvigione
La percentuale di provvigione può essere inserita nel tab di testata e viene poi ripresa in tutte le righe articolo.

### Totale provvigioni
In testata viene riepilogato il totale delle provvigioni calcolate sulle righe.

## Regole

### Proposta automatica
L'agente viene ripreso dall'anagrafica commerciale del cliente intestatario dell'ordine.

### Calcolo delle provvigioni
Se la percentuale di provvigione non viene inserita in testata, gli importi vengono calcolati direttamente sulle righe articolo in base all'impostazione della tabella **Ricerca provvigioni**.

### Agenti aggiuntivi
Possono essere aggiunti altri agenti.

### Gestione percentuali
Le percentuali di provvigione degli agenti aggiuntivi possono essere imputate:
- manualmente nella testata
- manualmente nelle singole righe articolo