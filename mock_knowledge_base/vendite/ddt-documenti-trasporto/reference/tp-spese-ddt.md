---
title: TP Spese del DDT
doc_kind: reference
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - TP Spese DDT
  - spese accessorie DDT
  - tipo fatturato DDT
  - modalità IVA DDT
  - aliquota IVA DDT
  - gestione valori bolle
task_tags:
  - riferimento TP Spese DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
  - amministrazione
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Spese
aliases:
  - spese bolla
  - spese accessorie bolla
field_labels:
  - Tipo fatturato
  - Modalità
  - Aliquota IVA
  - Importo
  - Analitica
---
# TP Spese del DDT

## Campi

### Tipo fatturato
Permette di indicare il tipo fatturato delle spese accessorie.

### Modalità
Permette di indicare la modalità associata alla spesa accessoria.

Se la modalità non viene indicata manualmente, viene desunta dalla tabella Tipo fatturato per il tipo fatturato specificato.

### Aliquota IVA
Permette di indicare l'aliquota IVA associata alla spesa accessoria.

Se l'aliquota IVA non viene indicata manualmente, viene desunta dalla tabella Tipo fatturato per il tipo fatturato specificato.

### Importo
Permette di indicare l'importo della spesa accessoria.

### Analitica
Permette di indicare i dati di analitica collegati alla spesa accessoria.

## Regole

### Attivazione del TP Spese
Il TP Spese è attivo solo se nella tabella Parametri del commerciale è stato impostato il flag bolle Gestione valori.