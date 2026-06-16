---
title: Esempi di compilazione documenti da anagrafica cliente
doc_kind: reference
domain: commerciale
feature: compilazione-documenti
keywords:
  - anagrafica cliente
  - cliente di spedizione
  - cliente di fatturazione
  - luogo di destinazione
  - ordini clienti
  - proposte di spedizione
  - buoni di spedizione
  - documenti di trasporto
  - fatturazione
task_tags:
  - riferimento compilazione documenti commerciale
erp_versions:
  - v.1.0
role_scope:
  - utente
review_status: approved
module: Commerciale
field_labels:
  - Cliente
  - Cliente di fatturazione
  - Cliente di spedizione
  - Luogo di destinazione
---
# Esempi di compilazione documenti da anagrafica cliente

## Regole
### Ambito
Gli esempi seguenti mostrano come l'impostazione dell'anagrafica cliente, dei relativi luoghi clienti di spedizione e dei clienti di fatturazione influenzi la compilazione dei documenti nei moduli del commerciale.

## Esempi
### Esempio 1
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione non impostato
- luogo di destinazione non impostato
- cliente di fatturazione non impostato

Ordini clienti:
- pannello Testata:
  - il conto riportato sarà ABC SRL
- pannello Dati spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente di spedizione indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL, via Roma 3, Milano

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà ABC SRL
- il luogo di destinazione indicato sarà ABC SRL, via Roma 3, Milano

Buoni di spedizione, pannello Dati di spedizione:
- il cliente di spedizione indicato sarà ABC SRL
- il cliente di fatturazione indicato sarà ABC SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL, via Roma 3, Milano

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati spedizioni:
  - il cliente di spedizione indicato sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL, via Roma 3, Milano

### Esempio 2
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione non indicato
- luogo di destinazione: ABC SRL, deposito merci, via della Ferriera, Brescia
- cliente di fatturazione non indicato

Ordini clienti:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente di spedizione indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera Brescia

Proposte di spedizione, pannello Tipo Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà ABC SRL
- il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera Brescia

Buoni di spedizione, pannello Dati:
- il cliente di spedizione indicato sarà ABC SRL
- il cliente di fatturazione indicato sarà ABC SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera Brescia

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di spedizione indicato sarà ABC SRL
  - il cliente d'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera Brescia

### Esempio 3
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione: 00020-0002, ragione sociale XYZ S.P.A., via Parigi 4, Bergamo
- nessuna indicazione in anagrafica di luogo di spedizione per il cliente di spedizione
- luogo di destinazione non indicato
- cliente di fatturazione non indicato

Ordini clienti:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente di spedizione indicato sarà XYZ S.P.A.
  - il luogo di destinazione indicato sarà XYZ S.P.A. via Parigi 4 Bergamo

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà XYZ S.P.A.
- il luogo di destinazione indicato sarà XYZ S.P.A. via Parigi 4 Bergamo

Buoni di spedizione, pannello Dati:
- il cliente di spedizione indicato sarà XYZ S.P.A.
- il cliente di fatturazione indicato sarà ABC SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà XYZ S.P.A.
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ S.P.A. via Parigi 4 Bergamo

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di spedizione indicato sarà XYZ S.P.A.
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ S.P.A. via Parigi 4 Bergamo

### Esempio 4
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione indicato con codice 00020-0002, ragione sociale XYZ S.P.A., via Parigi 4, Bergamo
- luogo di spedizione indicato in anagrafica del cliente di spedizione: Magazzino Centrale, Strada Statale 251, Bergamo
- luogo di destinazione non indicato
- cliente di fatturazione non indicato

Ordini clienti:
- pannello Testata:
  - il codice cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente di spedizione indicato sarà XYZ S.P.A.
  - il luogo di destinazione indicato sarà Magazzino Centrale, Strada Statale 251, Bergamo

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà XYZ S.P.A.
- il luogo di destinazione indicato sarà Magazzino Centrale, Strada Statale 251, Bergamo

Buoni di spedizione, pannello Dati:
- il cliente di spedizione indicato sarà XYZ SPA
- il cliente di fatturazione indicato sarà ABC SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà XYZ SPA
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà Magazzino Centrale, Strada Statale 251, Bergamo

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati di spedizione:
  - il cliente di spedizione indicato sarà XYZ SPA
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà Magazzino Centrale, Strada Statale 251, Bergamo

### Esempio 5
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione indicato con codice 00020-0002, ragione sociale XYZ S.P.A., via Parigi 4, Bergamo
- nessuna indicazione in anagrafica di luogo di spedizione per il cliente di spedizione
- luogo di destinazione indicato: ABC SRL, deposito merci, via della Ferriera, Brescia
- cliente di fatturazione non indicato

Ordini clienti:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente di spedizione indicato sarà XYZ S.P.A.
  - il luogo di destinazione indicato sarà XYZ S.P.A., via Parigi 4, Bergamo

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà XYZ S.P.A.
- il luogo di destinazione indicato sarà XYZ S.P.A., via Parigi 4, Bergamo

