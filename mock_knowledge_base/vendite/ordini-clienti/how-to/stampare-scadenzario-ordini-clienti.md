---
title: Stampare lo scadenzario ordini clienti
doc_kind: how_to
domain: vendite
feature: ordini-clienti
keywords:
  - scadenzario ordini clienti
  - consegne previste
  - consegne in ritardo
  - consegne effettuate
  - ordini clienti
  - stampa scadenzario
  - residuo ordine
task_tags:
  - stampa scadenzario ordini
  - verifica consegne ordini clienti
  - controllo ordini in ritardo
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - vendite
  - logistica
review_status: approved
module: Ordini
screen_title: Scadenzario ordini clienti
aliases:
  - scadenzario ordini
field_labels:
  - Cliente
  - Tipo ordine
  - Da numero ordine
  - A numero ordine
  - Da data
  - A data
  - Da articolo
  - A articolo
  - Da agente
  - A agente
  - Commessa
  - Consegne previste
  - Consegne in ritardo
  - Consegne effettuate
  - Scadenzario
  - Quantità gestionale
  - Quantità prezzo
  - Quantità vendita
  - Nazionale
  - Ordinamento
---
# Stampare lo scadenzario ordini clienti

## Prerequisiti
La stampa **Scadenzario ordini clienti** consente di ottenere una situazione delle consegne previste in relazione agli ordini inseriti e alle date di consegna indicate negli ordini stessi.

Prima di lanciare la stampa verificare che negli ordini siano presenti le date di consegna da analizzare.

## Procedura
1. Aprire la maschera di lancio della stampa **Scadenzario ordini clienti**.

2. Se necessario, indicare il **Cliente**. Il cliente può essere digitato direttamente oppure ricercato con il tasto destro del mouse, attivando la ricerca.

3. Se necessario, indicare il **Tipo ordine**. Anche il tipo ordine è ricercabile dalla maschera.

4. Se necessario, filtrare gli ordini per numero compilando i campi **Da numero ordine** e **A numero ordine**.

5. Se necessario, filtrare gli ordini per data compilando i campi **Da data** e **A data**.

6. Se necessario, indicare l'intervallo degli articoli compilando i campi **Da articolo** e **A articolo**.

7. Se necessario, indicare l'intervallo degli agenti compilando i campi **Da agente** e **A agente**.

8. Se il cliente gestisce le commesse, indicare il **Numero commessa** per limitare l'elaborazione agli ordini collegati alla commessa selezionata.

9. Nella sezione relativa alle consegne scegliere il tipo di situazione da estrarre:
   - **Consegne previste**, per visualizzare le consegne previste dagli ordini;
   - **Consegne in ritardo**, per visualizzare gli ordini in ritardo;
   - **Consegne effettuate**, per visualizzare le consegne già effettuate in un intervallo di date selezionato.

10. Se si seleziona **Consegne effettuate**, compilare il range **Da data** e **A data** relativo al periodo da verificare.

11. Nella multiscelta **Scadenzario**, scegliere il tipo di stampa:
   - **Valore**, per ottenere lo scadenzario a valore;
   - **Quantità**, per ottenere lo scadenzario a quantità.

12. Se viene selezionata la stampa a **Quantità**, scegliere il tipo di quantità da esporre:
   - quantità gestionale;
   - quantità di prezzo;
   - quantità di vendita.

1. Se necessario, impostare il filtro **Nazione** per distinguere clienti Italia, clienti estero oppure tutti i clienti.

2. Impostare il parametro **Ordinamento** scegliendo uno dei criteri disponibili:
   - codice cliente;
   - ragione sociale;
   - numero ordine;
   - articolo;
   - data di consegna;
   - commessa;
   - nazionale.

15. Selezionare il formato di stampa:
   - PDF standard dello scadenzario;
   - estrazione Excel.

16. Lanciare la stampa.

## Verifiche finali
Controllare che la stampa riporti gli ordini e le consegne coerenti con i filtri selezionati.

Se è stata richiesta la sezione **Consegne effettuate**, verificare che siano esposti gli estremi dei documenti di trasporto, le quantità spedite per ogni consegna e le eventuali fatture collegate.

Alla fine della stampa verificare il prospetto riepilogativo dei totali in euro dell'ordinato, del residuo e del consegnato.
