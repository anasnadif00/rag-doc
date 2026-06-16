---
title: Quantità unità di misura e colli della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - quantità fattura
  - quantità vendita
  - quantità prezzo
  - quantità gestionale
  - unità misura
  - colli fattura
task_tags:
  - riferimento quantità riga fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Articolo
field_labels:
  - Quantità
  - Quantità vendita
  - Quantità prezzo
  - Quantità gestionale
  - Colli
---
# Quantità unità di misura e colli della riga fattura

## Campi

### Quantità gestionale
È la quantità espressa nell'unità di misura gestionale principale dell'articolo.

È l'unica quantità obbligatoria.

Viene utilizzata per la movimentazione di magazzino.

### Quantità vendita
È la quantità espressa nell'unità di misura di vendita dell'articolo.

L'unità di misura viene proposta in base al campo unità di misura vendita dell'anagrafica articolo.

### Quantità prezzo
È la quantità espressa nell'unità di misura a cui è riferito il prezzo.

L'unità di misura prezzo è anche quella utilizzata dal listino.

### Colli
Il campo colli consente di indicare il numero di colli della riga.

## Regole

### Proposta delle unità di misura
Le unità di misura vendita e prezzo vengono proposte in base a quanto definito nell'anagrafica articolo.

Se non sono specificate, vengono proposte uguali all'unità di misura gestionale.

### Unità di misura alternative
Le unità di misura possono essere modificate scegliendo tra le unità di misura alternative definite nell'anagrafica articolo, nei dati gestionali, tabella unità alternative.

### Compilazione automatica da ordine o DDT
Se la riga viene ripresa da ordine o da DDT, le quantità risultano già compilate automaticamente.

### Calcolo da quantità vendita o prezzo
Indicando la quantità vendita o la quantità prezzo, viene calcolata automaticamente la quantità gestionale.

### Calcolo da quantità gestionale
Indicando la quantità gestionale, viene aggiornata la quantità prezzo se sono presenti unità di misura diverse.

### Fattori di conversione
Le quantità vengono calcolate automaticamente in base ai fattori di conversione presenti nell'anagrafica articolo.

### Quantità sincronizzate
Se nei dati gestionali dell'articolo è attiva l'opzione "Quantità sincronizzate", al variare di una quantità vengono aggiornate automaticamente anche le altre.

### Calcolo quantità da colli
All'inserimento o alla modifica dei colli viene calcolata e proposta la quantità gestionale quando:
- la quantità gestionale non è già presente
- nei dati tecnici dell'articolo sono impostati i prezzi colli
- nei dati tecnici dell'articolo sono impostati i colli barra prezzi

### Colli su righe omaggio
I colli vengono calcolati anche sulle quantità omaggio.