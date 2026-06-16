---
title: Campi della tabella Tipi numerazione movimenti
doc_kind: reference
domain: contabilita
feature: tipi-numerazione-movimenti
keywords:
  - tipi numerazione movimenti
  - tipo numerazione
  - numerazione documenti IVA
  - controllo protocollo
  - controllo numero documento
  - formato numero documento
  - controllo sequenza numerazione
task_tags:
  - riferimento tipi numerazione movimenti
  - configurazione numerazione documenti iva
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità
screen_title: Tipi numerazione movimenti
aliases:
  - tabella Tipi numerazione movimenti
  - tipo numerazione e movimenti
field_labels:
  - Tipo numerazione
  - Controllo
  - Formato
  - Controllo sequenza numerazione
---
# Campi della tabella Tipi numerazione movimenti

La tabella **Tipi numerazione movimenti** contiene la lista delle codifiche delle diverse tipologie di numerazione da utilizzare all'interno della contabilità generale relativamente ai tipi di documento IVA.

Per ogni tipologia di numerazione occorre impostare il controllo sul numero del documento oppure sul numero di protocollo assegnato, a seconda che si tratti di documenti emessi o ricevuti.

## Campi

### Tipo numerazione
Identifica in modo univoco la tipologia di numerazione.

Il campo può contenere al massimo 2 caratteri.

### Controllo
Consente di specificare il tipo di dato a cui si appoggia la tipologia di numerazione per i relativi controlli.

Il controllo può essere impostato:
- sul **protocollo** per i documenti di acquisto
- sul **numero documento** per i documenti di vendita

Le opzioni selezionabili sono:

- **Protocollo**
- **Documento per anno o sezionale / documento per anno**  
  In questo caso il numero documento è formato:
  - dal solo numero, formattato o meno, ad esempio `000025`
  - oppure dal sezionale e dal numero, formattato o meno, ad esempio `S/000025`
- **Documento per anno / sezionale**  
  In questo caso il numero documento è formato dal numero e dal sezionale, formattati o meno, ad esempio `000025/S`

### Formato
Definisce la modalità di formattazione del numero documento.

Le tipologie di formato previste sono:

- **Senza formato**
- **Numerico**, impostando ad esempio `000000` oppure `000000-00`
- **Alfanumerico**, impostando ad esempio `cccccc` oppure `cccccc-cc`
- **Numerico-Alfanumerico**, impostando ad esempio `000000-cc`
- **Alfanumerico-Numerico**, impostando ad esempio `cccccc-00`

Il formato può contenere al massimo 16 caratteri.

### Controllo sequenza numerazione
Consente di impostare la tipologia di controllo di sequenzialità da applicare alla numerazione.

I valori selezionabili sono:

- **Nessuno**: non viene effettuato alcun controllo
- **Per mese**: la sequenzialità viene controllata all'interno del mese di registrazione
- **Per data**: la sequenzialità viene controllata all'interno della data di registrazione

## Regole

### Unicità del tipo numerazione
Ogni tipologia di numerazione deve essere identificata da un valore univoco nel campo **Tipo numerazione**.

### Lunghezza massima del tipo numerazione
Il campo **Tipo numerazione** può contenere al massimo 2 caratteri.

### Ambito di utilizzo
Le codifiche della tabella **Tipi numerazione movimenti** sono utilizzate per i **tipi di documento IVA**.

### Regola di controllo per acquisti e vendite
Il campo **Controllo** deve essere impostato in funzione della tipologia di documento:
- per i documenti di acquisto il controllo avviene sul **protocollo**
- per i documenti di vendita il controllo avviene sul **numero documento**

### Struttura del numero documento
Se il controllo è impostato su una modalità basata sul documento, il numero documento può essere costruito:
- con il solo numero
- con il **sezionale/numero**
- con il **numero/sezionale**

La struttura effettiva dipende dall'opzione selezionata nel campo **Controllo**.

### Lunghezza massima del formato
Il campo **Formato** può contenere al massimo 16 caratteri.

### Tipologie di formato ammesse
Il campo **Formato** può essere definito solo secondo una delle seguenti tipologie:
- **Senza formato**
- **Numerico**
- **Alfanumerico**
- **Numerico-Alfanumerico**
- **Alfanumerico-Numerico**

### Regole del controllo sequenza numerazione
Il campo **Controllo sequenza numerazione** determina l'ambito del controllo di sequenzialità della numerazione:
- con **Nessuno** non viene applicato alcun controllo
- con **Per mese** il controllo viene eseguito all'interno del mese di registrazione
- con **Per data** il controllo viene eseguito all'interno della data di registrazione