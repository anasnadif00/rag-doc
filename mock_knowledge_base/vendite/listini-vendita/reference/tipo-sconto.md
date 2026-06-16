---
title: Tipo sconto
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - tipo sconto
  - priorità sconto
  - sconto in cascata
  - imponibile lordo
  - sconto di testata
  - sconto di listino in formazione
  - visibile sulle righe
  - maggiorazione
task_tags:
  - riferimento tipo sconto
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
field_labels:
  - Codice
  - Priorità
  - Base di applicazione
  - Valore
  - Sconto/maggiorazione
  - Maggiorazione
  - Sconto di testata
  - Sconto di listino in formazione
  - Visibile sulle righe
  - Riduzione imponibile provvigione
---
# Tipo sconto

## Regole

### Tabella trasversale
La tabella Tipo sconto consente di codificare tutte le tipologie di sconto utilizzate nei vari moduli della parte vendite.

È una tabella trasversale utilizzata da:
  Offerte clienti
- Ordini clienti
- Fatturazione
- Listini vendita

### Priorità di applicazione
La priorità definisce l'ordine di applicazione quando vengono richiamate più tipologie di sconto.

La priorità con progressivo più alto viene applicata per prima.

I valori 0 e 1 sono considerati i valori più alti e vengono quindi applicati per primi.

### Sconto in cascata
Se la base di applicazione indica lo sconto in cascata, in presenza di più sconti quelli successivi al primo vengono applicati sull'importo netto degli sconti precedentemente calcolati.

### Imponibile lordo
Se è attivata l'opzione Imponibile lordo, in presenza di più tipi di sconto tutti gli sconti vengono applicati sulla stessa base imponibile.

### Sconto o maggiorazione
Il tipo sconto può essere configurato come sconto oppure come maggiorazione.

Se è configurato come sconto, l'importo viene sottratto dall'imponibile.

Se è configurato come maggiorazione, l'importo viene sommato all'imponibile.

### Sconto di testata
Se il flag Sconto di testata è attivato, il tipo di sconto viene elencato nella testata dei documenti.

Lo sconto viene gestito nella testata di ordini, DDT e fatture e viene riportato a livello di riga articolo.

In questo caso lo sconto deve essere in percentuale.

### Sconto di listino 
Il flag Sconto di listino ha rilevanza solo nel modulo Listini vendita.

Se attivato, indica che il tipo di sconto viene elencato tra i tipi di sconto a quantità fissa della maschera principale del modulo Listini vendita.

### Visibilità sulle righe
Se il flag Visibile sulle righe è attivato, lo sconto viene elencato su tutte le righe dei documenti ed è visibile.

### Riduzione imponibile provvigione
Se il flag Riduzione imponibile provvigione è attivato, le provvigioni vengono applicate sull'importo delle righe al netto degli sconti calcolati.

## Campi

### Codice
Identifica il tipo di sconto.

### Priorità
Indica la priorità di applicazione quando vengono richiamate più tipologie di sconto.

### Base di applicazione
Definisce la base su cui applicare lo sconto.

Può determinare un comportamento di sconto in cascata oppure di applicazione sull'imponibile lordo.

### Valore
Indica se lo sconto viene applicato in percentuale oppure a valore.

### Sconto/maggiorazione
Se attivato, indica che l'importo dello sconto viene sottratto dall'imponibile.

### Maggiorazione
Se attivato, indica che l'importo viene calcolato sommando all'imponibile.

### Sconto di testata
Se attivato, abilita la gestione del tipo sconto nella testata dei documenti e il riporto sulle righe articolo.

### Sconto di listino 
Se attivato, rende il tipo sconto disponibile nei tipi di sconto a quantità fissa della maschera principale del modulo Listini vendita.

### Visibile sulle righe
Se attivato, rende il tipo sconto visibile ed elencato sulle righe dei documenti.

### Riduzione imponibile provvigione
Se attivato, le provvigioni sono calcolate sull'importo di riga al netto degli sconti calcolati.

## Combinazioni tra Visibile sulle righe e Sconto di testata

### Visibile sulle righe attivo e Sconto di testata attivo
Lo sconto è gestibile autonomamente sia sulla testata sia sulle righe.
Se lo sconto viene indicato in testata, viene ereditato anche dalle righe, ma resta modificabile.

### Visibile sulle righe attivo e Sconto di testata disattivato
Il tipo di sconto viene elencato solo sulle righe del documento.
È gestibile esclusivamente a livello di singola riga.

### Visibile sulle righe disattivato e Sconto di testata attivo
Lo sconto è gestibile solo dalla testata, ma viene calcolato sulle righe.
Se viene cancellato in testata, sparisce anche dalle righe.

### Visibile sulle righe disattivato e Sconto di testata disattivato
Questa combinazione non è significativa.
Il tipo di sconto non sarebbe comunque utilizzabile.