---
title: Tabella Articoli clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - Articoli clienti
  - codice articolo cliente
  - articolo di magazzino
  - cliente
  - marca
  - righe ordine
  - documenti emessi
task_tags:
  - configurazione articoli clienti
  - associazione articolo cliente
  - gestione codici articolo cliente
erp_versions:
  - v.1.0
role_scope:
  - operatore ordini clienti
  - commerciale
  - magazzino
review_status: approved
module: Ordini clienti
screen_title: Articoli clienti
aliases:
  - tabella Articoli clienti
field_labels:
  - Cliente
  - Conto cliente
  - Articolo di magazzino
  - Marca
  - Codice articolo cliente
---
# Tabella Articoli clienti

## Regole

### Corrispondenza tra articolo interno e articolo cliente
La tabella "Articoli clienti" consente di codificare la corrispondenza tra il codice articolo inserito nel magazzino interno e l'eventuale codice articolo del cliente.

Il codice articolo del cliente viene esposto nei documenti emessi, inclusi gli ordini clienti.

### Utilizzo nelle righe ordine
Una volta salvata la corrispondenza, quando viene richiamato lo stesso articolo di magazzino nelle righe di corpo dell'ordine, Magia riporta anche l'articolo del cliente.

## Campi

### Cliente
Identifica il cliente per il quale si vuole codificare la corrispondenza articolo.

### Conto cliente
Consente di richiamare il conto del cliente per il quale si vuole codificare l'articolo.

### Articolo di magazzino
Identifica l'articolo interno di magazzino da associare al codice articolo cliente.

### Marca
Campo opzionale per indicare la marca associata all'articolo.

### Codice articolo cliente
Indica il codice articolo utilizzato dal cliente e da esporre nei documenti emessi.