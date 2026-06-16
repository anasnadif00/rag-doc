---
title: Stampare la lista ordini clienti
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - lista ordini
  - stampa lista ordini
  - ordini clienti
  - elenco ordini clienti
  - lista ordini clienti standard
  - PDF lista ordini
task_tags:
  - stampa lista ordini clienti
  - consultazione elenco ordini
  - invio elenco ordini
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - backoffice
review_status: approved
module: Ordini clienti
submenu: Stampe ordini
screen_title: Lista ordini
aliases:
  - elenco ordini clienti
  - stampa elenco ordini
field_labels:
  - cliente
  - tipo dell'ordine
  - da numero a numero
  - da data a data
---
# Stampare la lista ordini clienti

## Prerequisiti
Verificare di avere definito i criteri con cui selezionare gli ordini da includere nella stampa.

Se necessario, verificare quale formato di stampa deve essere utilizzato. In assenza di personalizzazioni, è disponibile il formato standard **lista ordini clienti**.

## Procedura
1. Aprire la stampa **Lista ordini** tra le stampe disponibili del modulo **Ordini clienti**.

2. Impostare i filtri di selezione presenti nella maschera. I principali filtri disponibili sono:
   - **cliente**;
   - **tipo dell'ordine**;
   - **da numero a numero**;
   - **da data a data**.

3. Selezionare la tipologia di ordini da includere nella stampa, scegliendo se stampare:
   - ordini **caricati**;
   - ordini **bloccati**;
   - ordini **confermati**;
   - ordini **evasi**;
   - oppure **tutti** gli ordini.

4. Selezionare il formato di stampa desiderato. Il formato standard disponibile è **lista ordini clienti**, salvo eventuali personalizzazioni richieste dal cliente.

5. Eseguire l'azione desiderata:
   - aprire il PDF cliccando sull'icona della stampante con la lente di ingrandimento;
   - stampare direttamente sulla stampante;
   - inviare tramite mail l'elenco degli ordini, se si desidera trasmetterlo a un cliente.

## Verifiche finali
Verificare che la stampa riporti gli ordini coerenti con i filtri impostati.

Se è stato scelto il PDF o l'invio mail, verificare che il documento generato corrisponda al formato di stampa selezionato.

## Contenuto della stampa
La stampa **Lista ordini** può riportare, per ciascun ordine, le seguenti informazioni:
- tipologia dell'ordine;
- data;
- data di evasione, se esistente;
- cliente;
- stato dell'ordine;
- cliente di intestazione di fatturazione;
- ragione sociale;
- eventuale categoria amministrativa;
- operatore che ha inserito l'ordine.