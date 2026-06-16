---
title: Campi e regole del Tipo documento di trasporto
doc_kind: reference
domain: logistica
feature: ddt
keywords:
  - tipo documento di trasporto
  - tipo ddt
  - competenza iva ddt
  - ddt da ordine
  - scarico alla stampa
  - conto visione
task_tags:
  - riferimento tipo documento ddt
erp_versions:
  - v.1.0
role_scope:
  - logistica
  - amministrazione
review_status: approved
module: DDT
field_labels:
  - Tipo DDT
  - Descrizione
  - Tipo numerazione
  - Competenza IVA
---
# Campi e regole del Tipo documento di trasporto

## Campi

### Tipo DDT
Codice che identifica univocamente la tipologia del documento di trasporto.

### Descrizione
Descrizione libera associata alla tipologia di documento.

### Tipo numerazione
Definisce la tipologia di numerazione da utilizzare per il documento.

Se il campo non viene valorizzato, la numerazione è manuale e durante l'inserimento del DDT non viene proposto alcun numero automatico.

### Competenza IVA
Definisce come determinare la competenza IVA del documento.

Le opzioni disponibili consentono di desumere la competenza IVA in alternativa da:

- data di trasporto
- data della fattura

## Regole

### Numerazione manuale
La numerazione manuale non consente controlli automatici sulla progressione dei numeri.

Eventuali buchi di numerazione o cancellazioni potrebbero non essere rilevati dal sistema.

### Numerazione automatica
Si consiglia l'utilizzo di una tipologia di numerazione automatica e progressiva.

La progressione viene mantenuta per tutti i DDT che condividono lo stesso tipo di numerazione.

### Numerazioni condivise o separate
È possibile:

- utilizzare numerazioni differenti per differenti tipologie di DDT
- utilizzare la stessa numerazione per più tipologie di DDT

### Modifica del numero proposto
Anche in presenza di numerazione automatica, il numero proposto può essere modificato manualmente dall'utente.

## Campi

### Flag DDT da ordine
Se attivato, consente la generazione di DDT a partire dagli ordini clienti.

Se non attivato, non è possibile emettere DDT riprendendo ordini.

### Flag Gestione valori
Se attivato e se risulta impostato il parametro "Bolle gestione valori" nella tabella "Parametri del commerciale", consente la gestione di valori e sconti sul DDT.

### Flag Articolo senza prezzo
Se attivato, consente l'inserimento di articoli senza indicazione del prezzo.

Se non attivato, il prezzo è obbligatorio per ogni articolo inserito.

### Flag Scarico alla stampa
Se attivato, la stampa definitiva del DDT genera automaticamente anche il movimento di scarico di magazzino.

### Flag Bolla stampata modificabile
Se attivato, consente la modifica di un DDT già stampato in definitiva in stato di stampato.

### Flag Modificabile
Se attivato, consente la modifica di una bolla già scaricata con relativo movimento di magazzino in stato di scaricato.

### Flag Bolla valorizzata modificabile
Se attivato, consente la modifica di un DDT già fatturato in stato di valorizzato.

Si consiglia di non attivare questo flag per evitare modifiche a documenti già fatturati.

### Flag Conto/Visione
Se attivato, identifica il documento come DDT di Conto/Visione anziché come documento di vendita.