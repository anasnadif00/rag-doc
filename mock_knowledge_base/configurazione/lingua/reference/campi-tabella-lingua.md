---
title: Campi della tabella Lingua
doc_kind: reference
domain: configurazione
feature: lingua
keywords:
  - tabella lingua
  - idiomi
  - lingue
  - codice lingua
  - descrizione lingua
  - nazione country
  - decodifiche in lingua
task_tags:
  - riferimento campi lingua
  - configurazione lingue
erp_versions:
  - v.1.0
role_scope:
  - admin
review_status: approved
module: Tabelle
screen_title: Lingua
field_labels:
  - Codice
  - Descrizione
  - Lingua
  - Nazione/Country
---
# Campi della tabella Lingua

## Campi
### Codice
Contiene il codice univoco della lingua. Il codice è composto da massimo tre caratteri.

### Descrizione
Contiene la descrizione dell'idioma utilizzato in Magia.

### Lingua
Contiene l'identificativo utilizzato per le decodifiche automatiche in lingua nelle descrizioni gestite in Magia.

### Nazione/Country
Contiene l'identificativo utilizzato insieme al campo Lingua per le decodifiche automatiche nelle descrizioni in lingue diverse da quella di gestione.

## Regole
### Utilizzo per le descrizioni multilingua
I campi Lingua e Nazione/Country servono per gestire le decodifiche automatiche delle descrizioni in lingue diverse da quella di gestione all'interno di Magia.

### Unicità del codice
Ogni lingua deve essere identificata da un codice univoco di al massimo tre caratteri.