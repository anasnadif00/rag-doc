---
title: Forme di pagamento
doc_kind: reference
domain: contabilita
feature: forme-pagamento
keywords:
  - forme di pagamento
  - forma di pagamento
  - scadenze partite
  - codifica pagamento
  - ricevuta
  - tratta
  - paghero
  - bonifico
  - contanti
  - descrizione lingua
task_tags:
  - riferimento forme di pagamento
  - configurazione forme di pagamento
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Tabelle
screen_title: Forme di pagamento
aliases:
  - tabella forme di pagamento
field_labels:
  - Codice
  - Descrizione
  - Tipologia
  - Iscrizioni in lingua
---
# Forme di pagamento

## Campi
### Codice
Il codice univoco della forma di pagamento è rappresentato da un carattere.

### Descrizione
Descrizione della forma di pagamento.

### Tipologia
Per ogni forma di pagamento è necessario indicare la tipologia.

Le tipologie previste sono:
- ricevuta
- tratta
- pagherò
- altro

### Iscrizioni in lingua
Attraverso l'apposito pannello di iscrizioni in lingua è possibile definire la descrizione nella lingua in cui deve essere stampata l'eventuale fattura oppure l'eventuale effetto o bonifico.

## Regole
### Obbligatorietà della tipologia
Ad ogni forma di pagamento deve essere sempre associata una tipologia.

### Significato della tipologia Altro
La tipologia Altro può essere utilizzata per forme di pagamento quali bonifico, contanti ed eventuali altre modalità non riconducibili a ricevuta, tratta o pagherò.
