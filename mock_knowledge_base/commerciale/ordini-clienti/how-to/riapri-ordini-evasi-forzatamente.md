---
title: Riapri ordini evasi forzatamente
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - riapertura ordini evasi forzatamente
  - riapri ordini
  - evaso forzatamente
  - stato ordine
  - tipo ordine
  - ragione sociale
task_tags:
  - riapertura ordine cliente
  - annullamento evasione forzata
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Ordini Clienti
submenu: Elaborazioni
screen_title: Riapertura ordini evasi forzatamente
aliases:
  - riapertura ordini
field_labels:
  - Tipo
  - Numero
  - Anno
  - Data
  - Cliente
  - Ragione sociale
  - Stato
---
# Riapri ordini evasi forzatamente

## Prerequisiti
Utilizza questa elaborazione solo per ordini precedentemente **evasi in maniera forzata**. La funzione non riguarda gli ordini collegati a documenti di trasporto.

## Procedura
1. Apri l'elaborazione **Riapertura ordini evasi forzatamente** dal modulo **Ordini Clienti**.
2. Nella parte sinistra della maschera imposta i filtri di ricerca. Tra i filtri citati sono disponibili:
   3. **Tipo**
   4. **Numero**
   5. **Anno**
   6. **Data**
   7. **Cliente**
   8. **Ragione sociale**
   9. **Stato**, impostando il criterio relativo agli ordini evasi forzatamente
10. Clicca sull'icona dell'**imbuto** per visualizzare gli ordini che rientrano nella selezione.
11. Evidenzia gli ordini trovati con il **tasto verde**.
12. Clicca sul **martelletto** per lanciare l'elaborazione di riapertura.

## Verifiche finali
Verifica che, al termine dell'elaborazione:
1. Gli ordini selezionati risultino riaperti.
2. Gli ordini non si trovino più nello stato di **evaso forzatamente**.

## Note operative
La funzione interviene esclusivamente sugli ordini chiusi tramite evasione forzata e permette di riportarli in uno stato riutilizzabile per le successive lavorazioni.