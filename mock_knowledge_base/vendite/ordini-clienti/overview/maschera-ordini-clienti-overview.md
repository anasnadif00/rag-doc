---
title: Maschera Ordini clienti
doc_kind: overview
domain: vendite
feature: ordini-clienti
keywords:
  - ordini clienti
  - maschera ordini clienti
  - filtri ordini
  - testata ordine
  - righe ordine
task_tags:
  - consultazione ordini clienti
  - inserimento ordine cliente
  - navigazione maschera ordini
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
aliases:
  - testata ordini clienti
  - gestione ordini clienti
field_labels:
  - Tipo
  - Numero
  - Data ordine
  - Cliente
  - Divisa
  - Stato
---
# Maschera Ordini clienti

La maschera **Ordini clienti** è strutturata come le altre maschere di Magia ed è suddivisa in tre aree principali.

## Struttura della schermata

### Area sinistra
L'area sinistra contiene i filtri per la ricerca degli ordini già esistenti.

I filtri possono essere utilizzati anche in modo combinato e consentono di selezionare gli ordini in base a:
- dati del cliente
- tipologia dell'ordine
- numerazione
- indirizzi
- riferimenti
- CIG
- CUP
- altri dati normalmente inseriti nell'ordine

L'esecuzione del filtro avviene tramite i simboli di imbuto presenti nella parte centrale della schermata.

### Area superiore
L'area superiore contiene i dati di **testata** dell'ordine.

### Area inferiore
L'area inferiore contiene il **dettaglio dell'ordine**, cioè le righe degli articoli inseriti.

## Regole

### Struttura generale
La sezione di testata è organizzata in più tab, ciascuna dedicata a uno specifico gruppo di informazioni.

### Ripresa dati da offerta
Se l'ordine è stato generato a partire da un'offerta confermata, i dati presenti nella testata e nei vari tab vengono ripresi dall'offerta e possono comunque essere modificati o integrati dall'utente.

### Propagazione dati ai documenti successivi
Le informazioni inserite nell'ordine possono essere riprese nei documenti successivi, come DDT, fatture e contabilità generale, in base al tipo di dato gestito.