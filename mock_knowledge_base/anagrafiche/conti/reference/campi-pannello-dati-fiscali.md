---
title: Campi del pannello Dati Fiscali dei Conti
doc_kind: reference
domain: anagrafiche
feature: conti
keywords:
  - dati fiscali conti
  - pannello dati fiscali
  - fattura elettronica
  - percipienti
  - certificazione unica
  - modello 770
  - allegati IVA
  - dogana
  - comunicazione dati fatture
  - rappresentante fiscale
  - residenza
  - residenza estera
  - causale percipiente
  - tipologia prestazione
  - ritenuta fiscale
  - contributo previdenziale
  - dati INAIL
  - stato estero dichiarazioni di intento
task_tags:
  - riferimento campi conti
  - configurazione dati fiscali conto
  - configurazione fattura elettronica
  - configurazione percipienti
erp_versions:
  - v.1.0
role_scope:
  - admin
  - accounting
review_status: approved
module: Conti
screen_title: Conti
tab_name: Dati fiscali
field_labels:
  - Cognome
  - Nome
  - Allegati IVA
  - Dogana
  - Escludi da comunicazione dati fatture
  - Riepilogativo comunicazione dati fatture
  - Tipo
  - Indice PA
  - Codice destinatario
  - PEC
  - E-mail alternativa
  - Codice Paese
  - Partita IVA
  - Codice Fiscale
  - Denominazione
  - Titolo
  - Codice EORI
  - Via e numero civico
  - CAP
  - Città
  - Provincia
  - Stato di residenza
  - Codice stato estero
  - Residente
  - Luogo di attinenza
  - Non residente Schumacker
  - Frontaliere
  - Indirizzo
  - Codice Stato Estero Ministeriale
  - Causale
  - Tipologia prestazione
  - Codice
  - Percentuale di assoggettamento
  - Percentuale di ritenuta
  - Percentuale di assoggettamento contributo previdenziale
  - Percentuale contributo previdenziale
  - Percentuale a carico del collaboratore
  - Posizione assicurativa territoriale
  - Data inizio
  - Data fine
  - Codice comune
  - Stato estero per dichiarazioni di intento ricevute
---
# Campi del pannello Dati Fiscali dei Conti

## Campi
### Cognome
Deve essere compilato, insieme al campo Nome, per la corretta formazione delle Certificazioni Uniche e del file 770 relativi ai percipienti.

### Nome
Deve essere compilato, insieme al campo Cognome, per la corretta formazione delle Certificazioni Uniche e del file 770 relativi ai percipienti.

### Allegati IVA
È un'impostazione mantenuta per compatibilità con la versione precedente di Magia. Indicava la selezione e quindi l'inclusione del conto cliente all'interno degli allegati IVA.

### Dogana
Se impostato, indica che il conto è una dogana.

### Escludi da comunicazione dati fatture
Flag mantenuto per compatibilità con normative precedenti relative alla comunicazione dati fatture all'Agenzia delle Entrate.

### Riepilogativo comunicazione dati fatture
Flag mantenuto per compatibilità con normative precedenti relative alla comunicazione dati fatture all'Agenzia delle Entrate.

### Tipo
Definisce la tipologia del cliente rispetto all'invio della fattura elettronica.

### Indice PA
Indica il codice ufficio destinatario della fattura elettronica verso la Pubblica Amministrazione.

### Codice destinatario
Indica il codice destinatario di sette cifre da riportare nel file della fattura elettronica inviato al cliente.

### PEC
Indica l'indirizzo di posta elettronica certificata fornito dal cliente, utilizzabile in alternativa al Codice destinatario.

### E-mail alternativa
Indica un indirizzo di posta elettronica da utilizzare solo quando non sono disponibili o utilizzabili il Codice destinatario e la PEC.

### Codice Paese
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Partita IVA
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Codice Fiscale
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Denominazione
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Cognome del rappresentante fiscale
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Nome del rappresentante fiscale
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Titolo
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Codice EORI
Dato del rappresentante fiscale esposto nella sezione corrispondente della fattura elettronica.

### Via e numero civico
Dato di residenza del percipiente.

### CAP
Dato di residenza del percipiente.

### Città
Dato di residenza del percipiente.

### Provincia
Dato di residenza del percipiente.

### Stato di residenza
Dato di residenza del percipiente.

### Codice stato estero
Dato di residenza del percipiente.

### Residente
Va impostato se il percipiente è residente all'interno dello Stato.

### Luogo di attinenza
Va impostato per la compilazione della Certificazione Unica.

### Non residente Schumacker
Va impostato per la compilazione della Certificazione Unica.

### Frontaliere
Va impostato per la compilazione della Certificazione Unica.

### Indirizzo residenza estera
Contiene via e numero civico della residenza estera del percipiente.

