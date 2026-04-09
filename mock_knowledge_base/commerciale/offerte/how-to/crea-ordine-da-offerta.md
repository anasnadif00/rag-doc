---
title: Creare un ordine da un'offerta
doc_kind: how_to
domain: commerciale
feature: offerte
keywords:
  - crea ordine
  - ordine da offerta
  - evasione completa
  - evasione parziale
  - offerta evasa
  - vinta totale
  - vinta parziale
task_tags:
  - creazione ordine
  - evasione offerta
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Offerte
submenu: Navigazione offerta
screen_title: Crea Ordine
aliases:
  - crea ordine da navigazione
  - evasione offerta
field_labels:
  - Tipo ordine
  - Data
  - Data di consegna
  - Cliente
  - Evasione completa
  - Stato
  - Avanzamento
---
# Creare un ordine da un'offerta

## Prerequisiti
Verificare che l'offerta sia stata inserita e che il cliente abbia confermato la proposta.

## Procedura
1. Aprire l'offerta confermata.
2. Dal menu di navigazione, selezionare la procedura **Crea Ordine**.
3. Verificare che nella maschera vengano riportate automaticamente tutte le righe contenute nell'offerta.
4. Nella parte sottostante della maschera, compilare i parametri necessari alla creazione dell'ordine.
5. Inserire il **Tipo ordine**.
6. Inserire la **Data** dell'ordine.
7. Inserire la **Data di consegna**. Questo dato è obbligatorio.
8. Compilare il campo **Cliente** solo se si vuole intestare l'ordine a un cliente diverso.
9. Lasciare attivo il flag **Evasione completa** se si vuole evadere tutta l'offerta in un unico ordine.
10. Se non si vuole evadere tutta l'offerta, disattivare il flag **Evasione completa** e selezionare solo le righe da evadere.

## Verifiche finali
1. Verificare che l'ordine sia stato creato.
2. Verificare che, alla creazione dell'ordine, il programma aggiorni automaticamente lo **Stato** dell'offerta in **Evaso**.
3. Verificare che l'**Avanzamento** venga impostato in **Vinta Totale** oppure **Vinta Parziale** in base al tipo di evasione eseguita.