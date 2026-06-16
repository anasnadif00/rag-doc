---
title: Campi della tabella Attività IVA
doc_kind: reference
domain: contabilita
feature: attivita-iva
keywords:
  - attività IVA
  - attivita iva
  - codice attività IVA
  - descrizione attività IVA
  - comunicazioni liquidazioni periodiche IVA
task_tags:
  - riferimento attività iva
  - configurazione attività iva
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità
screen_title: Attività IVA
aliases:
  - tabella Attività IVA
field_labels:
  - Codice
  - Descrizione
  - Comunicazioni liquidazioni periodiche IVA
---
# Campi della tabella Attività IVA

La tabella **Attività IVA** contiene la lista delle codifiche delle diverse attività IVA relative all'azienda.

La separazione delle attività IVA permette a un soggetto con un'unica partita IVA di gestire la contabilità di più attività in modo autonomo.

La gestione separata consente di calcolare l'IVA a debito o a credito distintamente per ciascuna attività, evitando limitazioni sulla detrazione dell'imposta, come il pro-rata.

## Campi

### Codice
Identifica in modo univoco l'attività IVA.

Il codice può essere composto da un massimo di 3 caratteri.

### Descrizione
Consente di inserire la descrizione dell'attività IVA.

### Comunicazioni liquidazioni periodiche IVA
Se impostato, permette a tutte le operazioni relative all'attività di rientrare nella comunicazione liquidazione periodica IVA.

## Regole

### Unicità del codice
Ogni attività IVA deve essere identificata da un codice univoco.

### Lunghezza massima del codice
Il codice dell'attività IVA può contenere al massimo 3 caratteri.

### Finalità della separazione per attività
La separazione delle attività IVA consente di gestire in modo autonomo più attività riferite alla stessa partita IVA e di calcolare distintamente l'IVA per ciascuna attività.