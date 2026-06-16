---
title: TP Dati Analitica del DDT
doc_kind: reference
domain: logistica
feature: ddt
keywords:
  - tp dati analitica ddt
  - contabilità analitica ddt
  - competenza da a
  - commessa ddt
  - centro di costo ddt
  - destinazioni analitiche
task_tags:
  - riferimento analitica ddt
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - logistica
  - amministrazione vendite
  - amministrazione
review_status: approved
module: DDT
tab_name: TP Dati Analitica
field_labels:
  - Data da
  - Data a
  - Commessa
  - Centro di costo
---
# TP Dati Analitica del DDT

## Campi

### Data da
Indica l'inizio del periodo di competenza.

### Data a
Indica la fine del periodo di competenza.

### Commessa
Consente di indicare dati semplificati di contabilità analitica, se previsti.

### Centro di costo
Consente di indicare dati semplificati di contabilità analitica, se previsti.

## Regole

### Contabilità analitica
Nel TP Dati Analitica vengono gestite le informazioni di contabilità analitica del DDT.

Queste informazioni vengono riprese nei passaggi successivi del documento di trasporto, ad esempio:
- fatturazione
- contabilizzazione della fattura

### Competenza del periodo
I campi data da e data a permettono di determinare la quota di competenza del periodo.

### Attivazione campi analitici da tipo documento
Se nella tabella tipo documento di trasporto è impostato il TP di analitica, si attivano i campi corrispondenti alle destinazioni indicate nella tabella.

### Valori proposti
Nel TP possono essere impostati valori che verranno proposti automaticamente.

I valori proposti restano modificabili.

### Ripresa sulle righe
Le informazioni analitiche vengono riprese sulle righe del DDT e possono comunque essere modificate.