---
title: Modulo di contabilità generale
doc_kind: overview
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - registrazioni contabili
  - contabilizzazione da altri moduli
  - piano dei conti
  - mastro
  - partitario
  - liquidazioni IVA
  - consolidamento periodo
  - libro giornale
task_tags:
  - panoramica contabilità generale
  - flusso operativo contabilità generale
  - integrazioni contabilità generale
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
aliases:
  - contabilità generale
---
# Modulo di contabilità generale

Il modulo di contabilità generale consente di gestire la contabilità secondo la normativa vigente, tramite inserimento diretto delle registrazioni e/o tramite contabilizzazione dei dati generati da altri moduli.

## Funzione del modulo
Il modulo supporta la gestione della contabilità generale e costituisce un punto di raccordo tra registrazioni contabili, elaborazioni fiscali e scambio dati con altri moduli dell'ERP.

## Configurazione della maschera principale
La maschera principale si configura graficamente in modo diverso a seconda del tipo di registrazione contabile.

La configurazione dipende da:
- una serie di parametri chiave presenti in tabella Tipo documento
- il tipo di conto

Gli aspetti che influenzano il comportamento della gestione sono:
- gestione IVA
- contabilità analitica
- gestione partite
- gestione percipienti

Questi aspetti si sovrappongono e si intersecano tra loro, consentendo di rispondere a esigenze diversificate oltre a quella principale della contabilità generale e fornendo gli input all'elaborazione di altri moduli.

## Struttura del piano dei conti
Il piano dei conti su cui si basa la contabilità è organizzato su due livelli:
- mastro
- partitario

Tra i conti più articolati rientrano clienti e fornitori, che contengono informazioni rilevanti:
- sul piano anagrafico, amministrativo e fiscale
- sul piano commerciale

## Stampe e controlli
Oltre alle stampe fiscali, il modulo prevede anche stampe di utilità che forniscono dati su aspetti particolari delle registrazioni.

In particolare, tali stampe possono riguardare:
- partite
- differenze cambi
- incompletezze o discordanze tra i dati

## Integrazione con altri moduli
Il modulo di contabilità generale si interfaccia con altri moduli attraverso lo scambio di dati, sia in invio sia in ricezione.

### Fatturazione
Attraverso contabilizzazione fatture e note di credito attive.

### Bilancio
Attraverso rilevazione di chiusure e aperture dei conti e differenti prospetti di bilancio.

### Tesoreria
Attraverso inserimento di movimenti provvisori e presunti e situazioni finanziarie a più livelli.

### Pagamenti fornitori
Attraverso chiusura delle partite con l'emissione dei bonifici e contabilizzazione delle distinte di pagamento.

### Solleciti
Attraverso l'evidenza delle partite scadute da sollecitare ai clienti.

### Percipienti
Attraverso rilevazione dei compensi, delle ritenute e dei contributi.

### Cartellino cliente
Attraverso evidenza delle informazioni riguardanti il saldo contabile, l'esposizione, le partite e le dilazioni di pagamento.

### Cespiti
Attraverso inserimento di fatture di acquisto cespiti con compilazione anagrafica cespiti e contabilizzazione ammortamenti.

### Contabilità industriale
Attraverso ripresa dei movimenti contabili per l'analisi gestionale.

### Controllo fatture
Attraverso contabilizzazione fatture passive.

### Insoluti
Attraverso riapertura del credito andato in insoluto.

### Portafogli effetti
Attraverso chiusura delle partite clienti e rilevazione dell'esposizione bancaria.

### Agenti
Attraverso liquidazione provvigioni in base all'incassato e contabilizzazione fatture agenti.

## Flusso logico operativo
Il flusso logico delle operazioni da svolgere per l'utilizzo del modulo di contabilità generale è il seguente:

1. Inserimento movimenti e/o contabilizzazione dati da altri moduli.
2. Stampa fiscali, registri IVA, dichiarazioni di intento, Intrastat.
3. Liquidazioni IVA periodiche.
4. Consultazioni movimenti contabili.
5. Verifica partite aperte in scadenza o scadute.
6. Consolidamento del periodo.
7. Stampa libro giornale.