---
title: TP Dati di analitica del DDT
doc_kind: reference
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - TP Dati di analitica DDT
  - contabilità analitica DDT
  - commessa DDT
  - centro di costo DDT
  - competenza DDT
task_tags:
  - riferimento TP Dati di analitica DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
  - amministrazione
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Dati di analitica
aliases:
  - analitica DDT
  - dati analitici DDT
field_labels:
  - Da data
  - A data
  - Commessa
  - Centro di costo
---
# TP Dati di analitica del DDT

## Campi

### Da data
Consente di indicare la data iniziale del periodo di competenza.

### A data
Consente di indicare la data finale del periodo di competenza.

### Commessa
Consente di inserire dati semplificati di contabilità analitica.

### Centro di costo
Consente di inserire dati semplificati di contabilità analitica.

## Regole

### Gestione della contabilità analitica
Nel TP Dati di analitica vengono gestite le informazioni di contabilità analitica del DDT.

Queste informazioni verranno riprese nei passaggi successivi subiti dal documento di trasporto, ad esempio:

- fatturazione;
- contabilizzazione della fattura.

### Campi sempre attivi
Sono sempre attivi i campi:

- Da data;
- A data;
- Commessa;
- Centro di costo.

### Competenza del periodo
I campi Da data e A data permettono di determinare la quota di competenza del periodo.

### Analitica impostata sul tipo documento
Se nel tipo documento di trasporto è stato impostato il TP di analitica, vengono attivati tutti i campi corrispondenti alle destinazioni indicate nella tabella del tipo documento.

### Valori proposti sulle righe
Nel TP Dati di analitica possono essere impostati valori proposti automaticamente.

I valori vengono ripresi sulle righe del DDT e possono essere modificati.
