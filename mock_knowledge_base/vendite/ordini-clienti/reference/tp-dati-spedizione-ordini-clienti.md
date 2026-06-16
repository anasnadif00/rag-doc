---
title: TP Dati spedizione degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - TP Dati spedizione
  - cliente di fatturazione
  - cliente di spedizione
  - luogo di destinazione
  - spedizione ordine cliente
task_tags:
  - riferimento TP Dati spedizione ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP Dati spedizione
field_labels:
  - Cliente di fatturazione
  - Cliente di spedizione
  - Luogo di destinazione
---
# TP Dati spedizione degli Ordini clienti

## Campi

### Cliente di fatturazione
Viene ripreso dall'anagrafica del conto, se impostato, ed è il cliente al quale verrà fatturato l'ordine.

Può essere modificato e può anche essere inserito un cliente diverso da quello previsto nell'anagrafica.

È un campo obbligatorio.

### Cliente di spedizione
Indica il conto del cliente al quale verrà inoltrato il DDT di consegna.

Può coincidere con:
- il cliente intestatario dell'ordine
- il cliente di fatturazione

Se è presente nell'anagrafica del conto, viene proposto automaticamente. In caso contrario, il sistema propone il cliente dell'ordine.

Può essere modificato e può anche essere inserito un cliente diverso da quello previsto nell'anagrafica.

È un campo obbligatorio.

### Luogo di destinazione
Viene proposto dai dati di spedizione e fatturazione dell'anagrafica conti, se presente.

Può essere:
- lasciato vuoto
- inserito manualmente
- modificato rispetto al valore proposto

Non è un campo obbligatorio.

## Regole

### Obbligatorietà
I campi **Cliente di fatturazione** e **Cliente di spedizione** sono obbligatori per l'inserimento dell'ordine.

### Proposta automatica
I dati di fatturazione, spedizione e destinazione vengono normalmente proposti dall'anagrafica del conto, ma restano modificabili.

### Destinazione alternativa
Il **Luogo di destinazione** può essere compilato manualmente quando la spedizione deve essere effettuata in un luogo diverso da quello associato al cliente di spedizione.