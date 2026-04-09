---
title: Campi principali delle righe offerta
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - riga offerta
  - campi riga offerta
  - numero riga
  - codice articolo
  - descrizione
  - valore
  - quantità
  - quantità vendita
  - quantità prezzo
  - quantità gestionale
  - colli
  - prezzo
  - omaggi
  - data concordata
  - tassativa
  - data consegna
task_tags:
  - riferimento campi righe offerta
  - compilazione righe offerta
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Offerte
screen_title: Offerte
field_labels:
  - Numero riga
  - Codice articolo
  - Descrizione
  - Valore
  - Quantità
  - Quantità vendita
  - Quantità prezzo
  - Quantità gestionale
  - Colli
  - Prezzo
  - Omaggi
  - Data concordata
  - Tassativa
  - Data consegna
---
# Campi principali delle righe offerta

## Campi
### Numero riga
È il progressivo della riga. Viene proposto automaticamente dal sistema ma può essere modificato dall'utente.

### Codice articolo
Identifica l'articolo da inserire nella riga. Può essere richiamato digitando:
- il codice completo;
- una parte del codice;
- una parte della descrizione.

Il programma ricerca l'articolo nell'anagrafica di magazzino e propone i risultati selezionabili.

### Descrizione
Per gli articoli codificati di magazzino viene proposta automaticamente e non è modificabile.

Per gli articoli generici non codificati la descrizione è libera e può essere modificata dall'utente.

### Valore o Quantità
È la tendina che definisce il tipo di evasione della riga. Serve a indicare se l'evasione dovrà avvenire a valore oppure a quantità nei documenti successivi.

### Quantità vendita
È una quantità non obbligatoria.

### Quantità prezzo
È la quantità utilizzata per il calcolo del valore della riga, perché viene moltiplicata per il prezzo inserito.

### Quantità gestionale
È la quantità obbligatoria. Viene proposta in automatico dal sistema sulla base dell'anagrafica articolo e non è modificabile.

### Colli
Consente di indicare i colli associati alla riga articolo. Se il dato è presente nei dati tecnici dell'anagrafica articoli, il valore viene calcolato automaticamente. 

### Prezzo
È il prezzo dell'articolo in offerta. Normalmente viene proposto automaticamente se sono presenti listini. In assenza di listini può essere inserito manualmente.

### Omaggi
Consente di indicare la quantità di eventuali omaggi associati alla riga.

### Data concordata
Permette di registrare una data di consegna concordata con il cliente. È usata normalmente per esigenze interne e non per esposizione in stampa.

### Tassativa
È un flag che rende tassativa la data concordata con il cliente.

### Data consegna
È la data di consegna della riga. È un dato obbligatorio per poter confermare la riga e l'offerta.

## Regole
### Ricerca articolo
L'articolo deve essere presente nell'anagrafica di magazzino se si vuole usare un articolo codificato.

### Descrizione modificabile
La descrizione è modificabile solo per articoli generici non codificati, per le spese e per le note.

### Quantità proposte automaticamente
Se nell'anagrafica articolo non sono state specificate quantità vendita e quantità prezzo, il sistema le propone normalmente uguali alla quantità gestionale se impostata la sincronizzazione sull'anagrafica articolo.

### Obbligatorietà del prezzo
Il prezzo è obbligatorio nei seguenti casi:
- se nell'anagrafica articolo, nel TP dati gestionali, è impostata l'opzione **solo fatturazione**;
- se nella tabella **TPI offerta di vendita** non è attivata l'opzione **articolo senza prezzo**.

### Obbligatorietà della data consegna
La **Data consegna** deve essere compilata per poter confermare la riga o la conferma complessiva dell'offerta.