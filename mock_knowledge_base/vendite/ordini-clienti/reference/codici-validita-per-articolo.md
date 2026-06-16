---
title: Tabella Codici validità per articolo
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - Codici validità per articolo
  - validità articolo
  - articolo spese
  - articolo non codificato
  - obsoleto
  - movimentabile
  - schedulabile
  - codificatore articoli
task_tags:
  - configurazione validità articolo
  - classificazione articolo
  - gestione articoli ordini clienti
erp_versions:
  - v.1.0
role_scope:
  - operatore ordini clienti
  - magazzino
  - produzione
  - configuratore
review_status: approved
module: Ordini clienti
screen_title: Codici validità per articolo
aliases:
  - validità articolo
  - codice validità articolo
field_labels:
  - Codice
  - Descrizione
  - Obsoleto
  - Macro Ciclo
  - Movimentabile
  - Non movimentato considera inventario
  - Neutro
  - Previsionale
  - Schedulabile
  - Numeri dei caratteri del progressivo
  - Caratteri dell'articolo base
  - Caratteri parlanti
---
# Tabella Codici validità per articolo

## Regole

### Utilizzo dei codici validità
La tabella "Codici validità per articolo" consente di definire le validità di un articolo.
Le validità assegnate definiscono il comportamento dell'articolo nei diversi moduli nei quali viene utilizzato.

La tabella permette quindi di definire tipologie di articolo, ad esempio articoli spese, articoli non codificati o articoli generici da utilizzare nell'inserimento di offerte e ordini.

### Codifica automatica articoli
La tabella consente anche di definire elementi utili alla codifica automatica degli articoli per chi utilizza il codificatore per codificare nuovi articoli.

Gli elementi indicati sono:
- numeri dei caratteri del progressivo
- caratteri dell'articolo base
- caratteri parlanti

## Campi

### Codice
Identifica il codice di validità dell'articolo.

Il codice è scelto dall'utente.

### Descrizione
Descrive la validità dell'articolo.

Esempi indicati:
- "spese", se si tratta di un articolo spese
- "articolo non codificato", se si vogliono identificare articoli generici usati nell'inserimento di offerte o ordini e di cui descrizione modificabile

### Obsoleto
Flag che indica che l'articolo non deve più essere proposto nei vari help perché risulta disabilitato.

### Macro Ciclo
Flag che permette di simulare i carichi dei centri di lavoro.

I carichi possono essere generati dagli ordini pianificati che non verranno mai rilasciati in produzione.

### Movimentabile
Flag che indica che l'articolo viene movimentato a magazzino.

Un articolo movimentabile determina anche giacenza.

### Non movimentato considera inventario
Flag che indica che l'articolo non viene movimentato ma deve comunque essere considerato a giacenza.

### Neutro
Flag che identifica una tipologia di articolo utilizzata solo come elemento base per il codificatore.

### Previsionale
Flag che permette di creare un ordine pianificato derivante da domanda indipendente.

I criteri dell'ordine pianificato saranno poi gli articoli effettivi da produrre.

### Schedulabile
Flag da utilizzare quando l'articolo deve essere schedulato nella schedulazione MRP.

### Numeri dei caratteri del progressivo
Campo utilizzato nella configurazione della codifica automatica degli articoli.

### Caratteri dell'articolo base
Campo utilizzato nella configurazione dell'articolo base per la codifica automatica.

### Caratteri parlanti
Campo utilizzato nella codifica automatica degli articoli tramite codificatore.