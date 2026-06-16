---
title: Campi della tabella Versioni di contabilità
doc_kind: reference
domain: contabilita
feature: versioni-di-contabilita
keywords:
  - versioni di contabilità
  - parametri contabili
  - contabilità analitica
  - competenza IVA acquisti
  - numerazione movimenti consolidati
  - controllo ABI e CAB
  - partite su numero documento
  - data competenza bilancio
task_tags:
  - riferimento parametri contabili
  - configurazione versione contabilita
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità
screen_title: Versioni di contabilità
aliases:
  - tabella Versioni di contabilità
field_labels:
  - Conti extra contabili
  - Partite su numero documento
  - Descrizione conto su libro giornale
  - Descrizione conto su brogliaccio
  - Contro partita obbligatoria
  - Causale obbligatoria
  - Controlli importi IVA su registrazione
  - Controllo anno documento
  - Utilizzo numeri di registrazione cancellati
  - Descrizione Conto su Causale Contropartita
  - Tipologia di conto
  - Numerazione annuale movimenti consolidati
  - Controllo ABI e CAB
  - Contabilità analitica
  - Plafond sulla data
  - Metodo di calcolo
  - Numerazione Pagine Registro per anno
  - Competenza sulla data
  - Contabilizzazione effetto
  - Competenza IVA acquisti
  - Per fatture acquisto di fine anno
  - considera tutti i mesi
  - Visualizzazione fatture elettroniche passive con pulizia caratteri non consentiti
  - Su prime note
  - impostare la divisione di analitica da tabella operatore
---
# Versioni di contabilità

La tabella **Versioni di contabilità** consente di impostare parametri validi per tutte le registrazioni contabili e per le elaborazioni effettuate nel modulo.

## Campi

### Conti extra contabili
Se attivato, abilita il flag **Extra contabili** nell'anagrafica **Conti**.

### Partite su numero documento
Se attivato, le partite vengono generate identificandole con il numero di documento.  
Se non attivato, le partite vengono generate utilizzando il numero di protocollo.

### Descrizione conto su libro giornale
Se attivato, nel **libro giornale** viene stampata anche la descrizione del conto oltre al codice.

### Descrizione conto su brogliaccio
Se attivato, nel **brogliaccio** viene stampata anche la descrizione del conto oltre al codice.

### Contro partita obbligatoria
Se attivato, rende obbligatoria la contropartita in ogni registrazione.

### Causale obbligatoria
Se attivato, rende obbligatoria l'indicazione della causale in ogni registrazione.

### Controlli importi IVA su registrazione
Se attivato, esegue e segnala i controlli di correttezza sui calcoli relativi all'IVA nelle registrazioni di acquisto o di vendita.

### Controllo anno documento
Se attivato, controlla che la data documento appartenga all'anno in corso oppure, al massimo, all'anno precedente.

### Utilizzo numeri di registrazione cancellati
Consente di recuperare, con registrazioni successive, i numeri lasciati liberi da registrazioni cancellate.

Il numero non viene comunque recuperato se il movimento inserito è di tipo IVA, per non compromettere la sequenzialità del numero documento/protocollo.

### Descrizione Conto su Causale Contropartita
Se attivato, propone automaticamente sui movimenti relativi all'imponibile e all'IVA la descrizione del cliente o del fornitore.

### Tipologia di conto
Se attivato, permette di inserire nell'anagrafica **Conti** la tipologia del conto.

### Numerazione annuale movimenti consolidati
Se attivato, in fase di consolidamento movimenti assegna alle registrazioni un numero progressivo per esercizio che viene stampato nel libro giornale.

### Controllo ABI e CAB
Se attivato, e se gli archivi ABI/CAB sono stati caricati dal modulo **Dati RIBA**, in fase di inserimento o modifica dei codici ABI/CAB nell'anagrafica **Conti** viene controllata la loro presenza nell'archivio caricato.

### Contabilità analitica
Determina il comportamento del pannello **analitica** dei movimenti di COGE, a parità di attivazione della richiesta centro di costo per il tipo documento utilizzato.

Le opzioni disponibili sono:

- **Senza contabilità analitica**  
  Non viene mai richiesta la compilazione del pannello analitica dei movimenti di COGE.

- **Commessa / centro di costo senza contabilità analitica**  
  Per i conti economici viene richiesta la compilazione del campo **commessa**, situato in alto nel pannello analitica dei movimenti di COGE.

- **Contabilità analitica su conti economici**  
  Viene richiesta la compilazione del pannello analitica dei movimenti di COGE per destinazione per i conti economici.

- **Contabilità analitica sui conti selezionati**  
  Viene richiesta la compilazione del pannello analitica dei movimenti di COGE solo per i conti indicati nella tabella **Conti con imputazione**.

- **Contabilità analitica sui conti economici | patrimoniali**  
  Viene richiesta la compilazione del pannello analitica dei movimenti di COGE per tutti i conti, indipendentemente dal raggruppamento di bilancio.

### Plafond sulla data
Consente di selezionare una delle seguenti opzioni:

- **Documento**  
  La competenza del plafond viene desunta dalla data del documento.

- **Registrazione**  
  La competenza del plafond viene desunta dalla data di registrazione.

