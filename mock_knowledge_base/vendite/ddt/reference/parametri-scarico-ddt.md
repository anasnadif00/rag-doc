---
title: Parametri di Scarico DDT
doc_kind: reference
domain: vendite
feature: ddt
keywords:
  - parametri Scarico DDT
  - scaricabile
  - riscarica
  - data registrazione
  - Tipo documento scarico DDT
  - DDT già scaricato
task_tags:
  - riferimento parametri scarico DDT
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
  - Scaricabile
  - Riscarica
  - Data di registrazione
---
# Parametri di Scarico DDT

## Campi

### Scaricabile
Determina quali DDT vengono estratti per lo scarico.

Se **Scaricabile** è impostato a **Sì**, vengono estratti solo i DDT che hanno i parametri impostati nella tabella **Tipo documento scarico DDT**.

Se **Scaricabile** è impostato a **Tutti**, vengono estratti tutti i documenti che rispettano i filtri impostati.

In mancanza dei parametri necessari, lo scarico non viene effettuato e viene restituita una segnalazione di errore.

### Riscarica
Consente di rifare le registrazioni di movimentazione dei DDT che si trovano già nello stato **Scaricato**.

Il flag può essere usato quando è necessario rilanciare lo scarico, ad esempio dopo la cancellazione di un movimento generato in modo errato o modificato successivamente.

### Data di registrazione
Definisce la data da assegnare al movimento di magazzino generato dallo scarico.

La data del movimento viene solitamente proposta in relazione alle impostazioni della tabella **Tipo documento scarico DDT**, ma può essere modificata dall'operatore.

## Regole

### Controllo dei parametri di scarico
Per eseguire lo scarico automatico, il DDT deve avere i parametri necessari definiti nella tabella **Tipo documento scarico DDT**.

### Documenti non movimentabili
Se un documento non prevede la movimentazione di magazzino, lo scarico non viene effettuato.

Un esempio è il DDT di movimentazione interna, per il quale possono mancare i parametri necessari allo scarico.

### Segnalazione di errore
Quando un DDT viene estratto ma non dispone dei parametri richiesti per lo scarico, la procedura restituisce una segnalazione di errore e il documento non viene scaricato.