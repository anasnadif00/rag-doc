---
title: Duplica ordini
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - duplica ordini
  - duplicazione ordini
  - ordini clienti
  - copia ordine
  - tipo ordine
  - anno ordine
  - numero ordine
  - data ordine
  - cliente
  - divisa
  - data consegna
task_tags:
  - duplicazione ordine cliente
  - copia testata ordine
  - copia righe ordine
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Ordini Clienti
submenu: Elaborazioni
screen_title: Duplica ordini
aliases:
  - duplicazione ordini
field_labels:
  - Tipo ordine
  - Anno
  - Numero
  - Data
  - Cliente
  - Divisa
  - Data consegna
  - Tutto
---
# Duplica ordini

## Prerequisiti
Verifica di conoscere almeno uno o più elementi utili a filtrare l'ordine da duplicare, ad esempio tipo di ordine, anno, numero, data, codice cliente o divisa.

## Procedura
1. Apri l'elaborazione **Duplica ordini** dal modulo **Ordini Clienti**.
2. Nella parte sinistra della maschera imposta i filtri disponibili per individuare l'ordine da duplicare. I filtri principali sono **Tipo ordine**, **Anno**, **Numero**, **Data** ed eventualmente **Cliente** o **Divisa**.
3. Clicca sull'icona dell'**imbuto** per eseguire la ricerca.
4. Quando l'ordine compare nella parte destra della schermata, selezionalo con il **tasto verde** e conferma la selezione con il **visto verde**.
5. Nella sezione inferiore della maschera compila i parametri del nuovo ordine:
   6. **Tipo di ordine** da generare, che può anche essere diverso da quello dell'ordine originario.
   7. **Data** del nuovo ordine.
   8. **Data di consegna**, che resta obbligatoria.
9. Se il filtro ha restituito più ordini e devi duplicarli tutti, attiva il flag **Tutto** all'interno della maschera di duplica ordini. Questo flag consente di elaborare tutti gli ordini che soddisfano il filtro anche quando, per limiti fisici della maschera, non sono tutti visualizzabili e quindi non sono tutti selezionabili manualmente.
10. Clicca sul **martelletto** per lanciare l'elaborazione.
11. Conferma l'operazione richiesta dalla procedura.
12. Al termine dell'elaborazione, richiama il nuovo ordine dalla gestione ordini se devi effettuare ulteriori modifiche manuali.

## Verifiche finali
Verifica che:
1. Il nuovo ordine sia stato generato.
2. La testata e le righe risultino duplicate dall'ordine originario.
3. Il log riporti l'esito **duplicazione ordini** in assenza di errori.

## Note operative
Si consiglia di lasciare normalmente disattivato il flag **Tutto** e di lavorare con filtri di selezione più restrittivi, in modo da duplicare solo gli ordini effettivamente necessari.