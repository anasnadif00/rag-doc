---
title: Tipo pagamento
doc_kind: reference
domain: contabilita
feature: tipo-pagamento
keywords:
  - tipo pagamento
  - tipi di pagamento
  - giorno fisso di scadenza
  - giorno scarto giorno fisso
  - mesi esclusi
  - giorno fisso mese escluso
  - fine mese
  - addizione a spese
  - forma di pagamento
  - fatture elettroniche
  - codici ministeriali sdi
task_tags:
  - riferimento tipo pagamento
  - configurazione tipo pagamento
  - configurazione scadenze pagamento
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Tabelle
screen_title: Tipo pagamento
aliases:
  - tabella tipo pagamento
  - tipi di pagamento
field_labels:
  - Codice
  - Descrizione
  - Descrizione in lingua
  - Giorno fisso di scadenza
  - Giorno scarto giorno fisso
  - Mesi esclusi
  - Giorno fisso mese escluso
  - Fine mese
  - Addizione a spese
  - Forma di pagamento
  - Tipologia
  - Fatture elettroniche
---
# Tipo pagamento

## Campi
### Codice
Il tipo pagamento viene definito tramite un codice univoco di massimo tre caratteri.

### Descrizione
Descrizione del tipo pagamento.

### Descrizione in lingua
Nel pannello **Descrizione in lingua** è possibile codificare e impostare la descrizione nella lingua straniera desiderata.

### Giorno fisso di scadenza
Il campo **Giorno fisso di scadenza** indica il giorno fisso da considerare nell'attribuzione della data di scadenza.

Se il giorno di scadenza calcolato è superiore al giorno fisso, la data di scadenza viene spostata al mese successivo.

### Giorno scarto giorno fisso
Il campo **Giorno scarto giorno fisso** indica il numero di giorni di tolleranza da considerare rispetto al giorno fisso.

Se il giorno di scadenza calcolato supera il giorno fisso ma rientra nei giorni di scarto, la scadenza non viene spostata al mese successivo.

### Mesi esclusi
Nel campo **Mesi esclusi** vanno indicati i mesi da escludere nel calcolo delle scadenze.

### Giorno fisso mese escluso
Nel campo **Giorno fisso mese escluso** va indicato il giorno fisso a cui portare la scadenza nel mese successivo a quello escluso.

### Fine mese
Il flag **Fine mese**, se attivato, porta le scadenze all'ultimo giorno del mese indipendentemente dalla data del documento.

### Addizione a spese
Il flag **Addizione a spese** è utilizzato nei moduli del commerciale per applicare automaticamente le spese di incasso.

### Forma di pagamento
Nel campo **Forma di pagamento** va indicata la forma di pagamento associata al tipo di pagamento.

Una volta associata la forma di pagamento, viene riportata anche la relativa tipologia.

### Tipologia
La tipologia della forma di pagamento associata può assumere uno dei seguenti valori:
- ricevuta
- tratta
- pagherò
- altro

### Fatture elettroniche
Nel campo **Fatture elettroniche** vanno indicati i codici fissi MB ministeriali per la compilazione delle fatture elettroniche da inviare al sistema di interscambio.

## Regole
### Funzione della tabella
La tabella Tipo pagamento consente di definire i diversi tipi di pagamento da associare a clienti e fornitori.

### Regola del giorno fisso
Quando il giorno di scadenza calcolato supera il valore indicato in **Giorno fisso di scadenza**, la scadenza viene spostata al mese successivo.

### Regola dei giorni di scarto
Se il superamento del **Giorno fisso di scadenza** rientra nel numero di giorni indicati in **Giorno scarto giorno fisso**, la scadenza non viene spostata al mese successivo.

### Regola dei mesi esclusi
I mesi indicati in **Mesi esclusi** non devono essere utilizzati nel calcolo della scadenza.

In questi casi la scadenza viene portata al mese successivo, utilizzando il valore definito nel campo **Giorno fisso mese escluso**.

### Regola di fine mese
Se il flag **Fine mese** è attivo, la scadenza viene sempre portata all'ultimo giorno del mese.

### Relazione con la forma di pagamento
Ogni tipo pagamento può essere collegato a una **Forma di pagamento**. Da questa associazione viene alimentata automaticamente la forma di pagamento sulle partite.