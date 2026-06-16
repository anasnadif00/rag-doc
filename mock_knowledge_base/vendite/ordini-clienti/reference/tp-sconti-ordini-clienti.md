---
title: TP Sconti degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - TP Sconti
  - sconti ordine cliente
  - sconti di testata
  - sconti visibili sulle righe
  - riepilogo sconti
  - ricerca sconti
task_tags:
  - riferimento TP Sconti ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP Sconti
aliases:
  - riepilogo sconti ordine
---
# TP Sconti degli Ordini clienti

## Campi

### Tipi di sconto
Nel TP Sconti è possibile inserire sconti di tipologia diversa, che devono essere preventivamente impostati nella tabella **Parametri del commerciale**.

### Percentuale
Per gli sconti che prevedono una percentuale esplicita, il valore inserito viene applicato secondo le regole del tipo sconto.

### Riepilogo sconti non visibile sulle righe
Contiene tutti i tipi di sconto presenti nella tabella **Parametri del commerciale** per i quali, nella tabella **Tipo sconto**, non è attiva l'opzione **Visibile sulle righe**.

## Regole

### Sconti di testata
Gli sconti di testata sono i tipi di sconto per i quali nella tabella **Tipo sconto** è attiva l'opzione **Sconto di testata**. In questo caso la percentuale inserita viene applicata automaticamente su tutte le righe.

### Assenza di percentuale esplicita
Se non è presente alcuna percentuale, significa che esistono regole di applicazione degli sconti specifiche per ogni articolo. In questo caso è necessario controllare nel TP Sconti della riga la percentuale effettivamente applicata.

### Sconti non visibili sulle righe
Nel riepilogo sconti non visibile sulle righe viene esposto solo il valore calcolato e non la percentuale applicata, perché tale percentuale potrebbe essere diversa per ogni riga d'ordine.

### Ricerca automatica degli sconti
Gli sconti proposti vengono ricercati in relazione all'impostazione della tabella **Ricerca sconti**.