---
title: Campi del tab TP Dati di analitica dell'offerta
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - tp dati di analitica offerta
  - analitica offerta
  - data competenza offerta
  - commessa offerta
  - centro di costo offerta
  - tipo offerte di vendita
task_tags:
  - riferimento analitica offerta
erp_versions:
  - v.1.0
role_scope:
  - sales
  - accounting
review_status: approved
module: Offerte
screen_title: Offerte
tab_name: TP Dati di analitica
field_labels:
  - Da data
  - A data
  - Commessa
  - Centro di costo
---
# Campi del tab TP Dati di analitica dell'offerta

## Campi

### Da data
Campo utilizzato per determinare la quota di competenza del periodo.

### A data
Campo utilizzato per determinare la quota di competenza del periodo.

### Commessa
Identifica la commessa di riferimento da associare all'offerta.

### Centro di costo
Consente di identificare il centro di costo, se previsto dalla configurazione analitica adottata.

## Regole

### Ripresa nei documenti successivi
Le informazioni di contabilità analitica inserite nell'offerta vengono poi riportate automaticamente nei passaggi successivi, come ordine, eventuale DDT, fatturazione e contabilizzazione.

### Campi attivi nella configurazione standard
Nell'impostazione standard risultano sempre attivi i campi **Da data**, **A data** e il riferimento di **Commessa** o **Centro di costo**.

### Configurazione avanzata dell'analitica
Se si vuole impostare un'analitica differente, con possibilità di riportare più valori, la configurazione deve essere effettuata in:
1. **TP Società/Divisione**;
2. tabella **Tipo offerte di vendita**.

In questa configurazione vanno inseriti i campi che si desidera riportare nell'analitica dell'offerta.