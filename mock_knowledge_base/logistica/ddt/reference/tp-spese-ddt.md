---
title: TP Spese del DDT
doc_kind: reference
domain: logistica
feature: ddt
keywords:
  - tp spese ddt
  - spese accessorie ddt
  - tipo fatturato spese
  - modalità iva spese
  - aliquota iva spese
  - gestione valori bolle
task_tags:
  - riferimento spese ddt
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
  - amministrazione
review_status: approved
module: DDT
tab_name: TP Spese
field_labels:
  - Tipo fatturato
  - Modalità IVA
  - Aliquota IVA
  - Importo
  - Analitica
---
# TP Spese del DDT

## Campi

### Tipo fatturato
Indica il tipo fatturato da utilizzare per la spesa accessoria.

### Modalità IVA
Indica la modalità IVA applicata alla spesa.

### Aliquota IVA
Indica l'aliquota IVA applicata alla spesa.

### Importo
Indica l'importo della spesa accessoria.

### Analitica
Consente di indicare i dati analitici collegati alla spesa.

## Regole

### Inserimento spese accessorie
Nel TP Spese vengono inserite le spese accessorie del DDT.

### Proposta modalità IVA e aliquota IVA
Se modalità IVA e aliquota IVA non sono indicate manualmente, vengono desunte dalla tabella tipo fatturato in base al tipo fatturato specificato.

### Attivazione TP Spese
Il TP Spese è attivo solo se nella tabella Parametri del Commerciale è attivo il flag bolle Gestione valori.