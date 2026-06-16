---
title: Pannello Dettaglio del corpo della Contabilità Generale
doc_kind: reference
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - righe movimento
  - pannello dettaglio corpo
  - conto
  - contropartita
  - divisa
  - importo valuta
  - cambio
  - segno
  - causale
  - data valuta
  - data scadenza
  - nota
task_tags:
  - riferimento righe contabili contabilità generale
  - gestione dettaglio corpo
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Contabilità Generale
tab_name: Dettaglio
field_labels:
  - Riga
  - Conto
  - Contropartita
  - Divisa
  - Importo valuta
  - Cambio
  - Segno
  - Importo
  - Causale
  - Data valuta
  - Data scadenza
  - Nota
---
# Pannello Dettaglio del corpo della Contabilità Generale

Il pannello Dettaglio del corpo gestisce le righe della registrazione contabile.

## Campi
### Riga
La colonna è visualizzata solo nella griglia e non è modificabile dall'utente.

Serve a identificare il tipo di riga del movimento e può assumere i seguenti valori:
- Mov: identifica tutte le righe inserite manualmente per qualsiasi tipo di registrazione
- Tot: identifica la riga del totale del movimento per le registrazioni IVA di fatture e note di credito; contiene solitamente il cliente o il fornitore del documento IVA, viene proposta automaticamente per i tipi documento IVA e non può essere eliminata
- Iva: identifica la riga inserita in automatico che contiene il conto IVA a credito o IVA a debito per i tipi documento con IVA acquisti o vendite; il conto viene desunto dalla tabella Tipo documento
- Auto: identifica le righe create in automatico dai tipi documento che hanno impostato la chiusura partite e i conti compilati nella tabella Parametri conti automatismi partite; ad esempio righe di ritenuta o di abbuono.

### Conto
È il partitario movimentato.

### Contropartita
Non è obbligatoria, salvo che sia attivato il relativo flag nella tabella Versioni di contabilità.

Il suo inserimento consente di:
- utilizzare la funzione di duplica
- fungere da filtro nella lista parametrica movimenti
- avere una descrizione più completa della registrazione nelle stampe contabili

### Divisa
È la valuta in cui il conto è gestito oppure quella indicata come default in anagrafica.

Non possono essere movimentati conti con divise diverse nella stessa registrazione.

### Importo valuta
È l'importo espresso nella divisa indicata nel campo Divisa.

### Cambio
Viene applicato il cambio inserito nella tabella Divisa per la data corrispondente alla Data documento se nel Tipo documento è attivato il parametro Cambio su data documento.

Se il parametro è disattivato viene preso il cambio alla Data registrazione.

Se per la data inserita non esistono cambi in tabella Divisa, viene preso il cambio della data immediatamente precedente.

### Segno
È il segno della riga di registrazione:
- Dare
- Avere

### Importo
Indica l'importo in euro della riga.

Se la registrazione è in divisa, viene indicato il controvalore in euro dell'Importo valuta.

### Causale
Consente di dare una descrizione sintetica della riga del movimento.

È obbligatoria solo se nella tabella Versioni di contabilità è attivato il flag Causale obbligatoria.

Viene proposta la descrizione del Tipo documento se nella tabella Versioni di contabilità non è attivato il flag Descrizione conto su causale contropartita.

Se invece tale flag è attivato, sui movimenti relativi all'imponibile e all'IVA viene proposta la descrizione del cliente o del fornitore.

La causale proposta può essere modificata:
- richiamando una causale codificata nella tabella Causali movimento
- inserendo una descrizione personalizzata

### Data valuta
È obbligatoria quando il conto movimentato ha attivato in anagrafica il flag Tesoreria.

Viene presa come data di riferimento nell'elaborazione della proiezione finanziaria.

### Data scadenza
Il campo è visibile e attivo solo per i tipi documento aventi Natura documento impostata a Effetti.

Consente di indicare la data di scadenza dell'effetto se diversa da quella della partita associata alla registrazione.

Tale data viene utilizzata per il calcolo dell'esposizione cambiaria nella stampa dell'estratto conto.

### Nota
Consente di indicare una descrizione più completa della riga del movimento.

## Regole
### Tipi di riga automatici
Le righe Tot, Iva e Auto vengono generate automaticamente in funzione del Tipo documento e delle impostazioni collegate.

### Gestione divisa
All'interno della stessa registrazione non è possibile movimentare conti con divise diverse.

### Obbligatorietà della Causale
La Causale è obbligatoria solo se previsto dalla tabella Versioni di contabilità.

### Riferimento della Data valuta
La Data valuta è rilevante per la proiezione finanziaria quando il conto è gestito con il flag Tesoreria.