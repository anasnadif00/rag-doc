---
title: Sconti nei Listini vendita
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - sconti listini vendita
  - sconto a percentuale
  - sconto a valore
  - sconti a quantità fissa
  - sconti a scaglioni
  - tipo sconto
task_tags:
  - riferimento sconti listini vendita
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
screen_title: Listini vendita
tab_name: Sconti
field_labels:
  - Tipo sconto
  - Percentuale
  - Importo
  - Quantità
  - Valore
---
# Sconti nei Listini vendita

## Campi

### Tipo sconto
Indica il tipo di sconto utilizzato.

I tipi di sconto sono quelli inseriti nella tabella parametri del commerciale.

Possono essere selezionati solo i tipi di sconto che hanno attivo il flag sconto di listino.

### Sconto a percentuale
Se il tipo sconto ha attivo il flag a percentuale, lo sconto viene applicato in percentuale sul prezzo.

In questo caso si attiva il campo Percentuale.

### Percentuale
Contiene il valore percentuale dello sconto da applicare.

Il campo si attiva solo se il flag a percentuale è attivo.

### Sconto a valore
Se il tipo sconto non ha attivo il flag a percentuale, viene richiesto uno sconto a valore.

In questo caso si attiva il campo Importo.

### Importo
Consente di indicare il valore dello sconto da applicare.

Il campo si attiva solo se il flag a percentuale è disattivato.

### Sconti a quantità fissa
Gli sconti a quantità fissa permettono di applicare lo sconto indipendentemente dalla quantità movimentata in:
- ordini;
- DDT;
- fatture.

### Sconti a scaglioni
Gli sconti a scaglioni permettono di applicare sconti diversi in base a scaglioni di quantità o di valore.

### Quantità
Se attivata, lo scaglione di sconto viene determinato in base alla quantità indicata in ordine, DDT o fattura.

### Valore
Se attivato, lo scaglione di sconto viene determinato in base al valore della riga.

Il valore è calcolato come quantità per prezzo lordo dell'articolo presente in ordine, DDT o fattura.

## Regole

### Tipi sconto selezionabili
Nel listino possono essere utilizzati solo i tipi sconto configurati nei parametri del commerciale e abilitati come sconto di listino.

### Applicazione degli sconti a scaglioni
Per gli sconti a scaglioni, il sistema determina lo scaglione applicabile in base al criterio attivato:
- quantità;
- valore.

Il valore dello sconto applicato dipende dal tipo sconto e dallo scaglione individuato.