### Città residenza estera
Contiene la città della residenza estera del percipiente.

### Provincia residenza estera
Contiene la provincia della residenza estera del percipiente.

### Codice Stato Estero Ministeriale
Contiene il codice dello Stato estero ministeriale della residenza estera del percipiente.

### Causale
Indica, previa codifica nell'apposita tabella, la causale di operatività del percipiente.

### Tipologia prestazione
Indica il tipo di attività del percipiente, ad esempio regime ordinario, occasionale o forfettario.

### Codice
Indica il codice corretto per la compilazione della Certificazione Unica.

### Percentuale di assoggettamento
È la percentuale dell'imponibile sulla quale calcolare la ritenuta fiscale.

### Percentuale di ritenuta
È la percentuale di ritenuta fiscale da applicare alla parte di compenso assoggettata a ritenuta.

### Percentuale di assoggettamento contributo previdenziale
È la percentuale di assoggettamento del contributo utilizzata per il calcolo dei contributi previdenziali.

### Percentuale contributo previdenziale
È la percentuale del contributo previdenziale calcolata sul valore determinato dalla percentuale di assoggettamento contributo previdenziale.

### Percentuale a carico del collaboratore
È la percentuale utilizzata per calcolare la quota di contributo a carico del collaboratore.

### Posizione assicurativa territoriale
Dato INAIL mantenuto per compatibilità con annualità precedenti.

### Data inizio
Dato INAIL mantenuto per compatibilità con annualità precedenti.

### Data fine
Dato INAIL mantenuto per compatibilità con annualità precedenti.

### Codice comune
Dato INAIL mantenuto per compatibilità con annualità precedenti.

### Stato estero per dichiarazioni di intento ricevute
Consente di indicare lo stato estero da utilizzare per le dichiarazioni di intento ricevute.

## Regole
### Ambito del pannello
Nel pannello Dati fiscali della gestione dei Conti è possibile inserire i dati del conto relativi a fatturazione elettronica e percipienti.

### Obbligatorietà di Cognome e Nome per i percipienti
I campi Cognome e Nome devono essere compilati per la corretta formazione delle Certificazioni Uniche e del file 770 relativi ai percipienti.

### Valori del campo Tipo per la fattura elettronica
Il campo Tipo può assumere i seguenti valori:
- Non impostato: i nuovi clienti vengono creati con questo valore e, al salvataggio del conto, viene mostrato un messaggio di avviso per la mancata impostazione dei dati della fattura elettronica.
- Nessuna: il cliente non sarà destinatario di fattura elettronica.
- Pubblica amministrazione: il cliente è destinatario di fattura elettronica PA e si attiva il campo Indice PA.
- Privati: il cliente è una partita IVA o un privato destinatario di fattura elettronica e si attivano i campi Codice destinatario, PEC ed E-mail alternativa.

### Priorità del dato di spedizione per Indice PA
Il campo Indice PA può essere inserito anche a livello di cliente di spedizione. In caso di fatturazione raggruppata per cliente di spedizione, se la fattura indica il cliente di spedizione viene utilizzato il dato di quest'ultimo; altrimenti viene utilizzato quello del cliente di fatturazione.

### Priorità del dato di spedizione per Codice destinatario
Il campo Codice destinatario può essere inserito anche a livello di cliente di spedizione. In caso di fatturazione raggruppata per cliente di spedizione, se la fattura indica il cliente di spedizione viene utilizzato il dato di quest'ultimo; altrimenti viene utilizzato quello del cliente di fatturazione.

### Alternatività tra Codice destinatario e PEC
Il Codice destinatario non è obbligatorio. In alternativa può essere utilizzato l'indirizzo PEC fornito dal cliente.

### Utilizzo dell'E-mail alternativa
Il campo E-mail alternativa viene utilizzato solo quando non sono disponibili o non sono utilizzabili il Codice destinatario e la PEC.

### Esposizione del rappresentante fiscale in fattura elettronica
I dati del riquadro Rappresentante fiscale vengono esposti nella fattura elettronica se nel tipo fattura di vendita è impostato il flag che prevede l'esposizione dei dati del rappresentante fiscale.

### Utilizzo del riquadro Residenza
Il riquadro Residenza contiene i dati di residenza dei fornitori indicati anche come percipienti.

### Utilizzo del riquadro Residenza estera
Se il percipiente non risiede all'interno dello Stato, è possibile compilare i campi del riquadro Residenza estera.

### Utilizzo del riquadro Percipiente
Nel riquadro Percipiente vanno indicati i dati che consentono di calcolare automaticamente le ritenute e i contributi di un compenso all'interno di Magia.

### Compatibilità dei dati INAIL
I dati presenti nel riquadro Dati INAIL sono riferiti a annualità precedenti e sono mantenuti per compatibilità con le versioni di Magia.