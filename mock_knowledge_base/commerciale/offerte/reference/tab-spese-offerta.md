---
title: Campi del tab TP Spese dell'offerta
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - tp spese offerta
  - spese aggiuntive offerta
  - spese trasporto
  - spese consegna
  - spese montaggio
  - tipi fatturato
  - aliquota iva
task_tags:
  - riferimento spese offerta
erp_versions:
  - v.1.0
role_scope:
  - sales
  - accounting
review_status: approved
module: Offerte
screen_title: Offerte
tab_name: TP Spese
field_labels:
  - Modalità
  - Aliquota IVA
  - Importo
---
# Campi del tab TP Spese dell'offerta

## Campi

### Modalità
Definisce la modalità della spesa aggiuntiva.

### Aliquota IVA
Definisce l'aliquota IVA associata alla spesa.

### Importo
Definisce l'importo della spesa aggiuntiva.

## Regole

### Tipologie di spesa gestibili
Nel tab è possibile inserire spese aggiuntive all'offerta, come:
1. spese di trasporto;
2. spese di consegna;
3. spese di montaggio.

### Configurazione preventiva
Le spese devono essere caricate nella tabella **Tipi fatturato**.

### Dati richiesti in tabella
Nella tabella **Tipi fatturato** devono essere specificati:
1. modalità;
2. aliquota IVA;
3. importo.

### Proposta automatica di modalità e IVA
I campi **Modalità** e **Aliquota IVA**, se non valorizzati manualmente, vengono ripresi dalla tabella **Tipi fatturato** per il tipo di fatturato selezionato.