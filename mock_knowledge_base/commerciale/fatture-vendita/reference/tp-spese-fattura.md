---
title: Campi e regole del TP Spese
doc_kind: reference
domain: commerciale
feature: fatture-vendita
keywords:
  - tp spese
  - spese fattura
  - tipo fatturato
  - modalità iva
  - aliquota iva
  - spese automatiche
task_tags:
  - riferimento spese fattura
erp_versions:
  - v.1.0
role_scope:
  - amministrazione
  - commerciale
review_status: approved
module: Fatture
tab_name: Spese
field_labels:
  - Tipo fatturato
  - Modalità IVA
  - Aliquota IVA
  - Importo
---
# Campi e regole del TP Spese

## Campi

### Tipo fatturato
Identifica la tipologia di spesa da addebitare in fattura.

### Modalità IVA
Definisce la modalità IVA applicata alla spesa.

### Aliquota IVA
Definisce l'aliquota IVA associata alla spesa.

### Importo
Importo della spesa da addebitare.

### Dati analitici
Consentono l'imputazione delle informazioni di contabilità analitica associate alla spesa.

## Regole

### Proposta automatica dei dati IVA
Se Modalità IVA e Aliquota IVA non vengono compilate manualmente, i valori vengono ricavati dalla configurazione del Tipo fatturato selezionato.

### Ripresa automatica delle spese
Le spese possono essere proposte automaticamente oppure riprese da:

- ordini clienti
- documenti di trasporto

in funzione delle impostazioni presenti:

- nella tabella Tipo fattura di vendita
- nell'anagrafica cliente