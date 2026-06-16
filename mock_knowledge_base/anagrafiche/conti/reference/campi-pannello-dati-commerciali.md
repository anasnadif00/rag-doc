---
title: Campi del pannello Dati Commerciali dei Conti
doc_kind: reference
domain: anagrafiche
feature: conti
keywords:
  - dati commerciali conti
  - pannello dati commerciali
  - categoria amministrativa
  - gerarchia sconto
  - fido
  - cliente pagatore
  - lingua
  - tipo listino
  - porto
  - spedizione
  - imballo
  - vettore
  - nazione
  - zona
  - categoria provvigionale
  - categoria commerciale
  - percorso
  - classe evasione
  - agente
  - provvigione diretta
  - provvigione indiretta
  - fatturazione singola
  - addebito spese incasso
  - spese di bollo
  - sconti fornitore
task_tags:
  - riferimento campi conti
  - configurazione dati commerciali conto
erp_versions:
  - v.1.0
role_scope:
  - admin
  - commerciale
  - accounting
review_status: approved
module: Conti
screen_title: Conti
tab_name: Dati Commerciali
field_labels:
  - Categoria amministrativa
  - Gerarchia
  - Fido
  - Cliente pagatore
  - Lingua
  - Tipo di listino
  - Porto
  - Spedizione
  - Imballo
  - Vettore
  - Nazione
  - Zona
  - Categoria provvigionale
  - Categoria commerciale
  - Percorso
  - Classe evasione
  - Agente
  - Percentuale di provvisione diretta
  - Provvigione indiretta
  - Fatturazione singola
  - Addebito spese incasso
  - Spese di bollo
---
# Campi del pannello Dati Commerciali dei Conti

## Campi
### Categoria amministrativa
Identifica la categoria amministrativa relativa al conto e determina gli eventuali blocchi applicabili, in base alla tabella Categoria Amministrativa.

### Gerarchia
Consente di indicare la gerarchia dello sconto relativa al conto.

### Fido
Consente di indicare l'importo del fido relativo al conto.

### Cliente pagatore
Consente di indicare il codice del cliente pagatore relativo al conto.

### Lingua
Consente di indicare l'idioma relativo al conto.

### Tipo di listino
Consente di indicare il codice Tipo Listino relativo al conto.

### Porto
Consente di indicare il codice del Porto relativo al conto.

### Spedizione
Consente di indicare il codice della Spedizione relativo al conto.

### Imballo
Consente di indicare il codice dell'Imballo relativo al conto.

### Vettore
Consente di indicare il codice del Vettore relativo al conto.

### Nazione
Consente di indicare il codice della Nazione relativo al conto. Il campo è importante per la gestione dei dati IVA, ad esempio nella fatturazione elettronica e nell'Intrastat.

### Zona
Consente di indicare il codice della Zona relativa al conto.

### Categoria provvigionale
Consente di indicare il codice della Categoria Provvigionale relativa al conto.

### Categoria commerciale
Consente di indicare il codice della Categoria Commerciale relativa al conto.

### Percorso
Consente di indicare il codice del Percorso relativo al conto.

### Classe evasione
Consente di indicare il codice della Classe Evasione relativa al conto.

### Agente
Consente di indicare il codice dell'Agente associato al conto.

### Percentuale di provvisione diretta
Indica la percentuale di provvigione diretta relativa all'agente associato al conto.

### Provvigione indiretta
Indica la percentuale di provvigione indiretta relativa all'agente associato al conto.

### Fatturazione singola
Può assumere il valore sì oppure no. Se impostato a sì, per ogni documento di trasporto viene generata una fattura. Se impostato a no, è possibile effettuare una valorizzazione riepilogativa dei DDT.

### Addebito spese incasso
Consente di impostare l'addebito automatico di eventuali spese di incasso.

### Spese di bollo
Consente di indicare la modalità di applicazione delle spese di bollo.

### Sconti fornitore
Per i fornitori è possibile indicare fino a tre tipologie di sconto, ciascuna con la relativa percentuale.

## Regole
### Ambito del pannello
Il pannello Dati Commerciali raccoglie le informazioni gestite dal flusso commerciale di Magia, come ordini clienti, fatture e agenti.

### Valore predefinito della Nazione
Se il campo Nazione rimane vuoto, nelle elaborazioni di Magia viene desunto il valore Italia.

### Valori del campo Fatturazione singola
Il campo Fatturazione singola può essere impostato a:
- sì, per generare una fattura per ogni documento di trasporto
- no, per consentire una valorizzazione riepilogativa dei DDT

### Valori del campo Spese di bollo
Il campo Spese di bollo può essere impostato a:
- addebita, per esporre e addebitare le spese di bollo al cliente
- applica ma non addebita, per esporre le spese di bollo senza addebitarle al cliente
- no spese bollo, per non applicare le spese di bollo