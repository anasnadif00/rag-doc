---
title: Campi della tabella Tipo documento
doc_kind: reference
domain: contabilita
feature: tipo-documento
keywords:
  - tipo documento
  - tipo documento contabilità generale
  - tipo IVA
  - natura documento
  - competenza
  - tipo destinazione bilancio
  - percipienti
  - segno
  - tipo numerazione
  - tipo documento dati fatture
task_tags:
  - riferimento tipo documento
  - configurazione tipo documento contabile
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità
screen_title: Tipo documento
aliases:
  - tabella Tipo documento
field_labels:
  - Codice
  - Descrizione
  - Tipo IVA
  - Natura Documento
  - Competenza
  - Tipo destinazione bilancio
  - Percipienti
  - Segno
  - Insoluto
  - Richiesta centro di costo
  - Bolla doganale
  - Cambio su data documento
  - IVA ad esigibilità differita
  - Richiesta data valuta
  - Bilancio di apertura
  - Bilancio di chiusura
  - Risultato d'esercizio
  - Fattura definitiva
  - Acquisto o vendita cespite / studi di ricerca
  - Tipo numerazione
  - Tipo documento dati fatture
---
# Campi della tabella Tipo documento

La tabella **Tipo documento** contiene la lista delle codifiche dei tipi documento utilizzati per registrare i movimenti in contabilità generale.

Il tipo documento di contabilità generale determina come vengono gestite le movimentazioni all'interno di Magia. Per questo motivo è importante codificare correttamente ogni tipo documento.

## Campi

### Codice
Identifica in modo univoco il tipo documento.

Il codice può essere composto da un massimo di 3 caratteri.

### Descrizione
Consente di inserire la descrizione del tipo documento.

### Tipo IVA
Consente di indicare la tipologia del movimento.

Le opzioni possibili sono:
- **Non gestito**, per tutti i movimenti che non sono di tipo IVA, come prime note generiche, ammortamenti, pagamenti e incassi
- **Vendite**, per la fatturazione attiva
- **Acquisti**, per la fatturazione passiva
- **Fattura IVA proforma**, per le parcelle provvisorie
- **Corrispettivi**

### Natura Documento
Consente di indicare in che modo devono essere gestite le partite all'interno del movimento contabile.

Le opzioni possibili sono:
- **Non gestito a partite aperte**: non vengono richieste o gestite le partite all'interno del movimento, anche se il conto prevede la gestione delle partite
- **Apertura partite**: viene richiesta l'apertura obbligatoria di una partita per i conti impostati in anagrafica con gestione partite
- **Chiusura partite**: viene richiesta la chiusura di una partita oppure l'apertura di una nuova partita nel caso in cui non ce ne siano da chiudere, per i conti che in anagrafica hanno impostato gestione partite
- **Effetti**: si comporta come **Chiusura partite**, ma deve essere utilizzato per le tipologie di movimentazione relative alle registrazioni effetti, in modo da poter calcolare separatamente il valore di questi ultimi nell'estratto conto

### Competenza
Consente di indicare la competenza fiscale a livello di bilancio o contabile del movimento.

Le opzioni possibili sono:
- **Competenza esercizio in corso**: una registrazione inserita nell'anno è di competenza dello stesso anno
- **Competenza esercizio precedente**: una registrazione inserita nell'anno ha competenza nell'esercizio precedente
- **Senza competenza**: il movimento contabile non ha alcuna competenza e quindi nessuna rilevanza nei saldi contabili e nel bilancio

L'opzione **Senza competenza** viene utilizzata soprattutto per caricamenti o sistemazioni di partite. Si tratta quindi di movimenti il cui saldo non influisce sul bilancio, ma che possono variare la parte delle scadenze dell'estratto conto.

### Tipo destinazione bilancio
Consente di indicare la tipologia di destinazione di bilancio per la gestione IFRS.

Le opzioni possibili sono:
- **Comune**
- **Civilistico**
- **Internazionale**

### Percipienti
Consente di indicare la tipologia di registrazione relativa ai percipienti.

I valori possibili sono:
- **Compenso**: consente, nelle registrazioni contabili, la gestione dei dati dei compensi, come ritenuta e contributi, per i fornitori impostati in anagrafica come Percipienti
- **Ritenuta**: consente, nelle registrazioni contabili, di gestire la parte di rilevazione della ritenuta ed eventuali contributi in fase di pagamento della fattura per i fornitori impostati in anagrafica come Percipienti
- **Altro**: non attiva nelle registrazioni contabili la gestione dei dati dei percipienti, anche se i fornitori sono impostati in anagrafica come Percipienti