Buoni di spedizione, pannello Dati:
- il cliente di spedizione indicato sarà XYZ S.P.A.
- il cliente di fatturazione indicato sarà ABC SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà XYZ S.P.A.
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ S.P.A., via Parigi 4, Bergamo

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di spedizione indicato sarà XYZ S.P.A.
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ S.P.A., via Parigi 4, Bergamo

### Esempio 6
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione indicato con codice 00020-0002, ragione sociale XYZ S.P.A., via Parigi 4, Bergamo
- luogo di spedizione indicato in anagrafica del cliente di spedizione: Magazzino Centrale, Strada Statale 251, Bergamo
- luogo di destinazione: ABC SRL, deposito merci, via della Ferriera, Brescia
- cliente di fatturazione non indicato

Ordini clienti:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati spedizione:
  - il cliente di fatturazione indicato sarà ABC SRL
  - il cliente di spedizione indicato sarà XYZ SPA
  - il luogo di destinazione indicato sarà XYZ SPA, Magazzino Centrale, Strada Statale 251, Bergamo

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà XYZ SPA
- il luogo di destinazione indicato sarà XYZ SPA, Magazzino Centrale, Strada Statale 251, Bergamo

Buoni di spedizione, pannello Dati:
- il cliente di spedizione indicato sarà XYZ SPA
- il cliente di fatturazione indicato sarà ABC SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà XYZ SPA
- pannello Dati di spedizione:
  - il cliente di fatturazione sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ SPA, Magazzino Centrale, Strada Statale 251, Bergamo

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati spedizione:
  - il cliente di spedizione sarà XYZ SPA
  - il cliente dell'ordine sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ SPA, Magazzino Centrale, Strada Statale 251, Bergamo

### Esempio 7
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione non indicato
- luogo di destinazione non indicato
- cliente di fatturazione codice 00020-0003, ragione sociale DEF SRL, piazza Roma 5, Lecco

Ordini clienti:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati spedizione:
  - il cliente di fatturazione indicato sarà DEF SRL
  - il cliente di spedizione indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL via Roma 3 Milano

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà ABC SRL
- il luogo di destinazione indicato sarà ABC SRL via Roma 3 Milano

Buoni di spedizione, pannello Dati:
- il cliente di spedizione indicato sarà ABC SRL
- il cliente di fatturazione indicato sarà DEF SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati spedizione:
  - il cliente di fatturazione indicato sarà DEF SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL via Roma 3 Milano

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà DEF SRL
- pannello Dati spedizione:
  - il cliente di spedizione indicato sarà ABC SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL via Roma 3 Milano

### Esempio 8
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione non indicato
- luogo di destinazione: ABC SRL, deposito merci, via della Ferriera, Brescia
- cliente di fatturazione codice 00020-0003, ragione sociale DEF SRL, piazza Roma 5, Lecco

Ordini clienti:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati spedizione:
  - il cliente di fatturazione indicato sarà DEF SRL
  - il cliente di spedizione indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera, Brescia

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine indicato sarà ABC SRL
- il cliente di spedizione indicato sarà ABC SRL
- il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera Brescia

Buoni di spedizione, pannello Dati:
- il cliente di spedizione indicato sarà ABC SRL
- il cliente di fatturazione indicato sarà DEF SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà DEF SRL
  - il cliente dell'Ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera Brescia

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà DEF SRL
- pannello Dati Spedizione:
  - il cliente di spedizione sarà ABC SRL
  - il cliente dell'Ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà ABC SRL Deposito Merci via della Ferriera Brescia

### Esempio 9
Anagrafica cliente:
- codice 00020-0001
- ragione sociale ABC SRL, via Roma 3, Milano
- cliente di spedizione codice 00020-0002, ragione sociale XYZ SPA, via Parigi 4, Bergamo
- luogo di destinazione non indicato
- cliente di fatturazione codice 00020-0003, ragione sociale DEF SRL, piazza Roma 5, Lecco

Ordini clienti:
- pannello Testata:
  - il cliente indicato sarà ABC SRL
- pannello Dati di spedizione:
  - il cliente di fatturazione indicato sarà DEF SRL
  - il cliente di spedizione indicato sarà XYZ SPA
  - il luogo di destinazione indicato sarà XYZ SPA via Parigi 4 Bergamo

Proposte di spedizione, pannello Ordine:
- il cliente dell'ordine sarà ABC SRL
- il cliente di spedizione sarà XYZ SPA
- il luogo di destinazione indicato sarà XYZ SPA via Parigi 4 Bergamo

Buoni di spedizione, pannello Dati:
- il cliente di spedizione sarà XYZ SPA
- il cliente di fatturazione indicato sarà DEF SRL

Documenti di trasporto:
- pannello Testata:
  - il cliente indicato sarà XYZ SPA
- pannello Dati Spedizione:
  - il cliente di fatturazione indicato sarà DEF SRL
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ SPA via Parigi 4 Bergamo

Fatturazione:
- pannello Testata:
  - il cliente indicato sarà DEF SRL
- pannello Dati Spedizione:
  - il cliente di spedizione indicato sarà XYZ SPA
  - il cliente dell'ordine indicato sarà ABC SRL
  - il luogo di destinazione indicato sarà XYZ SPA via Parigi 4 Bergamo