---
title: Compila la testata di un'offerta
doc_kind: how_to
domain: commerciale
feature: offerte
keywords:
  - compila offerta
  - testata offerta
  - tipo documento offerta
  - cliente offerta
  - data offerta
  - riferimenti offerta
task_tags:
  - caricamento offerta
  - compilazione testata offerta
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Offerte
screen_title: Offerte
tab_name: TP Testata
field_labels:
  - Tipo documento
  - Numero
  - Data ordine
  - Data inserimento
  - Cliente
  - Nostro riferimento
  - Vostro riferimento
  - All'attenzione
  - Stato
  - Data scadenza
  - Avanzamento
  - Data avanzamento
  - Motivo avanzamento
  - Chiusura
---
# Compila la testata di un'offerta

## Prerequisiti
Verifica che siano disponibili il tipo documento da utilizzare e, se necessario, l'anagrafica del cliente.

## Procedura
1. Apri il modulo Offerte e posizionati nella testata del documento.
2. Inserisci il campo **Tipo**. Il tipo documento può essere richiamato anche con l'help attivabile con il tasto destro del mouse sul relativo campo.
3. Verifica il **Numero** proposto dal sistema. La numerazione è progressiva ed è assegnata automaticamente dal programma in base alle impostazioni del tipo documento scelto.
4. Inserisci la **Data ordine**. Il sistema propone normalmente la data giornaliera di sistema, ma il valore può essere modificato dall'utente.
5. Verifica la **Data inserimento**. Questa data resta quella di sistema e non può essere modificata dall'utente.
6. Inserisci il **Cliente** intestatario dell'offerta. Puoi:
   7. selezionare un cliente esistente digitando una parte del nome per ottenere la proposta automatica delle anagrafiche corrispondenti;
   9. selezionare il cliente con il codice esistente se già noto;
   10. help sul campo **Conto** con il tasto dx del mouse e ricerca dell'anagrafica con % per cercare parte di una stringa;
   11. digitare manualmente i dati di intestazione e indirizzo se l'offerta deve essere intestata senza richiamare un'anagrafica esistente.
12. Compila gli eventuali riferimenti liberi della testata, come **Nostro riferimento**, **Vostro riferimento** e **All'attenzione**.
13. Verifica lo **Stato** iniziale dell'offerta. Normalmente l'offerta parte da stato **Inserito**.
14. Imposta la **Data scadenza** dell'offerta, scegliendo una delle due modalità:
   15. inserire i giorni di validità per calcolare la data a partire dalla data ordine;
   16. modificare direttamente il campo data disponibile.
17. Se richiesto, imposta l'**Avanzamento**, la relativa **Data avanzamento**, il **Motivo avanzamento** e il valore di **Chiusura** che indica la probabilità di chiusura dell'offerta.
18. Completa i tab successivi della testata in base alle esigenze operative: **TP Condizioni**, **TP Dati di spedizione**, **TP Dati di analitica**, **TP Agenti**, **TP Pagamenti**, **TP Sconti**, **TP Trasporti**, **TP Spese**, **TP IVA**, **TP Pesi**, **TP Attributi**, **TP Note di testata**, **TP Allegati** e **TP Email inviate**.
19. Dopo aver completato la testata, procedi con il caricamento del dettaglio degli articoli nell'area inferiore della schermata.

## Verifiche finali
Controlla che:
1. il tipo documento sia corretto;
2. il numero sia stato assegnato automaticamente;
3. il cliente o l'intestazione manuale siano corretti;
4. stato, avanzamento e scadenza siano coerenti con la situazione commerciale;
5. i tab della testata siano stati completati secondo le informazioni richieste dall'offerta.