---
title: Duplica articolo a cliente
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - duplica articolo a cliente
  - articoli clienti
  - copia articoli cliente
  - cliente
  - codice articolo
  - codifica cliente
  - marca
task_tags:
  - duplicazione articoli cliente
  - copia articoli tra clienti
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Ordini Clienti
submenu: Elaborazioni
screen_title: Duplica articolo a cliente
aliases:
  - copia articoli clienti
field_labels:
  - Cliente
  - Codice articolo
  - Codifica cliente
  - Marca
---
# Duplica articolo a cliente

## Prerequisiti
Utilizza questa funzione quando devi copiare articoli già presenti nella tabella **articoli clienti** da un cliente origine a un cliente destinazione.

## Procedura
1. Apri l'elaborazione **Duplica articolo a cliente** dal modulo **Ordini Clienti**.
2. Imposta i filtri nella schermata per individuare gli articoli del cliente origine. I filtri disponibili comprendono:
   3. **Cliente**
   4. **Codice articolo**
   5. **Codifica cliente**
   6. **Marca**
7. Esegui la ricerca e visualizza nella griglia gli articoli che soddisfano i filtri impostati.
8. Seleziona gli articoli da duplicare utilizzando il **visto verde**.
9. Nella sezione parametri in basso indica il nuovo cliente a cui attribuire i dati duplicati.
10. Compila i parametri relativi ai dati da riportare sul cliente destinazione, compresi:
   11. Le **nuove codifiche**
   12. Il **codice articolo**
   13. Una **nuova codifica cliente**
   14. La **marca**
15. Clicca sul **martelletto** per lanciare l'elaborazione.

## Verifiche finali
Verifica che gli articoli selezionati siano stati copiati automaticamente nella tabella **articoli clienti** del nuovo cliente.

## Note operative
Questa elaborazione lavora su articoli già associati a un cliente e consente di trasferire rapidamente le relative codifiche commerciali verso un altro cliente senza reinserimento manuale.