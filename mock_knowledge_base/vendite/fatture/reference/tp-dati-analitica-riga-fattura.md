---
title: TP Dati Analitica della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - tp dati analitica fattura
  - contabilità analitica
  - competenza da a
  - ratei risconti
  - dati coin
  - commessa
  - centro di costo
task_tags:
  - riferimento analitica riga fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
  - amministrazione
review_status: approved
module: Fatture
tab_name: TP Dati Analitica
field_labels:
  - Competenza da
  - Competenza a
  - Commessa
  - Centro di costo
---
# TP Dati Analitica della riga fattura

## Campi

### Competenza da
Indica l'inizio del periodo di competenza della riga.

### Competenza a
Indica la fine del periodo di competenza della riga.

### Dati COIN
Se nella tabella tipo fattura di vendita è impostato il tipo dati COIN, vengono attivati i campi collegati alle destinazioni previste.

### Commessa
Campo disponibile se previsto dalle destinazioni configurate.

### Centro di costo
Campo disponibile se previsto dalle destinazioni configurate.

## Regole

### Contabilità analitica
Il TP Dati Analitica consente di inserire e gestire le informazioni di contabilità analitica.

Queste informazioni vengono riprese nei passaggi successivi:
- contabilizzazione
- ripresa in contabilità analitica dei dati fattura

### Ratei e risconti
I campi competenza da e competenza a permettono di determinare la quota di competenza del periodo per eventuali ratei e risconti.

### Attivazione campi COIN
Quando è impostato il tipo dati COIN nella tabella tipo fattura di vendita, si attivano tanti campi quante sono le destinazioni indicate nella tabella, inclusi eventuale commessa e centro di costo.