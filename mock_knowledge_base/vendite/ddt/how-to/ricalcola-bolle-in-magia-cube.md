---
title: Ricalcola bolle in Magia Cube
doc_kind: how_to
domain: vendite
feature: ddt
keywords:
  - Ricalcolo bolle in Magia Cube
  - ricalcolo DDT
  - ricalcolo bolle
  - importi DDT
  - documenti di trasporto
task_tags:
  - ricalcolo DDT
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
  - Tipo documento
  - Anno bolla
  - Numero
  - Codice conto
  - Descrizione cliente
  - Esito
---
# Ricalcola bolle in Magia Cube

## Prerequisiti
Usare questa elaborazione quando gli importi dei documenti di trasporto devono essere ricalcolati.

La procedura è utile quando:
- gli importi sono stati calcolati o modificati da applicazioni esterne in modo non corretto;
- sono state modificate impostazioni che possono avere impattato sui valori del documento di trasporto;
- è necessario rieseguire il calcolo dei DDT selezionati.

## Procedura
1. Apri la maschera principale del DDT.
2. Seleziona i tasti in alto a destra della maschera principale.
3. Apri il menu delle elaborazioni.
4. Seleziona l'elaborazione **Ricalcolo bolle in Magia Cube**.
5. Nella videata di selezione, imposta i filtri dei DDT da rielaborare.
6. Filtra i DDT per uno o più dei seguenti criteri: Tipo documento, Anno bolla, Numero, Codice conto, Descrizione cliente, Esito.
7. Clicca sull'icona dell'imbuto per applicare il filtro.
8. Verifica nella parte destra della videata l'elenco dei DDT che rispettano le condizioni impostate.
9. Seleziona i DDT da ricalcolare.
10. Conferma l'elaborazione lanciando il martelletto.

## Verifiche finali
Al termine dell'elaborazione, verificare che i DDT selezionati siano stati ricalcolati e che gli importi risultino coerenti con le impostazioni correnti.