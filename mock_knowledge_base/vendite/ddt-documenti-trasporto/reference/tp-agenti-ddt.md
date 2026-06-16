---
title: TP Agenti del DDT
doc_kind: reference
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - TP Agenti DDT
  - agente DDT
  - capo area DDT
  - provvigione DDT
  - ricerca provvigioni
task_tags:
  - riferimento TP Agenti DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Agenti
aliases:
  - agenti bolla
  - provvigioni DDT
field_labels:
  - Agente
  - Capo area
  - Percentuale provvigione
---
# TP Agenti del DDT

## Campi

### Agente
Viene proposto l'agente presente nel TP Dati commerciali dell'anagrafica conti per il cliente intestatario del DDT.

### Capo area
Il capo area viene proposto in relazione all'agente e alle impostazioni commerciali previste.

### Percentuale provvigione
La percentuale di provvigione viene ripresa in funzione delle impostazioni della tabella Ricerca/provvigioni.

## Regole

### Origine dell'agente
L'agente proposto nel DDT deriva dall'anagrafica conti del cliente intestatario.

### Ricerca provvigioni
La percentuale di provvigione viene determinata in base alle impostazioni presenti nella tabella Ricerca/provvigioni.
