---
title: Pannello Partite del corpo della Contabilità Generale
doc_kind: reference
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - pannello partite
  - scadenze
  - chiusura partite
  - apertura partite
  - rata
  - forma di pagamento
  - ritenute
  - contributi previdenziali
  - abbuono
  - sconto
  - spese
  - agente
  - CIG
  - CUP
task_tags:
  - riferimento pannello partite contabilità generale
  - gestione scadenze attive e passive
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Contabilità Generale
tab_name: Partite
field_labels:
  - Rata
  - Tipo documento
  - Numero documento
  - Anno documento
  - Scadenza
  - Forma di pagamento
  - Causale di non pagabilità
  - Data competenza
  - Segno
  - Saldo
  - Controvalore
  - CUP
  - CIG
  - Abbuono
  - Sconto
  - Spese
  - Ritenute
  - Contributi previdenziali
  - Agente
---
# Pannello Partite del corpo della Contabilità Generale

Il pannello Partite consente di gestire la generazione e il saldo delle scadenze, sia attive sia passive, e degli altri elementi collegati, come ritenute, contributi, differenze cambi, sconti e abbuoni.

I termini partita e scadenza sono da considerarsi sinonimi.

## Campi
### Rata
È un elemento identificativo della partita.

### Tipo documento
È un elemento identificativo della partita.

### Numero documento
È un elemento identificativo della partita.

### Anno documento
È un elemento identificativo della partita.

### Scadenza
È la data di scadenza della partita.

Può essere modificata anche dopo la generazione della partita, ma non dopo che la partita è stata associata per la chiusura.

### Forma di pagamento
È la forma di pagamento associata al tipo di pagamento indicato nell'anagrafica del cliente o del fornitore.

Funge da filtro per:
- generazione effetti
- Pagamenti fornitori

Può essere indicata manualmente se nell'anagrafica del conto non sono stati specificati tipo e soluzione di pagamento.

### Causale di non pagabilità
Per le partite appena generate consente di associare una causale o nota.

Per le partite riprese propone la nota eventualmente già associata in precedenza.

Se la partita è stata sollecitata, contiene gli estremi dei solleciti.

Il contenuto della nota è visualizzato in diverse stampe, tra cui:
- estratto conto
- scadenzario

### Data competenza
È la data di competenza IVA nel caso di incasso o pagamento di fatture con IVA ad esigibilità differita.

Quando viene ripresa una partita con tale caratteristica, la competenza viene impostata in base alla Data registrazione del movimento.

### Segno
Può essere:
- Dare
- Avere

### Saldo
È da utilizzare solo nel caso di tipi documento specificati come Chiusura partite.

Presenta le seguenti caratteristiche:
- viene proposto già spuntato se l'importo della partita corrisponde all'importo del movimento oppure è inferiore, quindi il residuo va a zero
- può essere spuntato dall'operatore se l'importo del movimento è inferiore a quello della partita ripresa ma questa deve essere comunque chiusa

Quando il saldo viene forzato con un importo del movimento inferiore a quello della partita, la differenza viene attribuita a un conto in base alle impostazioni del Tipo documento.

### Controvalore
Nel caso in cui la partita sia in divisa, riporta il controvalore originario della partita.

### CUP
È il Codice Univoco di Progetto.

Viene riportato in tutti i moduli successivi in cui viene richiamata la partita, ad esempio nel file dei bonifici SEPA in caso di pagamento a fornitore.

### CIG
È il Codice Identificativo di Gara.

Viene riportato in tutti i moduli successivi in cui viene richiamata la partita, ad esempio nel file dei bonifici SEPA in caso di pagamento a fornitore.

### Abbuono
Contiene l'importo in valuta o in euro della differenza tra l'importo indicato nella riga di movimento e l'importo della partita ripresa.

Se la partita è in divisa, viene compilato anche il relativo controvalore.

Quando viene rilevata una differenza d'importo e la partita è fleggata a saldo, la differenza viene assegnata automaticamente a questo campo, ma può essere modificata.

A questo campo corrisponde un conto da movimentare indicato nella tabella Parametri conti automatismi partite.

### Sconto
Contiene l'importo in valuta o in euro dello sconto.

