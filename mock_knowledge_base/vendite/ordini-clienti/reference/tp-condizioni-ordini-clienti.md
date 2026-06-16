---
title: TP Condizioni degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - TP Condizioni
  - condizioni ordine cliente
  - lingua ordine
  - listino ordine
  - imballo
  - porto
  - data listino
  - data consegna
  - data conferma
  - data evasione
task_tags:
  - riferimento TP Condizioni ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP Condizioni
field_labels:
  - Lingua
  - Listino
  - Imballo
  - Porto
  - Data listino
  - Data consegna
  - Data conferma
  - Data evasione
---
# TP Condizioni degli Ordini clienti

## Campi

### Lingua
Consente di indicare la lingua associata all'ordine.

### Listino
Il listino viene agganciato dall'anagrafica cliente e applicato agli articoli che verranno inseriti nell'ordine.

### Imballo
È normalmente ripreso dai dati presenti nell'anagrafica del conto.

### Porto
È normalmente ripreso dai dati presenti nell'anagrafica del conto.

### Data listino
Viene proposta con la data corrente, ma è modificabile.

### Data consegna
Se impostata nel tab, viene riportata automaticamente nelle righe caricate nell'ordine.

### Data conferma
Viene impostata automaticamente quando si esegue la stampa definitiva dell'ordine.

### Data evasione
Viene impostata automaticamente quando l'ordine viene evaso.

## Regole

### Ripresa dati anagrafici
Lingua, listino, imballo e porto sono normalmente proposti in automatico in base ai dati presenti nell'anagrafica del cliente.

### Propagazione alle righe
La **Data consegna** impostata nel TP Condizioni viene riportata automaticamente nelle righe dell'ordine.

### Ripresa dati da offerta
Se l'ordine deriva da un'offerta, i dati presenti nel TP Condizioni vengono ripresi dall'offerta e possono essere modificati o integrati.