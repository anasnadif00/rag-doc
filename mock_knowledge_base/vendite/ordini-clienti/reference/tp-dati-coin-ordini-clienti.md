---
title: TP Dati COIN degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - TP Dati COIN
  - contabilità industriale ordine cliente
  - dati COIN ordine
  - periodo competenza
  - tipi di destinazione
task_tags:
  - riferimento TP Dati COIN ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP Dati COIN
field_labels:
  - Da data
  - A data
---
# TP Dati COIN degli Ordini clienti

## Campi

### Da data
Campo sempre attivo nel quale è possibile inserire l'inizio del periodo di competenza.

### A data
Campo sempre attivo nel quale è possibile inserire la fine del periodo di competenza.

### Campi per tipi di destinazione
Se il TP Dati COIN è impostato nella tabella **Tipo ordine cliente**, si attivano ulteriori campi in relazione al numero di tipi di destinazione previsti in tabella.

## Regole

### Finalità del tab
Il TP Dati COIN consente di inserire e gestire le informazioni di contabilità industriale che verranno riprese nei passaggi successivi all'ordine.

### Ripresa nei documenti successivi
Le informazioni inserite nel TP Dati COIN possono essere riprese in:
- DDT
- fatture
- contabilità generale

### Periodo di competenza
I campi **Da data** e **A data** consentono di definire il periodo di competenza utile per eventuali futuri ratei e risconti generati a partire dall'ordine.

### Propagazione alle righe
Le informazioni del TP Dati COIN vengono riprese anche nelle righe dell'ordine e possono essere successivamente modificate a livello di articolo.

### Valori proposti
I valori possono essere proposti automaticamente in base alle impostazioni della tabella **Tipo ordine cliente**, mantenendo comunque la possibilità di modifica.