Se la partita è in divisa, viene compilato anche il relativo controvalore.

Può essere utilizzato in alternativa al campo Abbuono per imputare l'importo a uno specifico conto indicato nella tabella Parametri conti automatismi partite.

### Spese
Nel caso di un Tipo documento impostato come Chiusura partite, al momento della ripresa delle scadenze è possibile imputare a una o più partite un importo in questo campo, ad esempio a titolo di spese bancarie.

L'importo viene aggiunto alla registrazione utilizzando il conto corrispondente impostato nella tabella Parametri conti automatismi partite.

La quadratura degli importi avviene aumentando o diminuendo l'importo sul conto banca.

### Ritenute
Viene compilato automaticamente quando si sta pagando una partita a cui è collegata una ritenuta.

L'importo viene assegnato al conto corrispondente indicato nella tabella Parametri conti automatismi partite.

La quadratura degli importi avviene diminuendo l'importo sul conto banca.

### Contributi previdenziali
Viene compilato automaticamente quando si sta pagando una partita a cui sono collegati dei contributi.

L'importo viene assegnato al conto corrispondente indicato nella tabella Parametri conti automatismi partite.

La quadratura degli importi avviene diminuendo l'importo sul conto banca.

### Agente
Il campo si attiva solo se il conto è un cliente.

L'informazione dell'agente è riportata in tutte le stampe e le elaborazioni successive, compresi i solleciti, per avere sempre il riferimento dell'agente specifico di quella vendita.

## Regole
### Condizioni di attivazione
Per attivare il pannello Partite devono essere soddisfatte le seguenti condizioni:
- in tabella Tipo documento deve essere attivato uno dei parametri Natura documento diverso da Non gestito a partite aperte
- il conto su cui si vogliono gestire le partite deve avere attivo in anagrafica Conti il flag Gestione partite

Solitamente si tratta di clienti e fornitori, ma possono essere anche altri conti, come:
- scadenzari leasing
- rate di mutuo
- finanziamenti

### Momento di compilazione
La compilazione del pannello può essere effettuata in qualunque momento nel corso della registrazione.

### Quadratura obbligatoria
Se si tenta di memorizzare la registrazione senza partite, viene generato un messaggio di errore perché non è possibile memorizzare senza quadratura tra l'importo di riga e la somma algebrica delle partite.

Questo garantisce sempre la quadratura tra scheda contabile e scadenze.

La quadratura può essere verificata tramite i campi:
- riferito
- da riferire

### Generazione automatica delle partite
Se il Tipo documento ha attivato il parametro Apertura partite in tabella Tipo documento, le scadenze vengono generate automaticamente in base a:
- Numero documento e Data documento in testata del movimento, che in questo caso sono obbligatori
- condizioni di pagamento inserite nell'anagrafica del conto

I dati proposti possono essere modificati o annullati dall'utente.

Se le partite vengono annullate, possono essere ricreate:
- con inserimento manuale
- dalla toolbar destra, impostando il numero di rate e cliccando sul pulsante Genera

### Identificazione della partita
Una partita o scadenza è identificata dai seguenti elementi:
- conto cliente o fornitore
- divisa
- tipo documento
- anno del documento
- numero del documento
- numero di rata

### Chiusura partite
Per chiusura partite si intende un movimento, tipicamente di incasso o pagamento oppure una nota di credito, in cui si abbina una scadenza generata precedentemente.

### Gestione partite in divisa
Nel caso di conti gestiti in divisa:
- l'importo della partita è espresso in divisa
- il controvalore è espresso in euro

Il controvalore è calcolato sia al momento dell'apertura sia al momento della chiusura ed è rilevante ai fini del calcolo dell'eventuale differenza positiva o negativa di cambio.

### Ripresa partite esistenti
Se il Tipo documento ha impostato la Natura documento a Chiusura partite oppure Effetti, le scadenze non vengono generate ma devono essere associate quelle create precedentemente attraverso l'apposito pulsante di ripresa.

Il pulsante di ripresa apre una maschera con l'elenco delle partite ancora aperte, cioè con residuo diverso da zero per il conto e la divisa indicati nella riga di movimento.