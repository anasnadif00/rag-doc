---
title: Stampare la disponibilità prodotto
doc_kind: how_to
domain: vendite
feature: ordini-clienti
keywords:
  - disponibilità prodotto
  - stampa disponibilità prodotto
  - ordini clienti
  - disponibilità articoli
  - giacenza magazzino
  - ordini fornitori
  - ordini produzione
task_tags:
  - stampa disponibilità prodotto
  - verifica disponibilità articoli
  - controllo disponibilità ordini
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - magazzino
review_status: approved
module: Ordini
screen_title: Disponibilità prodotto
aliases:
  - disponibilità articoli
field_labels:
  - Tipo ordine
  - Numero ordine
  - Anno ordine
  - Periodo
  - Da data
  - A data
  - Solo articoli non disponibili
  - Ordini pianificati
  - Ordini clienti non confermati
  - Ordini bloccati
  - Articoli senza valori significativi
---
# Stampare la disponibilità prodotto

## Prerequisiti
La disponibilità prodotto può essere richiesta per gli articoli presenti in uno specifico ordine cliente oppure per tutti i prodotti gestiti a magazzino.

Prima di lanciare l'elaborazione verificare quali magazzini devono essere considerati, perché la disponibilità viene calcolata sulla giacenza dei magazzini selezionati.

## Procedura
1. Aprire l'elaborazione **Disponibilità prodotto** dal modulo **Ordini**.

2. Inserire il **Tipo ordine**, il **Numero ordine** e l'**Anno ordine** se la disponibilità deve essere calcolata in relazione agli articoli presenti in uno specifico ordine cliente.

3. Scegliere il formato di stampa:
   - **sintetica**, per visualizzare la disponibilità aggregata per periodo;
   - **analitica**, per visualizzare anche gli estremi degli ordini che contribuiscono alla disponibilità.

4. Se si seleziona la stampa **sintetica**, indicare il **Periodo** scegliendo tra:
   - giorni;
   - settimane;
   - mesi.

5. Verificare il campo **Da data**. Il sistema propone automaticamente la data di sistema, cioè la data in cui viene lanciata l'elaborazione, ma l'utente può modificarla.

6. Verificare il campo **A data**. Il valore viene determinato automaticamente dal sistema e non è modificabile. La data finale viene calcolata aggiungendo alla **Da data**:
   - 9 giorni, se il periodo scelto è espresso in giorni;
   - 9 settimane, se il periodo scelto è espresso in settimane;
   - 9 mesi, se il periodo scelto è espresso in mesi.

7. Se necessario, attivare il flag **Solo articoli non disponibili** per esporre in stampa soltanto gli articoli che non risultano disponibili.

8. Se necessario, attivare il flag per includere gli **ordini pianificati** nel calcolo della disponibilità.

9. Se necessario, attivare il flag per includere anche gli **ordini clienti non confermati** nel calcolo della disponibilità.

10. Se necessario, attivare il flag per includere anche gli **ordini bloccati**.

11. Se necessario, attivare il flag per includere anche gli **articoli senza valori significativi**.

12. Lanciare la stampa nel formato desiderato:
    - PDF standard della disponibilità prodotto;
    - estrazione Excel della stessa stampa.

## Verifiche finali
Controllare che la stampa riporti gli articoli attesi e che il periodo esposto sia coerente con la **Da data** e con il tipo di periodo selezionato.

Nel caso della stampa analitica, verificare che siano presenti anche gli estremi degli ordini clienti, degli ordini fornitori, degli ordini di produzione e degli ordini pianificati che hanno contribuito alla formazione della disponibilità.