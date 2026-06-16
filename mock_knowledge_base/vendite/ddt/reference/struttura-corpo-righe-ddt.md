---
title: Struttura del corpo righe DDT
doc_kind: reference
domain: vendite
feature: ddt
keywords:
  - DDT
  - righe DDT
  - corpo DDT
  - ripresa ordine
  - TP articolo
  - TP dati aggiuntivi
task_tags:
  - riferimento corpo righe DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
  - magazzino
review_status: approved
module: Vendite
screen_title: DDT
field_labels:
  - Codice articolo
  - Articolo cliente
  - Magazzino
  - Prezzo
  - Colli
---
# Struttura del corpo righe DDT

## Regole

### Inserimento delle righe
Dopo l'inserimento della testata del DDT è possibile inserire le righe del documento.

Le righe possono essere create in due modi:

- tramite ripresa dell'ordine;
- manualmente, tramite il tasto `+` verde.

### Ripresa dell'ordine
Se viene utilizzata la ripresa dell'ordine, le righe vengono precompilate automaticamente dal programma riprendendo le righe presenti nell'ordine.

Le righe riprese dall'ordine restano modificabili in tutti i loro campi.

### Inserimento manuale
Se non viene utilizzata la ripresa dell'ordine, l'operatore può inserire manualmente una nuova riga tramite il tasto `+` verde.

### TP del corpo DDT
Il corpo del DDT è formato dai seguenti TP:

- TP articolo;
- TP dati aggiuntivi;
- TP dati di analitica;
- TP agenti;
- TP pagamenti;
- TP sconti;
- TP note.

### Compilazione automatica dei TP
La maggior parte dei TP viene compilata automaticamente:

- con i dati presenti in testata;
- con i dati ripresi dall'ordine, se il DDT deriva da una ripresa ordine.

I dati proposti automaticamente possono essere modificati dove previsto dalla procedura.