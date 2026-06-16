---
title: Campi e regole del TP IVA
doc_kind: reference
domain: commerciale
feature: fatture-vendita
keywords:
  - tp iva
  - riepilogo iva
  - aliquote iva
  - modalità iva
  - prezzo iva compresa
  - scorporo iva
task_tags:
  - riferimento iva fattura
erp_versions:
  - v.1.0
role_scope:
  - amministrazione
review_status: approved
module: Fatture
tab_name: IVA
---
# Campi e regole del TP IVA

## Campi

### Modalità IVA
Riepiloga le modalità IVA utilizzate nelle righe della fattura.

### Aliquota IVA
Riepiloga le aliquote IVA utilizzate nelle righe della fattura.

### Imponibile
Importo imponibile calcolato per ciascuna combinazione di modalità IVA e aliquota.

### Imposta
Importo IVA calcolato.

### Omaggi
Eventuali importi relativi a omaggi presenti nel documento.

## Regole

### Riepilogo IVA
Nel TP IVA vengono riepilogate tutte le modalità IVA e le aliquote IVA utilizzate nella fattura con i relativi imponibili e imposte.

### Gestione prezzi IVA compresa
Quando è attivo il flag "Prezzo IVA compresa", i prezzi inseriti nelle righe articolo devono essere considerati comprensivi dell'IVA.

In questo caso il sistema esegue automaticamente lo scorporo dell'imposta e calcola correttamente imponibile e IVA.

### Modifica dei riepiloghi IVA
I dati riepilogativi presenti nel TP IVA sono modificabili.

Le modifiche effettuate vengono propagate automaticamente a tutte le righe che utilizzano la stessa combinazione di:

- modalità IVA
- aliquota IVA