---
title: Campi della testata DDT documenti di trasporto
doc_kind: reference
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - testata DDT
  - campi DDT
  - tipo DDT
  - numero DDT
  - data DDT
  - magazzino DDT
  - causale DDT
  - cliente DDT
task_tags:
  - riferimento campi testata DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - magazzino
  - amministrazione vendite
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Testata
aliases:
  - bolla
  - documento di trasporto
field_labels:
  - Operatore
  - Data di inserimento
  - Tipo
  - Numero
  - Data DDT
  - Magazzino
  - Causale
  - Cliente
  - Divisa
  - Nostro riferimento
  - Vostro riferimento
  - Stampato
  - Valorizzato
  - Scaricato
---
# Campi della testata DDT documenti di trasporto

## Campi

### Operatore
Identifica l'utente con cui si è entrati in Magia e con cui viene caricato il documento di trasporto.

### Data di inserimento
La data di inserimento viene normalmente proposta in automatico con la data di sistema.

La data di inserimento non è modificabile.

### Tipo
Indica la tipologia del documento di trasporto.

Il tipo DDT viene definito nella relativa tabella dei tipi documento.

Con il tasto destro del mouse è possibile attivare l'help per visualizzare i tipi documento disponibili.

Con F5 è possibile entrare in navigazione nella tabella dei tipi documento, ad esempio per verificare le impostazioni del tipo documento o inserirne uno nuovo.

### Numero
Il numero del DDT viene normalmente proposto automaticamente.

È possibile inserirlo manualmente, ma l'inserimento manuale è sconsigliato per evitare buchi nella numerazione dei DDT.

### Data DDT
La data del DDT viene normalmente proposta uguale alla data di sistema.

La data DDT può essere modificata dall'utente.

### Magazzino
Indica il magazzino dal quale viene prelevato il materiale da spedire.

Il magazzino deve essere impostato obbligatoriamente.

Con il tasto destro del mouse è possibile attivare l'help dei magazzini.

Con F5 è possibile entrare in navigazione nella relativa tabella.

### Causale
Indica la causale di magazzino con cui verranno generate le movimentazioni di magazzino relative al materiale spedito.

Possono essere scelte solo causali di magazzino che nella tabella delle causali di magazzino risultano impostate come:

- tipo causale di scarico;
- valide per commerciale.

Con il tasto destro del mouse è possibile attivare l'help delle causali.

Con F5 è possibile entrare in navigazione nella relativa tabella.

### Cliente
Identifica il cliente al quale viene intestato il DDT.

Se il DDT viene generato da un ordine, il cliente viene ripreso dall'ordine.

### Divisa
La divisa può essere impostata nel DDT.

Normalmente viene proposta in automatico in base a quanto impostato nell'anagrafica del cliente.

### Nostro riferimento
Campo libero compilabile manualmente.

Se il DDT viene generato da ordini in cui il dato è presente, il valore viene ripreso dagli ordini.

### Vostro riferimento
Campo libero compilabile manualmente.

Se il DDT viene generato da ordini in cui il dato è presente, il valore viene ripreso dagli ordini.

### Stampato
Indica che il DDT è stato stampato con stampa definitiva.

La stampa provvisoria non attribuisce lo stato di stampato.

### Valorizzato
Indica che dal DDT è stata generata una fattura.

Lo stato viene assunto automaticamente nel momento in cui viene generata la fattura dal DDT.

### Scaricato
Indica che per il DDT è stato effettuato lo scarico di magazzino.

Lo stato viene assunto nel momento in cui viene effettuato lo scarico di magazzino del DDT.

## Regole

### Numerazione del tipo DDT
A ogni tipologia DDT è abbinata una numerazione da adottare.

La numerazione è determinata dalle impostazioni del tipo DDT.

### Impostazioni del tipo DDT
Le impostazioni del tipo DDT regolano il comportamento del documento di trasporto.

Tra le impostazioni del tipo DDT rientrano:

- la possibilità di azione in funzione dello stato del DDT;
- la gestione dei DDT stampati;
- la gestione dei DDT valorizzati;
- la gestione dei DDT scaricati;
- la gestione dei DDT regolati da ordine;
- la gestione dei valori;
- la gestione degli articoli senza prezzo.

### Ripresa ordini dalla testata
Dopo avere impostato i campi Tipo, Magazzino e Causale, se il tipo DDT prevede il flag DDT da ordine, è possibile eseguire la ripresa ordini tramite l'icona a forma di cartellina disponibile nella testata.