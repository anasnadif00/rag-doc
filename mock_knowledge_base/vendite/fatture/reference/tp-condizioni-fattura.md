---
title: TP Condizioni della fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - tp condizioni
  - lingua
  - listino
  - spedizione
  - imballo
  - porto
  - zona
  - ritenuta attiva
task_tags:
  - riferimento condizioni fattura
erp_versions:
  - v.1.0
role_scope:
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: Condizioni
field_labels:
  - Lingua
  - Tipo listino
  - Spedizione
  - Imballo
  - Porto
  - Zona
  - Data listino
---
# TP Condizioni della fattura

## Campi

### Lingua

Ripresa dall'anagrafica cliente o dall'ordine di origine.

### Tipo listino

Ripreso dall'anagrafica cliente o dall'ordine.

### Spedizione

Ripresa dai dati commerciali del cliente o dall'ordine.

### Imballo

Ripreso dai dati commerciali del cliente o dall'ordine.

### Porto

Ripreso dai dati commerciali del cliente o dall'ordine.

### Zona

Ripresa dai dati commerciali del cliente o dall'ordine.

### Data listino

Viene proposta la data corrente.

Il valore è modificabile.

### Banca azienda

Viene proposta dai dati del documento ma può essere modificata.

### Banca di appoggio

Viene proposta dai dati del cliente ma può essere modificata.

### Ritenuta attiva

Se il cliente ha una percentuale di ritenuta attiva nei dati fiscali dell'anagrafica, il valore viene riportato automaticamente e utilizzato per il calcolo dell'importo relativo.

## Regole

### Origine dei dati

Le informazioni sono normalmente riprese:

- dall'anagrafica cliente;
- dall'ordine cliente eventualmente ripreso in fattura.