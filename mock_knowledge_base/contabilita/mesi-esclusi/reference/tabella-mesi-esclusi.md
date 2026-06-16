---
title: Tabella Mesi esclusi
doc_kind: reference
domain: contabilita
feature: mesi-esclusi
keywords: [mesi esclusi, scadenze, cliente, fornitore, giorno fisso di scadenza, giorno relativo, soluzioni di pagamento, rate partite]
task_tags: [riferimento mesi esclusi, configurazione scadenze clienti fornitori]
erp_versions: [v.1.0]
role_scope: [accounting]
review_status: review
field_labels: [Codice, Descrizione, Giorno fisso di scadenza, Mesi esclusi, Giorno relativo]
---
# Tabella Mesi esclusi

La tabella consente di definire, a livello di singolo cliente o fornitore, l’esclusione dal calcolo delle scadenze di uno o più mesi, andando al mese successivo in sostituzione a quanto previsto per il tipo pagamento specificato.

## Campi
### Codice
È un codice univoco di al massimo 3 caratteri.

### Descrizione
È la descrizione del codice mese escluso.

### Giorno fisso di scadenza
Rappresenta il giorno fisso da considerare nell’attribuzione della data di scadenza.

Se indicato, la data di scadenza calcolata viene modificata impostando il giorno uguale al valore del campo.

Se il giorno di scadenza calcolato è superiore al giorno fisso, la data di scadenza viene spostata al mese successivo.

### Mesi esclusi
Consentono di indicare i mesi che sono esclusi nel calcolo delle date di scadenza da attribuire alle rate di una partita.

Se la data di scadenza della rata, determinata a partire dalla data del documento sommando i giorni di dilazione previsti nella tabella Soluzioni di pagamento, cade in uno dei mesi esclusi, si possono presentare due casi:
- se nel campo Giorno relativo non è indicato alcun valore, la data di scadenza effettiva viene portata allo stesso giorno del primo mese successivo non escluso
- se nel campo Giorno relativo è indicato un giorno, la data di scadenza effettiva viene portata al giorno specificato del primo mese successivo non escluso

### Giorno relativo
Rappresenta il giorno fisso da attribuire alla data di scadenza nel caso in cui quella calcolata a partire dalla data del documento, sommando i giorni di dilazione previsti nella tabella Soluzioni di pagamento, cada in uno dei mesi esclusi.

## Regole
### Ambito di applicazione
La configurazione viene definita a livello di singolo cliente o fornitore.

### Deroga al tipo pagamento
L’esclusione di uno o più mesi nel calcolo delle scadenze viene applicata in sostituzione di quanto previsto per il tipo pagamento specificato.

### Interazione con le Soluzioni di pagamento
Il calcolo della scadenza parte dalla data del documento e dai giorni di dilazione previsti nella tabella Soluzioni di pagamento.

### Gestione del giorno fisso di scadenza
Se è valorizzato il campo Giorno fisso di scadenza, la data calcolata viene adeguata a quel giorno.

Se il giorno risultante è successivo al giorno fisso indicato, la scadenza slitta al mese successivo.

### Gestione dei mesi esclusi
Se la scadenza calcolata cade in un mese escluso, la data effettiva viene rinviata al primo mese successivo non escluso.

### Gestione del giorno relativo
Se il campo Giorno relativo è compilato e la scadenza cade in un mese escluso, la nuova data di scadenza viene impostata al giorno indicato nel primo mese successivo non escluso.