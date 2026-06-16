---
title: Evadi ordini forzatamente
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - evasione ordini
  - evadi ordini
  - evasione forzata
  - ordini non evasi
  - stato ordine
  - operatore
  - il nostro riferimento
  - il vostro riferimento
task_tags:
  - evasione forzata ordine cliente
  - chiusura ordine senza ddt
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Ordini Clienti
submenu: Elaborazioni
screen_title: Evasione ordini
aliases:
  - evadi ordini
field_labels:
  - Stato
  - Operatore
  - Tipo ordine
  - Numero
  - Data al cliente
  - Indirizzo
  - Provincia
  - Data inserimento ordine
  - Il nostro riferimento
  - Il vostro riferimento
---
# Evadi ordini forzatamente

## Prerequisiti
Utilizza questa elaborazione per gli ordini che non vengono evasi o non saranno evasi da un DDT e che devono quindi essere chiusi con evasione forzata.

## Procedura
1. Apri l'elaborazione **Evasione ordini** dal modulo **Ordini Clienti**.
2. Nella parte sinistra della schermata imposta i filtri disponibili per restringere la selezione degli ordini da evadere. Tra i filtri citati sono disponibili:
   3. **Stato**
   4. **Operatore**
   5. **Tipo ordine**
   6. **Numero**
   7. **Data al cliente dell'ordine**
   8. Campi di intestazione del cliente come **Indirizzo**, **Provincia** e **Data di inserimento dell'ordine**
   9. Campi come **Il nostro riferimento** e **Il vostro riferimento**
10. Clicca sull'icona dell'**imbuto** per visualizzare nella parte destra gli ordini che rientrano nei criteri impostati.
11. Seleziona gli ordini da elaborare nella parte destra della maschera.
12. Clicca su **Evadi** per eseguire l'evasione forzata delle righe degli ordini selezionati.

## Verifiche finali
Verifica che:
1. Le righe degli ordini selezionati risultino evase forzatamente.
2. Gli ordini restino bloccati in stato di evasione.
3. Non siano più consentite correzioni o annullamenti sull'ordine, così da mantenere traccia dell'operazione eseguita.

## Note operative
L'elaborazione consente di operare con tutti i filtri disponibili nella videata, quindi è consigliabile utilizzarli in modo mirato per evitare di evadere ordini non desiderati.