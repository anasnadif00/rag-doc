---
title: Campi della riga ordine cliente
doc_kind: reference
domain: commerciale
feature: ordini-clienti
keywords:
  - campi riga ordine
  - quantità ordine
  - prezzo ordine
  - sconti ordine
  - date ordine cliente
task_tags:
  - riferimento campi ordine
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: review
module: Commerciale
screen_title: Ordini clienti
aliases:
  - dettaglio riga ordine
field_labels:
  - Articolo
  - Quantità
  - Prezzo
  - Importo netto
  - Data consegna
source_uri: :contentReference[oaicite:1]{index=1}
---
# Campi della riga ordine cliente

## Campi

### Numero riga
Progressivo identificativo della riga. Proposto automaticamente ma modificabile.

### Articolo
Codice dell’articolo da inserire. Può essere selezionato tramite ricerca per descrizione o per codice.

### Quantità e valore
Determina la modalità di evasione:
- a quantità → gestione evasione a quantità,
- a valore → gestione evasione su importo.

### Descrizione articolo
Descrizione dell’articolo proposta automaticamente per gli articoli codificati, . Modificabile per articoli non codificati altrimenti non modificabile.

### Unità di misura
- Gestionale: unità misura principale di magazzino.
- Vendita: unità misura utilizzata dal cliente.
- Prezzo: unità misura su cui è espresso il prezzo.

### Quantità
- Inseribile in una delle unità disponibili.
- Le altre vengono calcolate automaticamente in base ai fattori di conversione o sincronizzate se previsto in anagrafica articolo.

### Colli
Numero di colli calcolato in relazione alle impostazioni in anagrafica articolo. Può determinare automaticamente la quantità gestionale se configurato.

### Prezzo
Prezzo unitario espresso nell’unità di misura di prezzo.
Può essere:
- Proposto da listino,
- Recuperato da anagrafica articolo.

### Importo lordo
Calcolato come quantità × prezzo.

### Sconti
Fino a tre percentuali inseribili con operatori (+ / -).
Gestiti anche nel tab sconti con classificazione per tipo.

### Importo netto
Calcolato automaticamente applicando gli sconti all’importo lordo.

### Articolo cliente
Codice articolo utilizzato dal cliente.

### Date
- Data richiesta
- Data concordata
- Data confermata (se attivo controllo disponibilità)
- Data consegna (obbligatoria)

### Flag tassativo
Indica vincolo sulla data di consegna concordata ma è solo informativo.

### Tipologia articolo
Determinata automaticamente:
- articolo
- non codificato
- spesa
- note

## Tab Dati aggiuntivi

### Marca
Marca di vendita dell’articolo. Può influenzare il prezzo.

### Magazzino
Magazzino di scarico per la riga.

### Imballo
Tipo imballo proposto dalle condizioni ordine.

### Tipo fatturato
Determina il conto contabile in fatturazione.

### Modalità IVA
Determinata in base a:
- natura articolo (bene/servizio),
- tipo fatturato inserito nell'articolo
- cliente spedizione o fatturazione,
- anagrafica articolo o tabelle.

### Aliquota IVA
Aliquota applicata alla riga.

### Vostro riferimento
Campo libero per riferimento cliente.

## Tab Date cons. log
Memorizza lo storico modifiche apportate alle data di consegna e data concordata.
- data modifica
- operatore
- valore precedente e nuovo

## Tab Dati spedizioni

### Cliente di spedizione
Può differire dalla testata.

### Luogo di destinazione
Associato al cliente di spedizione.

## Tab Dati analitica

### Data competenza
Utilizzata per ratei e risconti.

### Dati CO.IN
Campi variabili in base alla configurazione tipo ordine relativamente alle destinazioni impostate.

## Tab Agenti
Provvigioni derivate da:
- anagrafica cliente
- articoli
- tabelle provvigionali

## Tab Pagamenti
Condizioni di pagamento della riga:
- scadenza
- tipo imputazione (percentuale o valore)

## Tab Sconti
Riepilogo dettagliato degli sconti:
- visibili in riga → inclusi nell’importo netto della riga
- non visibili → riepilogati solo in testata e nel totale ordine

## Tab Note
Inserimento note libere o predefinite associate alla riga.

## Regole

### Calcolo quantità
Le quantità sono convertite automaticamente tramite fattori di conversione articolo.

### Obbligatorietà prezzo
Il prezzo è obbligatorio se previsto da:
- tipo ordine cliente
- configurazione articolo

### Data consegna obbligatoria
Ogni riga deve avere una data di consegna valorizzata.

### Determinazione IVA
Segue una priorità:
1. Cliente spedizione o fatturazione
2. Anagrafica articolo
3. Tipo fatturato
4. Inserimento manuale