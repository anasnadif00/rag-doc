---
title: TP Dati pagamenti degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords: [TP Dati pagamenti, pagamento ordine cliente, soluzione pagamento, data scadenza, tipo imputazione, condizioni di pagamento]
task_tags: [riferimento TP Dati pagamenti ordine cliente]
erp_versions: [v.1.0]
role_scope: [commerciale]
review_status: review
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP Dati pagamenti
field_labels: [Pagamento, Soluzione, Data scadenza, Tipo imputazione]
---
# TP Dati pagamenti degli Ordini clienti

## Campi

### Pagamento
Dato normalmente ripreso dal tab dati pagamenti dell'anagrafica del cliente intestatario dell'ordine.

### Soluzione
Se impostata, consente il calcolo automatico delle scadenze in base ai giorni definiti nella tabella soluzione.

### Data scadenza
Può essere indicata manualmente se la soluzione non è impostata.

### Tipo imputazione
Può essere impostato a percentuale oppure a valore.

## Regole

### Ripresa dati anagrafici
I dati di pagamento vengono normalmente proposti dall'anagrafica del cliente, con possibilità di modifica.

### Calcolo della scadenza
Se la **Soluzione** è impostata, la data di scadenza viene calcolata automaticamente in base ai giorni definiti nella relativa tabella.

### Obbligo in caso di imputazione a valore
Se è stato concordato con il cliente un pagamento con **Tipo imputazione** a valore, è obbligatorio inserire anche un tipo di pagamento con imputazione a percentuale per eventuali spese accessorie.

### Propagazione alle righe
Le condizioni di pagamento vengono proposte nelle singole righe dell'ordine con possibilità di modifica.

### Aggiornamento delle righe
Se le condizioni di pagamento vengono modificate successivamente in testata, le variazioni vengono riportate su tutte le righe dell'ordine che hanno le stesse condizioni di pagamento originarie.