### Metodo di calcolo
Consente di selezionare una delle seguenti opzioni:

- **Solare**  
  La stampa riepilogo plafond effettua i calcoli degli importi del plafond utilizzando il metodo solare.

- **Mobile**  
  La stampa riepilogo plafond effettua i calcoli degli importi del plafond utilizzando il metodo mobile.

### Numerazione Pagine Registro per anno
Consente di selezionare una delle seguenti opzioni:

- **Anno fiscale**  
  Le pagine dei registri IVA e del libro giornale vengono numerate in base all'anno fiscale.

- **Anno solare**  
  Le pagine dei registri IVA e del libro giornale vengono numerate in base all'anno solare.

### Competenza sulla data
Consente di selezionare una delle seguenti opzioni:

- **Registrazione**  
  Il campo **Data competenza bilancio** sui movimenti contabili assume lo stesso valore della data registrazione.

- **Documento**  
  Il campo **Data competenza bilancio** assume il valore della data documento. Se la data documento non è valorizzata, viene utilizzata la data registrazione.

La data competenza bilancio visibile sui movimenti contabili è una data alternativa a quella fiscale effettiva e viene utilizzata per la redazione di bilancini infrannuali.

### Contabilizzazione effetto
Consente di selezionare una delle seguenti opzioni:

- **Immediata**  
  La contabilizzazione immediata degli effetti chiude le partite ad essi associate prima che gli effetti arrivino effettivamente a scadenza. In questo caso l'estratto conto risulta a zero e diventa necessario utilizzare il valore dell'esposizione cambiaria.

- **A scadenza**  
  Consente di utilizzare scritture transitorie prima di chiudere effettivamente la partita e di azzerare quindi il saldo dell'estratto conto.

### Competenza IVA acquisti
Consente di selezionare una delle seguenti opzioni:

- **Registrazione**
- **Documento**

L'impostazione determina come viene calcolata la competenza IVA sulle registrazioni di tipo acquisto.

### Per fatture acquisto di fine anno, considera tutti i mesi
Se impostato, indica che le fatture di fine anno registrate in mesi diversi dal primo vengano gestite come i documenti simili ricevuti a gennaio.

### Visualizzazione fatture elettroniche passive con pulizia caratteri non consentiti
Se impostato, permette la visualizzazione dei documenti ricevuti previa pulizia dei caratteri non riconosciuti o non consentiti.

### Su prime note, impostare la divisione di analitica da tabella operatore
Consente la compilazione automatica della divisione nel pannello analitica delle registrazioni contabili di **prime note** in base all'operatore.

## Regole

### Recupero dei numeri di registrazione cancellati
L'opzione **Utilizzo numeri di registrazione cancellati** consente di riutilizzare i numeri lasciati liberi da registrazioni cancellate, ma non applica il recupero ai movimenti di tipo IVA, per preservare la sequenzialità del numero documento/protocollo.

### Numerazione annuale in consolidamento
Con l'opzione **Numerazione annuale movimenti consolidati** attivata, durante il consolidamento movimenti viene assegnato alle registrazioni un progressivo per esercizio che viene poi stampato nel libro giornale.

### Regole di compilazione della contabilità analitica
L'obbligatorietà del pannello analitica dei movimenti di COGE dipende dall'opzione selezionata nel campo **Contabilità analitica** e presuppone l'attivazione della richiesta centro di costo per il tipo documento utilizzato.

### Regola di competenza del plafond
Con **Plafond sulla data**, la competenza del plafond viene determinata alternativamente dalla data documento oppure dalla data di registrazione, in base all'opzione selezionata.

### Regola di numerazione delle pagine
Con **Numerazione Pagine Registro per anno**, la numerazione dei registri IVA e del libro giornale può essere gestita per anno fiscale oppure per anno solare.

### Regola della data competenza bilancio
Con **Competenza sulla data**:
- se l'impostazione è **Registrazione**, il campo **Data competenza bilancio** assume la data registrazione;
- se l'impostazione è **Documento**, il campo assume la data documento;
- se la data documento non è valorizzata, viene utilizzata la data registrazione.

### Regole di contabilizzazione effetto
Con **Contabilizzazione effetto**:
- l'opzione **Immediata** chiude le partite prima della scadenza effettiva degli effetti;
- l'opzione **A scadenza** utilizza scritture transitorie e consente la chiusura effettiva della partita alla scadenza.

### Regole di competenza IVA acquisti
Con **Competenza IVA acquisti**:
- se viene selezionata l'opzione **Registrazione**, la competenza IVA delle fatture di acquisto è il mese della registrazione;
- se viene selezionata l'opzione **Documento** e la fattura è registrata entro il 15 del mese successivo, la competenza IVA è pari al mese della data documento;
- se viene selezionata l'opzione **Registrazione** e la fattura è registrata dopo il 15 del mese successivo, la data con la competenza IVA è pari al mese della data registrazione;
- per i periodi a cavallo dell'anno, la competenza IVA si intende sempre sulla data di registrazione.

### Fatture acquisto di fine anno
Se è attivo il parametro **Per fatture acquisto di fine anno, considera tutti i mesi**, le fatture di fine anno registrate in mesi diversi dal primo vengono trattate come documenti analoghi ricevuti a gennaio.