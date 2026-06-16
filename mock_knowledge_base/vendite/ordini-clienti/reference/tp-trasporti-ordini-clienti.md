---
title: TP Trasporti degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - TP Trasporti
  - trasporto ordine cliente
  - vettore
  - cura trasporto
  - spese ordine
  - tipo fatturato
  - aliquota IVA
task_tags:
  - riferimento TP Trasporti ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: review
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP Trasporti
field_labels:
  - Cura trasporto
  - Vettore
  - Tipo fatturato
  - Modalità
  - Aliquota IVA
  - Importo
  - Analitica
---
# TP Trasporti degli Ordini clienti

## Campi

### Cura trasporto
Consente di specificare la modalità con cui viene eseguito il trasporto della merce.

I valori gestiti sono:
- a cura del mittente
- a cura del destinatario
- a cura del vettore

### Vettore
Se nel tab dati commerciali dell'anagrafica del conto è presente un vettore, il campo viene proposto automaticamente, con possibilità di modifica.

Tp Spese
### Tipo fatturato
Consente di definire la tipologia di spesa aggiuntiva da addebitare all'ordine.

### Modalità
Definisce la modalità associata alla spesa.

### Aliquota IVA
Definisce l'aliquota IVA da applicare alla spesa.

### Importo
Indica l'importo della spesa aggiuntiva.

### Analitica
Può essere indicata se prevista.

## Regole

### Proposta del vettore
Il vettore può essere ripreso automaticamente dall'anagrafica del conto oppure inserito direttamente in fase di ordine.

### Gestione spese aggiuntive
Il TP Trasporti consente anche di aggiungere spese aggiuntive all'ordine.

### Derivazione di modalità e aliquota IVA
I campi **Modalità** e **Aliquota IVA**, se non indicati manualmente, vengono desunti dalla tabella **Tipi di fatturato** in base al tipo fatturato selezionato.

### Proposta automatica delle spese
Le spese possono essere proposte automaticamente o riprese dalla precedente offerta, in base a quanto impostato:
- nella tabella **Tipo ordine cliente**
- nell'anagrafica del conto