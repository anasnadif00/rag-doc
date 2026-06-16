---
title: TP Trasporto del DDT
doc_kind: reference
domain: logistica
feature: ddt
keywords:
  - tp trasporto ddt
  - trasporto ddt
  - vettore ddt
  - note vettore
  - dati commerciali cliente
task_tags:
  - riferimento trasporto ddt
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - logistica
  - amministrazione vendite
review_status: approved
module: DDT
tab_name: TP Trasporto
field_labels:
  - Trasporto
  - Vettore
  - Note
---
# TP Trasporto del DDT

## Campi

### Trasporto
Contiene le informazioni relative al trasporto e a cura di chi viene effettuato.

### Vettore
Se nei dati commerciali dell'anagrafica conti è impostato un vettore, il campo viene proposto automaticamente.

## Regole

### Origine dati trasporto
Le informazioni del TP Trasporto vengono riportate dal TP Dati Commerciali dell'anagrafica conti, se presenti.

### Proposta vettore
Se è impostato il vettore:
- viene automaticamente attivato il relativo flag
- viene proposto il vettore
- il vettore resta modificabile

### Note vettore
Se al vettore sono associate note, queste vengono riprese automaticamente nel TP Note.

### Modifica vettore
Se il codice vettore viene modificato o cancellato:
- le note vengono sostituite con quelle del nuovo vettore
- oppure vengono cancellate se il vettore viene rimosso
