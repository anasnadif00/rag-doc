---
title: TP IVA, TP Pesi, TP Attributi, TP Note, TP Allegati e TP Mail inviate degli Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - TP IVA
  - TP Pesi
  - TP Attributi
  - TP Note
  - TP Allegati
  - TP Mail inviate
  - note commerciali ordine
  - allegati ordine
task_tags:
  - riferimento tab accessori ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
tab_name: TP IVA
aliases:
  - tab accessori ordine cliente
field_labels:
  - Modalità IVA
  - Aliquota IVA
  - Imponibile
  - Imposta
  - Omaggi
  - Colli
  - Volume
  - Peso netto
  - Peso lordo
---
# TP IVA, TP Pesi, TP Attributi, TP Note, TP Allegati e TP Mail inviate degli Ordini clienti

## Campi

### TP IVA
Nel TP IVA vengono riepilogate:
- modalità IVA
- aliquote IVA
- imponibili totali
- imposte totali
- eventuali omaggi

I campi non sono modificabili perché vengono ricalcolati in base ai dati inseriti nelle righe dell'ordine.

### TP Pesi
Riporta eventualmente i dati relativi a:
- colli
- volume
- peso netto
- peso lordo

I valori vengono riepilogati in relazione a quanto inserito nel TP dati tecnici dell'anagrafica articolo. I campi possono essere gestiti anche manualmente.

### TP Attributi
Consente di assegnare all'ordine caratteristiche ulteriori rispetto ai dati gestiti negli altri tab. L'attributo deve essere inserito nella tabella Caratteristiche Attributi.

### TP Note
Consente di inserire note:
- manualmente
- richiamandole per argomento

Le note possono essere di tipologia diversa in base alle impostazioni della tabella **TP nota**.

### TP Allegati
Consente di associare uno o più documenti all'ordine.

### TP Mail inviate
Consente di memorizzare le mail inviate per l'ordine.

## Regole

### Ricalcolo del TP IVA
I dati del TP IVA dipendono dalle righe dell'ordine e non sono modificabili manualmente.

### Attivazione del TP Attributi
L'attivazione della sezione attributi avviene tramite l'impostazione della tabella **Caratteristiche attributi**, nella quale vengono definiti gli attributi disponibili per l'ordine.

### Tipologie di note
Nel TP Note le note possono essere:
- di testata
- di riga

Possono inoltre essere associate ad argomenti preimpostati, richiamabili tramite il numero dell'argomento.

### Ripresa note commerciali del conto
Se nell'anagrafica del conto intestatario dell'ordine, nel TP **Note commerciali**, sono presenti note per le quali è prevista la ripresa o la stampa negli ordini, tali note vengono proposte automaticamente con possibilità di modifica.

### Attivazione ripresa note
La ripresa delle note commerciali del conto dipende dalle impostazioni del tipo nota utilizzato nella tabella **Tipo nota cliente**./tp-iva-pesi-attributi-note-allegati-mail-ordini-clienti.md