---
title: Pannello Analitica del corpo della Contabilità Generale
doc_kind: reference
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - pannello analitica
  - dati coin
  - contabilità industriale
  - contabilità analitica
  - centro di costo
  - commessa
  - tipo transazione
  - destinazioni
task_tags:
  - riferimento pannello analitica contabilità generale
  - gestione dati COIN
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Contabilità Generale
tab_name: Analitica
aliases:
  - DATI COIN
field_labels:
  - Commessa
  - Anno
  - Divisione
  - Importo
  - Da data competenza
  - A data competenza
---
# Pannello Analitica del corpo della Contabilità Generale

Il pannello Analitica gestisce le informazioni di contabilità analitica o DATI COIN in base alle impostazioni definite in Versioni di contabilità, Tipo documento, tipi transazione e tipi destinazione.

## Campi
### Commessa
Si attiva quando in tabella Versioni di contabilità è impostata l'opzione Commessa e centri di costo senza contabilità analitica e risultano soddisfatte le condizioni di attivazione del pannello.

Il campo fa riferimento alla tabella Commesse / Centri di costo della gestione tabelle di Contabilità Generale.

### Anno
Si attiva insieme al campo Commessa quando la modalità di gestione prevista è Commessa e centri di costo senza contabilità analitica.

### Divisione
Nelle configurazioni con collegamento alla contabilità industriale, una volta inserita la Divisione, Magia attiva automaticamente i campi delle destinazioni gestite dal tipo transazione associato al movimento.

### Importo
È uno dei campi fissi del pannello nelle configurazioni con collegamento alla contabilità industriale.

### Da data competenza
È uno dei campi fissi del pannello nelle configurazioni con collegamento alla contabilità industriale.

### A data competenza
È uno dei campi fissi del pannello nelle configurazioni con collegamento alla contabilità industriale.

## Regole
### Prima condizione di attivazione
Per attivare il pannello Analitica, in tabella Versioni di contabilità la voce Contabilità analitica deve essere impostata con un'opzione diversa da Senza contabilità analitica.

### Seconda condizione di attivazione
Nel Tipo documento utilizzato deve essere attivato il valore Richiesta centro di costo.

### Terza condizione di attivazione
Per l'attivazione del pannello viene verificato anche il raggruppamento di bilancio del partitario, con regole diverse in base all'opzione di Contabilità analitica impostata in Versioni di contabilità.

#### Commessa e centri di costo senza contabilità analitica oppure Contabilità analitica sui conti economici
Il raggruppamento di bilancio del partitario deve essere economico, quindi costo o ricavo.

#### Contabilità analitica su conti selezionati
Il raggruppamento di bilancio del partitario può essere sia economico sia patrimoniale, a condizione che il conto sia presente nella tabella Conti con imputazione contabilità analitica.

#### Contabilità analitica su conti economici/patrimoniali
Il raggruppamento di bilancio del partitario può essere sia economico sia patrimoniale.

### Gestione senza collegamento alla contabilità industriale
Se in Versioni di contabilità è impostata l'opzione Commessa e centri di costo senza contabilità analitica, quando tutte le condizioni sono soddisfatte risultano compilabili nel pannello:
- Commessa
- Anno

### Gestione con collegamento alla contabilità industriale
Se in Versioni di contabilità è impostata una delle opzioni seguenti:
- contabilità analitica su conti economici
- contabilità analitica su conti selezionati
- contabilità analitica su conti economici/patrimoniali

si attiva il collegamento con la contabilità industriale.

In base al Tipo documento specificato, viene reperito per società e divisione il codice transazione associato al movimento.

Il codice transazione identifica una tipologia di movimentazione di contabilità industriale e definisce i tipi di destinazione che devono essere compilati e valorizzati, indicando anche se sono obbligatori o meno.

Le destinazioni compilabili sono variabili in base a quanto indicato nel tipo transazione.

### Quadratura degli importi
Per confermare la registrazione è necessario che il totale degli importi inseriti su tutte le righe di analitica sia uguale al valore della riga di movimento a cui si riferiscono.