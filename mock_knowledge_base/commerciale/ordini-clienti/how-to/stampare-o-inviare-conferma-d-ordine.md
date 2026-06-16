---
title: Stampare o inviare la conferma d'ordine
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - conferma d'ordine
  - stampa conferma d'ordine
  - invio mail ordine
  - ordini da stampare
  - stampa provvisoria
  - stampa definitiva
  - PDF ordine
  - ordine confermato
task_tags:
  - stampa conferma d'ordine
  - invio conferma d'ordine
  - conferma ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - backoffice
review_status: approved
module: Ordini clienti
submenu: Stampa conferma d'ordine
screen_title: Stampa conferma d'ordine
aliases:
  - conferma ordine
  - stampa ordine
field_labels:
  - ordini
---
# Stampare o inviare la conferma d'ordine

## Prerequisiti
Verificare di avere individuato gli ordini da elaborare tramite i filtri di selezione disponibili nella maschera di stampa.

Se è richiesto l'uso della modalità definitiva, considerare che l'ordine verrà confermato e potrà essere trattato dai processi successivi.

Se nella tabella **Parametri di controllo fido della fatturazione con il cliente** è attivo il controllo fido online, la stampa definitiva è soggetta a tale controllo.

## Procedura
1. Aprire la funzione **Stampa conferma d'ordine**.

2. Scegliere da quale contesto lanciare la stampa:
   - dal menu principale a sinistra della maschera **ordini**, per stampare uno o più ordini usando i filtri;
   - dalla navigazione dell'ordine aperto, per predisporre automaticamente la stampa sul numero dell'ordine che si sta inserendo o modificando.

3. Impostare i filtri per selezionare gli ordini da elaborare. In base all'esigenza, è possibile filtrare per numero ordine, data o cliente.

4. Nelle opzioni di stampa, valorizzare il flag **ordini** scegliendo una delle modalità disponibili:
   - tutti;
   - la tipologia di ordini desiderata;
   - solo quelli **da stampare**, cioè quelli non ancora stampati in definitivo.

5. Selezionare la modalità di emissione:
   - **provvisoria**, se si vuole produrre una stampa non definitiva;
   - **definitiva**, se si vuole confermare il documento.

1. Selezionare il formato di stampa previsto. I formati disponibili dipendono dalle personalizzazioni predisposte in base alle esigenze del cliente e sono selezionabili dal campo formato.

2. Eseguire una delle azioni disponibili:
   - aprire il documento in PDF cliccando su **apri** dall'icona della stampante con la lente di ingrandimento;
   - stampare direttamente sulla stampante cliccando sul simbolo di stampa;
   - inviare il documento via mail cliccando sull'icona **email**.

8. Se si sceglie l'invio via mail, compilare i dati richiesti:
   - destinatario della posta;
   - eventuali indirizzi in copia conoscenza;
   - oggetto;
   - messaggio email, se già predisposto nelle relative tabelle.

## Verifiche finali
Verificare che il documento sia stato prodotto nel canale scelto: PDF, stampa diretta oppure email.

Se la stampa è stata eseguita in modalità **definitiva**, controllare che l'ordine abbia assunto lo stato di **confermato**.

## Effetti della stampa definitiva
Con la stampa definitiva della conferma d'ordine, l'ordine assume lo stato di **confermato**.

Un ordine confermato:
- può essere trattato dal processo produttivo;
- può essere trattato dalle spedizioni per la generazione dei relativi documenti di trasporto;
- non può essere annullato né totalmente né parzialmente.

Se occorre intervenire su un ordine già confermato, è necessario procedere con una modifica dello stato, se consentita.