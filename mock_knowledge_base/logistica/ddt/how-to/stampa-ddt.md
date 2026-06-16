---
title: Stampa DDT
doc_kind: how_to
domain: logistica
feature: ddt
keywords:
  - stampa ddt
  - stampa definitiva ddt
  - stampa provvisoria ddt
  - invio ddt mail
  - scarico alla stampa
  - bolla stampata modificabile
task_tags:
  - stampa ddt
  - invio ddt
  - stampa definitiva
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - logistica
  - amministrazione vendite
review_status: approved
module: DDT
field_labels:
  - Tipo bolla
  - Magazzino
  - Anno
  - Data
  - Cliente
  - Stampato
  - Scaricato
---
# Stampa DDT

## Prerequisiti 
(N.B non so perchè ha inserito i requisiti, io li toglierei ma non so se è corretto farlo, vedere con Anas)
Verificare che:
- il DDT sia stato inserito correttamente
- il cliente sia presente in anagrafica
- il tipo documento di trasporto sia configurato correttamente
- siano presenti eventuali configurazioni mail nella tabella "Mail messaggi"

## Procedura
1. Accedere alle elaborazioni del modulo DDT.
2. Aprire la funzione "DDT".
3. Impostare i filtri desiderati:
   - tipo di bolla
   - magazzino
   - numero documento
   - anno
   - intervallo date
   - cliente
4. Selezionare il tipo di stampa:
   - provvisoria
   - definitiva
5. Avviare la stampa del DDT.
6. In alternativa utilizzare:
   per la stampa definitiva con generazione automatica del movimento di magazzino se impostato in Tabella Tipo documento di scarico
   -  l'icona della chiocciola  l'invio diretto tramite mail
   - la stampa cartacea tramite icona stampante

## Regole
### Stampa provvisoria
La stampa provvisoria produce un documento di prova senza attivare il flag di stampato.

### Stampa definitiva
La stampa definitiva:
- attiva automaticamente il flag "Stampato"
- può impedire successive modifiche al DDT

### Modifica DDT stampato
Il DDT stampato in definitiva può essere modificato solo se nel "Tipo documento di trasporto" è attivo il flag:
- "Bolla stampata modificabile"

### Scarico alla stampa
Se nel "Tipo documento di trasporto" è attivo il flag:
- "Scarico alla stampa"

all'esecuzione della stampa definitiva:
- viene generato automaticamente il movimento di scarico di magazzino
- il DDT viene aggiornato come scaricato

### Formati di stampa
Sono disponibili:
- formati standard
- formati personalizzati cliente con loghi e impostazioni dedicate

## Verifiche finali
Verificare che:
- il DDT risulti stampato
- il flag "Stampato" sia aggiornato
- l'eventuale movimento di magazzino sia stato generato
- il flag "Scaricato" sia valorizzato se previsto lo scarico