---
title: Imposta data di trasporto
doc_kind: how_to
domain: vendite
feature: ddt
keywords:
  - Imposta data di trasporto
  - DDT
  - data inizio trasporto
  - ora inizio trasporto
  - aggiornamento massivo DDT
task_tags:
  - impostazione data trasporto DDT
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - amministrazione vendite
review_status: approved
module: DDT
submenu: Elaborazioni
aliases:
  - documento di trasporto
  - bolle
field_labels:
  - Magazzino
  - Tipo bolla
  - Anno bolla
  - Numero bolla
  - Data
  - Cliente
  - Descrizione
  - Data di inizio trasporto
  - Ora di inizio trasporto
  - Minuti
  - Elabora tutto
  - Ignora DDT con data maggiore di un mese
---
# Imposta data di trasporto

## Prerequisiti
Usare l'elaborazione **Imposta data di trasporto** per impostare massivamente la data di inizio trasporto sui DDT che:
- non hanno già la data di inizio trasporto valorizzata in testata;
- rientrano nei filtri impostati nella videata.

## Procedura
1. Apri la maschera principale del DDT.
2. Apri il menu delle elaborazioni dai tasti in alto a destra.
3. Seleziona l'elaborazione **Imposta data di trasporto**.
4. Nella parte sinistra della videata, imposta i filtri per individuare i DDT da aggiornare.
5. Filtra i documenti usando uno o più dei seguenti criteri: Magazzino, Tipo bolla, Anno bolla, Numero bolla, Data, Cliente, Descrizione.
6. Applica il filtro per visualizzare nella parte destra i DDT che rispettano i criteri impostati.
7. Seleziona i DDT da aggiornare, se l'elaborazione deve essere limitata ai documenti visualizzati e selezionati.
8. Nella sezione **Parametri di inserimento**, indica la Data di inizio trasporto.
9. Indica l'Ora di inizio trasporto, se deve essere valorizzata.
10. Indica i Minuti nell'apposito campo separato, se devono essere valorizzati.
11. Imposta il parametro **Elabora tutto** in base al comportamento desiderato, ovvero se si vogliono considerare tutte le bolle anche quelle che non compaiono nella visualizzazione per motivi di spazio.
12. Imposta il parametro **Ignora DDT con data maggiore di un mese** in base ai documenti da includere nell'elaborazione.
13. Conferma l'elaborazione.

## Verifiche finali
Controllare che sui DDT elaborati siano stati valorizzati la data di inizio trasporto e, se indicati, anche ora e minuti di inizio trasporto.