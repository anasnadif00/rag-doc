---
title: Pannello Ritenute del corpo della Contabilità Generale
doc_kind: reference
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - pannello ritenute
  - percipienti
  - chiusura partite
  - compensi
  - contributi
  - selezione compensi
task_tags:
  - riferimento pannello ritenute contabilità generale
  - gestione ritenute su partite
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Contabilità Generale
tab_name: Ritenute
field_labels:
  - Selezione
---
# Pannello Ritenute del corpo della Contabilità Generale

Il pannello Ritenute contiene i dati relativi alle ritenute e ai contributi collegati a una partita.

## Regole
### Condizioni di attivazione
Il pannello si attiva solo se il Tipo documento utilizzato ha:
- Natura documento impostata a Chiusura partite
- parametro Percipienti impostato a Ritenuta

### Compilazione automatica
Nel caso in cui si stia pagando una partita per la quale è stato registrato un compenso, la compilazione del pannello avviene automaticamente riprendendo la partita nel pannello Partite.

L'operatore interviene quindi principalmente per modificare i dati già ripresi.

### Struttura del pannello
La maschera è strutturata come il pannello Compenso di testata del movimento.

### Pulsante Selezione
Il pannello contiene in più il pulsante Selezione, che apre un help sui compensi precedentemente registrati da abbinare alla registrazione corrente.