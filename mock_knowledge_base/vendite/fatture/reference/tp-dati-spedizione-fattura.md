---
title: TP Dati di spedizione della fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - cliente spedizione
  - cliente ordine
  - luogo destinazione
  - destinazione merce
task_tags:
  - riferimento dati spedizione fattura
erp_versions:
  - v.1.0
role_scope:
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: Dati di spedizione
field_labels:
  - Cliente spedizione
  - Cliente ordine
  - Luogo di destinazione
---
# TP Dati di spedizione della fattura

## Campi

### Cliente spedizione

Se la fattura deriva dalla valorizzazione di un DDT viene riportato il cliente intestatario del documento di trasporto.

Negli altri casi coincide con l'intestatario della fattura.

### Cliente ordine

Se la fattura deriva da un ordine cliente o da un DDT viene visualizzato il cliente intestatario dell'ordine.

Negli altri casi coincide con l'intestatario della fattura.

### Luogo di destinazione

Viene proposto il luogo di destinazione presente nei dati di spedizione e fatturazione del cliente di spedizione.

In presenza di più destinazioni viene proposta quella impostata come predefinita.

Se non esistono luoghi di destinazione configurati, vengono riportati ragione sociale e indirizzo del cliente di spedizione.

I dati proposti sono modificabili.

È possibile inserire una destinazione diversa da quelle presenti in anagrafica.

## Regole

### Obbligatorietà

Il luogo di destinazione non è un campo obbligatorio.