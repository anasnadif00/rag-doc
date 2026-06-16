---
title: TP Dati di spedizione del DDT
doc_kind: reference
domain: logistica
feature: ddt
keywords:
  - tp dati spedizione ddt
  - cliente fatturazione ddt
  - cliente ordine ddt
  - luogo destinazione ddt
  - cliente spedizione
task_tags:
  - riferimento dati spedizione ddt
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - logistica
  - amministrazione vendite
review_status: approved
module: DDT
tab_name: TP Dati di spedizione
field_labels:
  - Cliente di fatturazione
  - Cliente ordine
  - Luogo di destinazione
---
# TP Dati di spedizione del DDT

## Campi

### Cliente di fatturazione
Indica il cliente che verrà utilizzato per l'emissione delle fatture generate dal DDT.

È un campo obbligatorio.

### Cliente ordine
Se il DDT è stato generato dalla ripresa di un ordine, viene ripreso dal intestatario dell'ordine.

### Luogo di destinazione
Indica il luogo di destinazione della merce.

Non è un campo obbligatorio.

## Regole

### Proposta cliente di fatturazione
Se nell'anagrafica del cliente di spedizione non è stato indicato alcun cliente di fatturazione, viene proposto il cliente di spedizione.

Se è presente un cliente di fatturazione differente, viene proposto quello.

### Più clienti di fatturazione
Se per il cliente di spedizione sono presenti più clienti di fatturazione, non viene proposto automaticamente alcun cliente di fatturazione.

L'utente può sceglierlo dalla lista dei clienti di fatturazione associati al cliente di spedizione.

### Cliente di fatturazione diverso
È possibile inserire anche un cliente di fatturazione diverso da quelli specificati nell'anagrafica del cliente di spedizione.

### Proposta luogo di destinazione
Il luogo di destinazione viene proposto dal TP corrispondente dell'anagrafica cliente di spedizione.

Se sono presenti più luoghi di destinazione, viene proposto quello di default.

Se non è stato specificato alcun luogo di destinazione, viene proposta la ragione sociale e l'indirizzo del cliente di spedizione.

### Luogo di destinazione diverso
È possibile inserire una destinazione diversa da quelle presenti nell'anagrafica del cliente di spedizione.

### Modificabilità
I dati proposti sono modificabili.