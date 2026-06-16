---
title: Ricalcola ordini in M3
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - ricalcolo ordini
  - ricalcola ordini in m3
  - magia cube
  - importi ordini
  - ordine codice conto
  - esito
task_tags:
  - ricalcolo importi ordini
  - riallineamento ordini
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Ordini Clienti
submenu: Elaborazioni
screen_title: Ricalcolo ordini in M3
aliases:
  - ricalcolo ordini in Magia Cube
field_labels:
  - Tipo ordine
  - Anno
  - Ordine numero
  - Ordine codice conto
  - Descrizione cliente
  - Esito
---
# Ricalcola ordini in M3

## Prerequisiti
Utilizza questa elaborazione quando gli importi degli ordini risultano calcolati o modificati in modo non corretto da procedure esterne e devono essere riallineati.

## Procedura
1. Apri l'elaborazione **Ricalcolo ordini in M3** dal modulo **Ordini Clienti**.
2. Imposta i filtri per individuare gli ordini da ricalcolare. I filtri citati sono:
   3. **Tipo ordine**
   4. **Anno**
   5. **Ordine numero**
   6. **Ordine codice conto**
   7. **Descrizione cliente**
   8. **Esito**
9. Clicca sull'icona dell'**imbuto** per visualizzare gli ordini che soddisfano i criteri impostati.
10. Seleziona gli ordini trovati.
11. Evidenzia i record selezionati con il **flag verde**.
12. Clicca sul **martelletto** per lanciare l'elaborazione di ricalcolo.

## Verifiche finali
Verifica che l'elaborazione abbia aggiornato e riallineato gli importi degli ordini selezionati rispetto alle modifiche sopraggiunte successivamente.

## Note operative
La funzione è utile quando il totale ordine o altri importi risultano incoerenti a seguito di interventi esterni al normale flusso applicativo.