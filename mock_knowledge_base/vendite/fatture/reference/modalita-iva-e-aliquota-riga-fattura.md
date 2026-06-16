---
title: Modalità IVA e aliquota IVA della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - modalità iva fattura
  - aliquota iva fattura
  - iva riga fattura
  - tipo fatturato vendita
  - nomenclatura combinata
task_tags:
  - riferimento iva riga fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Dati Aggiuntivi
field_labels:
  - Modalità IVA
  - Aliquota IVA
  - Tipo fatturato
---
# Modalità IVA e aliquota IVA della riga fattura

## Campi

### Modalità IVA
Indica la tipologia di assoggettamento IVA da applicare alla singola riga della fattura.

### Aliquota IVA
Indica l'aliquota IVA da applicare quando la riga è soggetta a IVA.

## Regole

### Proposta modalità IVA per beni materiali
Se l'articolo è un bene materiale, viene proposta la modalità IVA presente nell'anagrafica del cliente di spedizione.

### Proposta modalità IVA per servizi
Se l'articolo è un servizio, viene proposta la modalità IVA presente nell'anagrafica del cliente di fatturazione.

### Determinazione natura articolo
La natura del bene viene determinata in base alla nomenclatura combinata dell'articolo.

### Ordine di ricerca modalità IVA
Se nelle anagrafiche clienti non è indicata la modalità IVA, il programma ricerca il valore in questo ordine:
1. anagrafica articolo, se l'articolo è codificato
2. tabella tipo fatturato di vendita per cliente
3. tabella tipo fatturato di vendita

Se non viene trovato alcun valore, la modalità IVA deve essere inserita manualmente.

### Ricerca manuale modalità IVA
La modalità IVA può essere selezionata tra i valori disponibili in tabella tramite tasto destro del mouse.

### Ordine di ricerca aliquota IVA
L'aliquota IVA viene proposta in questo ordine:
1. anagrafica articolo, se l'articolo è codificato
2. tabella tipo fatturato di vendita per cliente
3. tabella tipo fatturato di vendita

Se non viene trovato alcun valore, l'aliquota IVA deve essere inserita manualmente.

### Ricerca manuale aliquota IVA
L'aliquota IVA può essere selezionata tra i valori disponibili in tabella tramite tasto destro del mouse.