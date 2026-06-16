---
title: Stampare il portafoglio a valore
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - portafoglio a valore
  - stampa portafoglio a valore
  - portafoglio ordini clienti
  - ordini a valore
  - portafoglio ordini excel
  - portafoglio ordini pdf
task_tags:
  - stampa portafoglio a valore
  - analisi valore ordini
  - controllo portafoglio ordini clienti
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - backoffice
review_status: approved
module: Ordini clienti
submenu: Stampe ordini
screen_title: Portafoglio a valore
aliases:
  - portafoglio ordini a valore
  - stampa portafoglio ordini a valore
field_labels:
  - da data a data
  - da numero a numero
  - da articolo a articolo
  - categoria merceologica
  - cliente
  - agente
  - categoria amministrativa
  - categoria commerciale
  - tipologie dell'ordine
  - zona
  - commessa
  - nazioni
  - cliente
  - ragioni sociali
  - ordine
  - articolo
---
# Stampare il portafoglio a valore

## Prerequisiti
Verificare i criteri di selezione degli ordini da includere nel portafoglio.

Se necessario, verificare se deve essere utilizzato il formato standard oppure un formato personalizzato richiesto dal cliente.

## Procedura
1. Aprire la stampa **Portafoglio a valore** tra le stampe disponibili del modulo **Ordini clienti**.

2. Impostare i filtri di selezione disponibili nella maschera. I principali filtri sono:
   - **da data a data**;
   - **da numero a numero**;
   - **da articolo a articolo**;
   - **categoria merceologica**;
   - **cliente**;
   - **agente**;
   - **categoria amministrativa**;
   - **categoria commerciale**;
   - **tipologie dell'ordine**;
   - **zona**;
   - **commessa**, se gestita;
   - **nazioni**.

3. Nel filtro **nazioni**, scegliere una delle modalità disponibili:
   - **tutte**, per considerare tutti gli ordini in essere;
   - **Italia**, per estrarre solo gli ordini dei clienti senza nazione in anagrafica oppure con nazione avente codice ISO uguale a quello indicato nella tabella **Società**, campo **codice ISO nazione**;
   - **Estero**, per estrarre gli ordini dei clienti che hanno in anagrafica una qualsiasi nazione diversa da quella il cui codice ISO è indicato nella tabella **Società**, campo **codice ISO nazione**.

4. Impostare l'ordinamento desiderato. La stampa consente ordinamenti diversi per:
   - **cliente**;
   - **ragioni sociali**;
   - **ordine**;
   - **articolo**.

5. Selezionare la tipologia di ordini da riportare nel portafoglio. È possibile scegliere:
   - **tutti gli ordini**;
   - **quelli non stampati**;
   - **quelli stampati e non evasi**;
   - **stampati e evasi**;
   - **ordini bloccati**;
   - **ordini stampati e non evasi e bloccati**;
   - **ordini annullati**.

6. Se necessario, attivare le opzioni aggiuntive disponibili:
   - escludere le **righe evase forzatamente** tramite l'apposito flag;
   - stampare le **note dell'ordine** all'interno del portafoglio.

7. Selezionare il formato di output desiderato:
   - formato **PDF** standard;
   - formato **PDF** personalizzato, se richiesto dal cliente;
   - formato **Excel**.

1. Eseguire la stampa o l'esportazione del portafoglio a valore. E' possibile aprire il pdf sempre dall'icona lente di ingrandimento, stampare cliccando su stampante o inviare per mail cliccando su icona e-mail.

## Verifiche finali
Verificare che gli ordini riportati siano coerenti con i filtri impostati.

Controllare che l'ordinamento corrisponda al criterio selezionato.

Se è stata richiesta l'esclusione delle righe evase forzatamente o la stampa delle note, verificare che tali opzioni siano state applicate correttamente.

Se è stato generato un file Excel, verificare che i dati siano completi e utilizzabili per ulteriori elaborazioni.

## Contenuto della stampa
La stampa **Portafoglio a valore** riporta, per ogni ordine o riga prodotta, le seguenti informazioni:
- estremi dell'ordine;
- cliente;
- nazione;
- zona;
- agente;
- divisa;
- stato dell'ordine;
- quantità ordinata;
- valore ordinato;
- quantità consegnata;
- valore consegnato.

## Riepilogo finale
Alla fine della stampa è riportato un riepilogo per **divisa** con i seguenti valori:
- **valore ordinato**;
- **valore consegnato**;
- **valore evaso forzatamente**;
- **valore residuo**.

## Regole di selezione per nazione
Se nel filtro **nazioni** si seleziona **Italia**, vengono estratti:
- gli ordini dei clienti che non hanno una nazione impostata in anagrafica;
- gli ordini dei clienti che hanno una nazione con codice ISO uguale a quello indicato nella tabella **Società**, campo **codice ISO nazione**.

Se nel filtro **nazioni** si seleziona **Estero**, vengono estratti gli ordini dei clienti che hanno in anagrafica una qualsiasi nazione diversa da quella il cui codice ISO è indicato nella tabella **Società**, campo **codice ISO nazione**.