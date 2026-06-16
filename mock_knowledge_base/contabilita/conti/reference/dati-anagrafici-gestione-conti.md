---
title: Dati anagrafici della gestione Conti
doc_kind: reference
domain: contabilita
feature: conti
keywords:
  - conti
  - dati anagrafici
  - conto
  - tipo conto
  - cliente
  - fornitore
  - gestione partite
  - divise
  - codice fiscale
  - partita IVA
  - dichiarazione di intento
task_tags:
  - riferimento campi conti
  - configurazione conto
  - anagrafica conto
erp_versions:
  - v.1.0
role_scope:
  - amministrazione
  - contabilità
review_status: approved
module: Contabilita
screen_title: Conti
tab_name: Dati anagrafici
aliases:
  - anagrafica conti
  - pannello dati anagrafici conti
field_labels:
  - Conto
  - Sigla
  - Tipo conto
  - Raggruppamento di bilancio
  - Cliente
  - Fornitore
  - Percipiente
  - Gestione partite
  - Extra contabile
  - Tesoreria
  - Solo spedizione
  - Obsoleto
  - Divise
  - Descrizione
  - Ragione sociale
  - Indirizzo
  - CAP
  - Città
  - Provincia
  - Telefono
  - Fax
  - Email
  - Tipo cliente o fornitore
  - Sesso
  - Luogo di nascita
  - Provincia di nascita
  - Data di nascita
  - Codice fiscale
  - Codice fiscale estero
  - Partita IVA
  - Partita IVA estera
  - Modalità IVA
  - Nostra dichiarazione di intento
  - Vostra dichiarazione di intento
  - Sede amministrativa
  - Esclusioni interesse di mora
---
# Dati anagrafici della gestione Conti

Il pannello Dati anagrafici della gestione Conti consente di codificare e gestire i dati dei conti.

## Campi
### Conto
Contiene il codice univoco del conto, formato da 5 caratteri per il mastro e 4 caratteri per il partitario.

Quando viene creato un nuovo conto:
- se si digitano i 5 caratteri del mastro e si preme Invio, e il mastro non è già presente in Magia, i 4 caratteri successivi vengono impostati a 0000 e il conto viene riconosciuto come mastro
- se il mastro è già presente nel piano dei conti della società in cui si sta lavorando, Magia calcola automaticamente il progressivo successivo in base all'ultimo inserito

Il progressivo proposto da Magia è modificabile. Per gli inserimenti successivi, Magia considera come riferimento il progressivo più alto presente e propone quello successivo.

### Sigla
Permette di inserire una stringa utile per la ricerca tramite i filtri nelle varie applicazioni di gestione.

### Tipo conto
Deve essere inserito in base alla tipologia del conto.

Quando gli ultimi 4 caratteri del codice conto sono tutti zeri, il conto viene impostato di default come tipo conto 01 Mastro.

Per conti come:
- costi
- ricavi generici
- conti che non siano né clienti né fornitori e nemmeno conti effetti
- conto IVA

si può indicare il tipo conto 10 Partitario.

Per distinguere i clienti si può utilizzare:
- 15 per clienti non gestiti a partite
- 20 per clienti gestiti a partite

Per distinguere i fornitori si può utilizzare:
- 25 per fornitori non gestiti a partite
- 30 per fornitori gestiti a partite

### Raggruppamento di bilancio
Consente di inserire la sezione di appartenenza al bilancio:
- attività
- passività
- costi
- ricavi

### Cliente
Se impostato, indica che il conto è un cliente.

### Fornitore
Se impostato, indica che il conto è un fornitore.

### Percipiente
Si attiva qualora il conto sia stato indicato come Fornitore (flag) e permette di indicare se il fornitore è anche un percipiente, quindi un lavoratore o un collaboratore autonomo.

### Gestione partite
Indica se il conto deve essere gestito a partite all'interno di Magia.

### Extracontabile  
Consente di codificare un conto le cui movimentazioni non compaiono né a bilancio né nel libro giornale.  
  
È utilizzato tipicamente come conto di appoggio in registrazioni particolari, ad esempio:  
- fatture omaggio  
- bolle doganali  
  
Il flag è attivabile se nella tabella **Versioni di contabilità** è selezionato il parametro **Conti extracontabili**.  
  
Se il mastro del conto inserito è superiore a **90000**, il conto viene definito di default come extracontabile, ma l'impostazione è modificabile.

### Tesoreria
Indica se il conto rientra nelle elaborazioni del modulo di Tesoreria.

