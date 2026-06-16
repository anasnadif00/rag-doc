---
title: Arrotondamento divisa
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - arrotondamento divisa
  - duplica listini
  - aggiornamento listini
  - prezzo unitario
  - precisione arrotondamento
task_tags:
  - riferimento arrotondamento divisa
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
field_labels:
  - Divisa
  - Prezzo unitario
---
# Arrotondamento divisa

## Regole

### Utilizzo dell'arrotondamento divisa
La tabella Arrotondamento divisa viene utilizzata nelle funzioni di duplica listini e aggiornamento listini.

Consente di indicare, per una divisa, l'importo massimo a livello di prezzo unitario fino al quale applicare una determinata precisione di arrotondamento.

### Applicazione per fasce di importo
Per ogni configurazione è possibile indicare il valore fino al quale deve essere applicata la precisione di arrotondamento.

In questo modo il sistema può gestire arrotondamenti diversi in base al valore del prezzo unitario.

## Campi

### Divisa
Identifica la divisa per la quale viene configurato l'arrotondamento.

La tabella consente di filtrare le divise presenti.

### Importo massimo
Indica il valore massimo del prezzo unitario fino al quale applicare la precisione di arrotondamento configurata.

### Precisione di arrotondamento
Indica la precisione di arrotondamento da applicare fino all'importo massimo indicato.

## Note operative

### Inserimento di un arrotondamento
Per aggiungere un arrotondamento si utilizza il tasto più verde.

Dopo aver impostato il valore fino al quale applicare la precisione di arrotondamento, la configurazione deve essere salvata con la freccia verde.