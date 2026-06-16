---
title: TP Trasporti del DDT
doc_kind: reference
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - TP Trasporti DDT
  - trasporto DDT
  - vettore DDT
  - note vettore DDT
  - cura trasporto
task_tags:
  - riferimento TP Trasporti DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - magazzino
  - amministrazione vendite
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Trasporti
aliases:
  - trasporti bolla
  - vettore bolla
field_labels:
  - Trasporto
  - Vettore
  - Note
---
# TP Trasporti del DDT

## Campi

### Trasporto
Il TP Trasporti contiene le informazioni relative al trasporto, compresa l'indicazione di chi effettua il trasporto.

### Vettore
Se nel TP Dati commerciali dell'anagrafica conti è stato impostato il vettore, il campo relativo viene automaticamente flaggato e viene proposto il vettore.

Il vettore proposto può essere modificato.

### Note
Se al vettore sono associate note, queste vengono riprese automaticamente nel TP Note.

Le note possono essere modificate.

## Regole

### Origine dei dati di trasporto
I dati di trasporto possono essere riportati dal TP Dati commerciali dell'anagrafica conti.

### Modifica o cancellazione del vettore
Se viene modificato il codice vettore, le note vengono sostituite con quelle associate al nuovo vettore.

Se viene cancellato il codice vettore, vengono cancellate anche le note associate.