### Segno
Consente di indicare il segno proposto della prima riga del movimento.

I valori possibili sono:
- **Dare**
- **Avere**

### Insoluto
Se impostato, indica che il movimento è una registrazione di insoluto.

### Richiesta centro di costo
Se attivato, durante la registrazione vengono richiesti i dati relativi alla contabilità analitica.

### Bolla doganale
Se impostato, indica che la registrazione è una bolla doganale.

### Cambio su data documento
Se impostato, il cambio viene applicato basandosi sulla data documento. In caso contrario viene applicato in base alla data registrazione.

### IVA ad esigibilità differita
Se attivato, durante la compilazione del movimento si applicano le regole previste per la registrazione particolare IVA ad esigibilità differita.

### Richiesta data valuta
Se attivato, per i conti di tesoreria viene richiesta la data valuta dell'operazione.

### Bilancio di apertura
Da attivare solo per il tipo documento utilizzato per l'apertura del bilancio.

Il saldo di apertura viene esposto come prima riga della scheda contabile anche se la registrazione di apertura è stata effettuata nel corso dell'anno.

### Bilancio di chiusura
Da attivare solo per il tipo documento utilizzato per la chiusura del bilancio.

Il relativo movimento viene escluso dalla scheda contabile richiesta con il flag **riporto saldi esercizio precedente**.

### Risultato d'esercizio
Da attivare solo per il tipo documento utilizzato per la rilevazione dell'utile o della perdita in fase di chiusura del bilancio.

### Fattura definitiva
Deve essere attivato per i tipi documento utilizzati per la registrazione di fatture definitive a fronte di preavvisi di parcella.

### Acquisto o vendita cespite / studi di ricerca
Se attivato, il movimento viene considerato dalla stampa **Rimborsi IVA**.

### Tipo numerazione
È rilevante per i documenti IVA.

Consente di attribuire al tipo documento una numerazione ai fini del registro IVA. Le numerazioni utilizzabili sono codificate nella tabella **Tipo numerazione e movimenti**.

### Tipo documento dati fatture
Contiene l'indicazione del codice **TD** associato alla tipologia di movimento, per fatture attive e passive, in base alle disposizioni ministeriali relative alla fatturazione elettronica.

## Regole

### Unicità del codice
Ogni tipo documento deve essere identificato da un codice univoco.

### Lunghezza massima del codice
Il codice del tipo documento può contenere al massimo 3 caratteri.

### Effetto del tipo IVA
Il valore del campo **Tipo IVA** determina se il movimento è gestito come movimento non IVA oppure come movimento IVA di acquisto, vendita, fattura IVA proforma o corrispettivi.

### Effetto della natura documento sulle partite
Il valore del campo **Natura Documento** determina se le partite non devono essere gestite, se devono essere aperte, se devono essere chiuse oppure se devono essere gestite come effetti.

### Effetto della competenza
Il valore del campo **Competenza** determina se il movimento ha competenza nell'esercizio in corso, nell'esercizio precedente oppure se è senza competenza e quindi senza rilevanza nei saldi contabili e nel bilancio.

### Utilizzo di Senza competenza
L'opzione **Senza competenza** è destinata soprattutto a caricamenti o sistemazioni di partite. In questo caso il saldo del movimento non influisce sul bilancio, ma può modificare le scadenze dell'estratto conto.

### Gestione IFRS
Il campo **Tipo destinazione bilancio** determina la destinazione di bilancio per la gestione IFRS tra **Comune**, **Civilistico** e **Internazionale**.

### Gestione percipienti
Il campo **Percipienti** attiva oppure non attiva la gestione dei dati dei compensi, delle ritenute e degli eventuali contributi nelle registrazioni contabili per i fornitori impostati come Percipienti.

### Proposta del segno iniziale
Il campo **Segno** determina il segno proposto per la prima riga del movimento.

### Utilizzo dei flag di bilancio
I campi **Bilancio di apertura**, **Bilancio di chiusura** e **Risultato d'esercizio** devono essere attivati solo per i tipi documento specificamente destinati alle relative registrazioni di bilancio.

### Utilizzo del tipo numerazione
Il campo **Tipo numerazione** è utilizzato solo per i documenti IVA e collega il tipo documento a una numerazione definita nella tabella **Tipo numerazione e movimenti**.

### Utilizzo del tipo documento dati fatture
Il campo **Tipo documento dati fatture** associa al tipo documento il codice **TD** previsto dalle disposizioni ministeriali per la fatturazione elettronica.