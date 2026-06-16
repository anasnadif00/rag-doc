---
title: Scarica DDT
doc_kind: how_to
domain: vendite
feature: ddt
keywords:
  - Scarico DDT
  - scaricare DDT
  - movimentazione di magazzino
  - riscarica
  - scaricabile
  - Tipo documento scarico DDT
task_tags:
  - scarico automatico DDT
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
  - Tipo
  - Bolla
  - Anno
  - Numero
  - Data
  - Cliente
  - Descrizione del cliente
  - Già scaricato
  - Già stampato
  - Scaricabile
  - Riscarica
  - Data di registrazione
---
# Scarica DDT

## Prerequisiti
Usare l'elaborazione **Scarico DDT** per effettuare la movimentazione di magazzino dei DDT selezionati in base ai criteri di filtro impostati.

Rispetto allo **Scarico DDT da gestione di magazzino**, questa funzionalità consente l'esecuzione dello scarico in modo completamente automatico, senza particolari interventi da parte dell'operatore.

## Procedura
1. Apri il menu delle elaborazioni del modulo DDT.
2. Seleziona l'elaborazione **Scarico DDT**.
3. Nella parte sinistra della videata, imposta i filtri per individuare i DDT da scaricare.
4. Filtra i DDT usando uno o più dei seguenti criteri: Magazzino, Tipo, Bolla, Anno, Numero, Data, Cliente, Descrizione del cliente, Già scaricato, Già stampato, Scaricabile.
5. Applica il filtro per visualizzare i DDT che rispettano le condizioni impostate.
6. Seleziona i DDT da scaricare.
7. Indica la Data di registrazione da assegnare al movimento di magazzino.
8. Valuta il parametro **Scaricabile** in base ai documenti da estrarre.
9. Valuta il flag **Riscarica** se devono essere rigenerate movimentazioni di DDT già scaricati.
10. Lancia l'elaborazione con il martelletto.
11. Verifica il log dell'elaborazione.

## Verifiche finali
Verificare che i movimenti di magazzino siano stati generati.

I movimenti generati possono essere visualizzati e modificati dalla navigazione del DDT direttamente nella gestione di magazzino.