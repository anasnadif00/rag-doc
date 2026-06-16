---
title: Tabella Conti immobilizzazioni
doc_kind: reference
domain: contabilita
feature: conti-immobilizzazioni
keywords:
  - conti immobilizzazioni
  - beni pluriennali
  - cespiti
  - tipo cespite
  - provenienza cespite
  - attività cespite
  - categoria fiscale cespite
  - automatismo cespiti
task_tags:
  - riferimento tabella conti immobilizzazioni
  - configurazione automatismo cespiti
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
screen_title: Conti immobilizzazioni
aliases:
  - tabella conti immobilizzazioni
field_labels:
  - Conto
  - Tipologia cespite
  - Provenienza
  - Attività
  - Categoria fiscale
---
# Tabella Conti immobilizzazioni

## Campi
### Conto
Indica il conto che identifica un bene pluriennale.

### Tipologia cespite
Indica la tipologia cespite associata al conto.

Il valore è codificato nella tabella Tipo cespite del modulo Cespiti.

### Provenienza
Indica la provenienza associata al conto.

Il valore è codificato nella tabella Provenienza del modulo Cespiti.

### Attività
Indica l'attività associata al conto.

Il valore è codificato nella tabella Attività del modulo Cespiti.

### Categoria fiscale
Indica la categoria fiscale associata al conto.

Il valore è codificato nella tabella Categoria fiscale del modulo Cespiti.

## Regole
### Identificazione dei beni pluriennali
La tabella consente di indicare quali sono i conti che identificano un bene pluriennale.

### Integrazione con il modulo Cespiti
Associando al conto le informazioni di Tipologia cespite, Provenienza, Attività e Categoria fiscale, è possibile creare il cespite all'interno del modulo Cespiti.

### Automatismo in registrazione acquisto
La creazione del cespite avviene in concomitanza con la registrazione del documento di acquisto, utilizzando l'automatismo previsto da Magia.