---
title: Tabella Errori (contabilità)
doc_kind: reference
domain: contabilita
feature: errori-contabilita
keywords:
  - errori contabilità
  - tabella errori
  - brogliaccio
  - inserimento movimenti
  - correzione movimenti
  - errori bloccanti
  - errori non bloccanti
  - da stampare
task_tags:
  - riferimento tabella errori contabilità
  - configurazione controlli contabilità generale
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Errori (contabilità)
aliases:
  - Errori contabilità
  - tabella Errori
field_labels:
  - Bloccante
  - Da stampare
error_codes:
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  - 9
  - 12
  - 13
  - 14
  - 15
  - 16
  - 17
  - 20
  - 102
  - 103
  - 104
  - 300
  - 301
  - 302
  - 404
  - 700
  - 701
  - 702
---
# Tabella Errori (contabilità)

La tabella Errori (contabilità) contiene la codifica per la gestione degli errori trattati dalla Contabilità Generale.

## Campi
### Bloccante
Attraverso il campo Bloccante è possibile selezionare uno dei seguenti comportamenti da richiedere a Magia:

- Sì: l'errore è considerato bloccante ai fini della conferma dei dati della registrazione o del controllo di correttezza da parte del Brogliaccio.
- No, ma avviso: l'errore viene rilevato ai fini della conferma dei dati della registrazione e del controllo di correttezza da parte del Brogliaccio, tuttavia ne viene dato solo un avviso.
- Ignora: l'errore viene ignorato ai fini della conferma dei dati della registrazione o del controllo di correttezza da parte del Brogliaccio.

### Da stampare
Se il flag Da stampare è attivato, l'errore viene evidenziato nella stampa del Brogliaccio.

## Regole
### Codici errore predefiniti
I codici di errore sono fissati a priori.

Non è possibile definire nuovi codici o annullare codici esistenti.

### Ambiti di utilizzo
I codici fanno riferimento a due ambiti:

- elaborazione del Brogliaccio
- inserimento e correzione movimenti

### Gestione nel Brogliaccio
Per gli errori utilizzati dal Brogliaccio è possibile stabilire:
- se devono essere considerati bloccanti o meno ai fini del consolidamento movimenti
- se devono essere stampati o meno

### Gestione in inserimento e correzione movimenti
In inserimento e correzione movimenti, se si verifica una condizione di errore, viene in ogni caso visualizzato il codice con la relativa descrizione.

La segnalazione viene trattata:
- come semplice avviso se l'errore è classificato come non bloccante
- come condizione da sanare obbligatoriamente se l'errore è classificato come bloccante

### Codici storici
I codici indicati come Non gestito si riferiscono a codifiche utilizzate nelle versioni del gestionale precedenti a Magia3, rimaste visibili per motivi di storicità e compatibilità.

## Codici di errore
### 001 - Tipo doc. errato
Non gestito.

### 002 - Data doc. errata
Non gestito.

### 003 - Numeri IVA div.
Nella stessa registrazione sono presenti movimenti con numeri di protocollo IVA diversi.

### 004 - Date doc. diverse
Nella stessa registrazione IVA sono presenti movimenti con date di documento diverse.

### 005 - Mod. IVA errata
In sede di registrazione di un movimento IVA manca la modalità IVA.

### 006 - Aliquota IVA errata
In sede di registrazione di un movimento IVA avente modalità IVA imponibile, cioè modalità IVA inferiore a 50, manca l'aliquota IVA.

### 007 - Compet. IVA diverse
Singole righe di una stessa registrazione riportano competenze IVA diverse.

### 008 - Num. reg. errato
Il sistema riscontra anomalie nella sequenza dei numeri di registrazione all'interno di una stessa data.

### 009 - Num. 1 errata
Il sistema riscontra errori nella sequenza di numerazione dei documenti per le registrazioni il cui tipo documento prevede in tabella una numerazione controllata.

Esempi:
- sequenza protocolli errata per le fatture di acquisto
- sequenza numero documento errata per le fatture di vendita

### 012 - Data valuta errata
Non gestito.

### 013 - Comp. IVA mancante
Nella registrazione di un movimento con IVA ad esigibilità immediata manca la data di competenza IVA.

### 014 - Comp. IVA errata
In una registrazione di sole fatture di vendita con IVA ad esigibilità immediata, la competenza IVA non corrisponde al mese/anno di registrazione o al mese/anno precedente.

### 015 - Imp. IVA err.
L'importo dell'IVA presente nella registrazione non corrisponde all'importo imponibile moltiplicato per l'aliquota, arrotondato alla cifra superiore.

### 016 - Tipo doc. err.
La registrazione presenta un tipo documento con attribuito in tabella un tipo numerazione o un tipo IVA errati.

### 017 - Conto inesist.
Non gestito.

### 020 - Cod. div. err.
Non gestito.

### 102 - Doc. rif. inesistente
Non gestito.

### 103 - Data doc. mancante
Non gestito.

### 104 - Importo movim. = 0
Non gestito.

### 300 - Prot. occupato
In fase di gestione movimenti si tenta di attribuire un numero di protocollo IVA già utilizzato.

### 301 - Protocollo non in sequenza
In fase di gestione movimenti il protocollo IVA attribuito non è corretto, in quanto esiste un documento con numero o data di registrazione successivo e numero di protocollo IVA inferiore a quello in fase di inserimento.

### 302 - Protocollo non in sequenza sulla data
In fase di gestione movimenti il protocollo IVA attribuito non è corretto, in quanto esiste un documento con numero o data di registrazione inferiore e numero di protocollo IVA superiore a quello in fase di inserimento.

### 404 - Imp. iva errato
In fase di gestione movimenti si tenta di concludere una registrazione in cui i movimenti relativi all'IVA non corrispondono agli importi imponibili moltiplicati per le relative aliquote.

### 700 - La registrazione non quadra
Il totale dare e il totale avere della registrazione sono diversi.

### 701 - Più righe totale documento
Sulla registrazione è presente più di una riga impostata come Totale documento.

### 702 - Manca la riga di totale documento
Sulla registrazione non è presente la riga definita come Totale documento, ma l'impostazione del tipo documento la richiede.