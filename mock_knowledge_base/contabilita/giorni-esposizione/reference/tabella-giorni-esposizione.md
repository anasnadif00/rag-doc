---
title: Tabella Giorni esposizione
doc_kind: reference
domain: contabilita
feature: giorni-esposizione
keywords:
  - giorni esposizione
  - tabella giorni esposizione
  - estratto conto
  - esposizione cambiaria
  - effetti in circolazione
  - data scadenza
task_tags:
  - riferimento tabella
  - configurazione estratto conto
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
screen_title: Giorni esposizione
aliases:
  - giorni esposizione
field_labels:
  - Numero di giorni
---
# Tabella Giorni esposizione

La tabella Giorni esposizione viene utilizzata nell'estratto conto per evidenziare l'esposizione cambiaria, cioè gli effetti ancora in circolazione.

Questa gestione consente di considerare effetti già contabilizzati ma non ancora scaduti.

## Campi

### Numero di giorni
Indica il numero di giorni da utilizzare nel calcolo dell'esposizione cambiaria nell'estratto conto.

Il valore deve essere indicato con il segno meno.

## Regole

### Utilizzo nell'estratto conto
La tabella è utilizzata dall'estratto conto per determinare gli effetti ancora in circolazione alla data richiesta.

### Segno del valore
Il numero di giorni deve essere sempre inserito con segno negativo.

Questo consente di anticipare il confronto con la data di scadenza e includere correttamente gli effetti nell'esposizione cambiaria.

### Criterio di estrazione alla data odierna
Se viene richiesto l'estratto conto alla data odierna, vengono estratte tutte le scadenze registrate che rispettano entrambe le condizioni seguenti:

- data registrazione inferiore alla data odierna
- data scadenza superiore alla data odierna più i Giorni esposizione

### Finalità del calcolo
L'utilizzo dei Giorni esposizione permette di evidenziare nell'estratto conto gli effetti contabilizzati ma non ancora scaduti, mantenendoli tra le partite esposte come esposizione cambiaria.