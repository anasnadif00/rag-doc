---
title: Campi del pannello Parametri liquidazione in Società
doc_kind: reference
domain: contabilita
feature: societa
keywords:
  - parametri liquidazione
  - liquidazione IVA
  - tipo documento liquidazione
  - conto IVA a debito
  - conto IVA a credito
  - conto erario
  - conto IVA indetraibile prorata
task_tags:
  - riferimento parametri liquidazione
  - configurazione liquidazione IVA
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilita
screen_title: Società
tab_name: Parametri liquidazione
field_labels:
  - Tipo documento
  - Conto IVA a debito
  - Conto IVA a credito
  - Conto erario
  - Conto IVA indetraibile prorata
source_uri: trascrizione-utentee-tabella-societa
---
# Campi del pannello Parametri liquidazione in Società

## Campi

### Tipo documento
È il tipo documento della registrazione che Magia genererà in automatico dopo la liquidazione dell'IVA.

### Conto IVA a debito
Indica il conto IVA a debito che sarà stornato dalla scrittura generata.

### Conto IVA a credito
Indica il conto IVA a credito che sarà stornato dalla scrittura generata.

### Conto erario
Indica il conto erario nel quale confluirà la differenza tra il valore dell'IVA a debito e dell'IVA a credito rilevati dalle liquidazioni.

### Conto IVA indetraibile prorata
Identifica la quota relativa al prorata in base alle percentuali indicate.

## Regole

### Finalità del pannello
Nel pannello **Parametri liquidazione** è possibile impostare i parametri per la generazione automatica di una scrittura contabile al termine della liquidazione IVA.

### Generazione automatica della scrittura
I conti indicati in questo pannello sono utilizzati da Magia per costruire la registrazione contabile automatica successiva alla liquidazione.