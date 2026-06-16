---
title: Dati pagamenti dei Conti clienti e fornitori
doc_kind: reference
domain: contabilita
feature: conti
keywords:
  - conti
  - dati pagamenti
  - clienti
  - fornitori
  - pagamento
  - soluzione
  - mesi esclusi
  - fine mese
  - effetti riepilogativi
  - emissione dei solleciti
  - sdd
  - sepa direct debit
  - banca di appoggio
  - iban
  - cin
  - bic
  - aggiorna partite aperte cf
task_tags:
  - riferimento dati pagamenti conti
  - configurazione pagamenti clienti
  - configurazione pagamenti fornitori
  - configurazione banche di appoggio
  - aggiornamento partite aperte cf
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Conti
screen_title: Conti
tab_name: Dati pagamenti
aliases:
  - pannello dati pagamenti
  - dati bancari clienti e fornitori
field_labels:
  - Pagamento
  - Soluzione
  - Mesi esclusi
  - Fine mese
  - Effetti riepilogativi
  - Emissione dei solleciti
  - SDD data mandato
  - SDD identificativo mandato
  - SDD codice strumento
  - SDD tipo sequenza incasso
  - Codice banca
  - ABI
  - CAB
  - Conto corrente
  - IBAN
  - CIN
  - BIC
  - Descrizione banca
  - Aggiorna partite aperte CF
---
# Dati pagamenti dei Conti clienti e fornitori

## Campi
### Ambito del pannello
Il pannello **Dati pagamenti** della gestione dei **Conti** permette di inserire i dati bancari di incasso e di pagamento relativi a clienti e fornitori.

I dati del pannello si attivano solo per i conti impostati come **clienti** o come **fornitori**.

### Pagamento
Il campo **Pagamento** può essere impostato con uno dei tipi di pagamento inseriti nell'apposita tabella Tipi pagamento.

Il campo identifica la tipologia del pagamento del cliente o del fornitore.

### Soluzione
Il campo **Soluzione** può essere impostato con una delle voci inserite nella tabella **Soluzione Pagamento**.

Il campo identifica in che modo verranno calcolate le scadenze per le fatture emesse verso i clienti o ricevute dai fornitori.

### Mesi esclusi
Nel campo **Mesi esclusi** è possibile indicare un mese da escludere dal calcolo delle scadenze.

Il mese escluso farà slittare la data di scadenza a quello successivo.

### Fine mese
Il flag **Fine mese**, se impostato, calcola come data di scadenza l'ultimo giorno del mese rispetto ai giorni definiti nella soluzione di pagamento.

### Effetti riepilogativi
Il flag **Effetti riepilogativi**, se impostato, consente in fase di generazione degli effetti di produrre effetti riepilogativi per più scadenze e non per singola partita.

### Emissione dei solleciti
Il flag **Emissione dei solleciti**, se impostato, consente la sollecitabilità delle partite nel modulo **Solleciti**.

### SDD data mandato
Il campo **SDD data mandato** può essere inserito per i conti che gestiscono incassi **SEPA Direct Debit**.

### SDD identificativo mandato
Il campo **SDD identificativo mandato** può essere inserito per i conti che gestiscono incassi **SEPA Direct Debit**.

### SDD codice strumento
Il campo **SDD codice strumento** può essere inserito per i conti che gestiscono incassi **SEPA Direct Debit**.

### SDD tipo sequenza incasso
Il campo **SDD tipo sequenza incasso** può essere inserito per i conti che gestiscono incassi **SEPA Direct Debit**.

### Banche di appoggio
Ai conti clienti e fornitori è possibile associare una o più **banche di appoggio** che saranno utilizzate per la gestione degli effetti e dei bonifici.

Per ogni banca di appoggio è previsto un **codice univoco di due caratteri** impostato dall'utente.

Dopo l'inserimento del codice, tramite gli help di Magia, è possibile selezionare le banche in base all'archivio **ABI** e **CAB**.

### ABI
Il campo **ABI** identifica il codice ABI della banca di appoggio.

### CAB
Il campo **CAB** identifica il codice CAB della banca di appoggio.

### Conto corrente
Il campo **Conto corrente** contiene il numero di conto corrente della banca di appoggio.

### IBAN
Il campo **IBAN** identifica il codice IBAN della banca di appoggio. Una volta inseriti i campi **ABI**, **CAB** e **Conto corrente**, il codice **IBAN** viene calcolato automaticamente.

### CIN
Il campo **CIN** identifica il codice CIN della banca di appoggio. Una volta inseriti i campi **ABI**, **CAB** e **Conto corrente**, il codice **CIN** viene calcolato automaticamente.

### BIC
Il campo **BIC** identifica il codice BIC della banca di appoggio.

### Descrizione banca
Il campo **Descrizione** consente di indicare la descrizione della banca di appoggio..

### Aggiorna partite aperte CF
Attraverso il pulsante **Aggiorna partite aperte CF** è possibile aggiornare in automatico i dati bancari delle fatture di acquisto inserite nel modulo **Controllo fatture** con la banca di default impostata in anagrafica conto.

### Banca associata al conto
Per ogni conto cliente o fornitore è possibile indicare anche una banca associata.

## Regole
### Attivazione del pannello
Il pannello **Dati pagamenti** è gestibile solo per i conti configurati come **clienti** o **fornitori**.

### Calcolo delle scadenze
Il calcolo delle scadenze dipende dai valori indicati nei campi **Pagamento**, **Soluzione**, **Mesi esclusi** e **Fine mese**.

### Effetti riepilogativi
Se il flag **Effetti riepilogativi** è attivo, la generazione degli effetti avviene in forma riepilogativa per più scadenze, non per singola partita.

### Sollecitabilità delle partite
Se il flag **Emissione dei solleciti** è attivo, le partite del conto possono essere gestite nel modulo **Solleciti**.

### Utilizzo dei dati SDD
I dati **SDD data mandato**, **SDD identificativo mandato**, **SDD codice strumento** e **SDD tipo sequenza incasso** vengono utilizzati per la generazione dei relativi file da inviare ai servizi di remote banking.

### Banche di appoggio multiple
A un conto cliente o fornitore possono essere associate una o più banche di appoggio.

### Banca di default
Tra le banche di appoggio associate è necessario indicarne **una e una sola di default**.

### Calcolo automatico di IBAN e CIN
Dopo l'inserimento di **ABI**, **CAB** e **Conto corrente**, i campi **IBAN** e **CIN** vengono calcolati automaticamente.

### Aggiornamento delle fatture di acquisto
Il pulsante **Aggiorna partite aperte CF** aggiorna i dati bancari delle fatture di acquisto del modulo **Controllo fatture** utilizzando la banca di default definita nell'anagrafica conto.