### Solo spedizione
Indica se il conto cliente è utilizzato solo per le spedizioni.

### Obsoleto
Può assumere la valenza sì oppure no.

Per i conti impostati come obsoleti:
- normalmente non appaiono di default nei filtri di ricerca
- viene dato un avviso qualora si tenti di registrare in contabilità un movimento con un conto di questo tipo

### Divise
La gestione delle divise permette di associare delle valute a un conto e indica quali valute il conto può gestire all'interno della contabilità o degli altri moduli di Magia.

Sono previste tre possibilità:
- non gestire alcuna divisa; in questo caso il conto viene movimentato solo in moneta di conto, quindi euro
- gestire alcune divise specifiche; oltre all'euro devono essere specificate le altre valute che il conto potrà gestire
- tutte; in questo caso non è necessario specificare singolarmente tutte le divise, perché Magia permette la gestione del conto in tutte le valute registrate nella tabella divise

### Descrizione o Ragione sociale
Per ogni conto sono disponibili due campi per l'inserimento della descrizione o della ragione sociale nel caso di clienti o fornitori.

I due campi hanno lunghezza di 60 caratteri ciascuno.

### Indirizzo
Contiene i dati dell'indirizzo del conto:
- via e numero civico
- CAP
- città
- provincia

### Telefono
Contiene un primo riferimento telefonico del conto.

### Fax
Contiene il numero di fax del conto.

### Email
Contiene l'indirizzo email del conto.

### Tipo cliente o fornitore
Permette di indicare se il cliente o il fornitore è:
- società
- persona fisica

Se viene selezionata la tipologia persona fisica, viene visualizzata anche una sezione con i dati della persona fisica.

### Sesso
Per la persona fisica è necessario indicare:
- maschio
- femmina

### Luogo e provincia di nascita
Per la persona fisica è necessario indicare il luogo e la provincia di nascita.

### Data di nascita
Per la persona fisica è necessario indicare la data di nascita.

### Codice fiscale
Contiene il codice fiscale del conto.

### Codice fiscale estero
Contiene il codice fiscale estero del conto.

### Partita IVA
Contiene l'identificativo fiscale italiano del conto.

### Partita IVA estera
Contiene l'identificativo fiscale estero del conto.

### Modalità IVA
Viene gestita manualmente e può contenere solo modalità IVA che non sono imponibili.

La modalità IVA in questo campo serve soprattutto per la gestione delle dichiarazioni di intento. Un conto cliente che ha impostata una certa modalità IVA genererà fatture e ordini con la modalità IVA specificata nel conto e potrà ricondurre eventuali dichiarazioni di intento inserite in Magia.

### Nostra dichiarazione di intento
Contiene un riferimento descrittivo alla nostra dichiarazione di intento emessa verso i fornitori.

### Vostra dichiarazione di intento
Contiene i riferimenti descrittivi delle eventuali dichiarazioni di intento ricevute dai clienti.

### Sede amministrativa
I campi relativi alla sede amministrativa possono essere utilizzati per indicare:
- via
- numero civico
- codice di avviamento postale
- città
- provincia

### Esclusioni interesse di mora
Consente di escludere il conto dalle applicazioni che calcolano gli interessi di mora sulle partite generate dalla gestione dei movimenti.

## Regole
### Creazione automatica di mastro e partitario
Se il mastro non esiste, Magia crea un conto con partitario 0000 e lo riconosce come mastro.

Se il mastro esiste già nella società corrente, Magia propone automaticamente il progressivo numerico successivo del partitario.

### Relazione tra codice conto e tipo conto
Un conto con ultimi 4 caratteri pari a 0000 è un mastro.

I conti con progressivo finale diverso da 0000 sono gestiti come partitario secondo la tipologia selezionata.

### Gestione clienti e fornitori a partite
Per distinguere i clienti e i fornitori gestiti o non gestiti a partite devono essere utilizzati i codici tipo conto specifici:
- 15 clienti non gestiti a partite
- 20 clienti gestiti a partite
- 25 fornitori non gestiti a partite
- 30 fornitori gestiti a partite

### Controlli esterni su indirizzo e identificativi fiscali
Tramite l'apposita icona accanto al campo Indirizzo è possibile verificare l'indirizzo con l'applicazione di geolocalizzazione di Google.

Accanto ai campi Partita IVA e Partita IVA estera è presente un pulsante con l'icona dell'Agenzia delle entrate che consente di verificare la correttezza dell'identificativo fiscale italiano oppure estero.