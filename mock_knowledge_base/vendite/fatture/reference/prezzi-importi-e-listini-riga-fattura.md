---
title: Prezzi importi e listini della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - prezzo fattura
  - listino fattura
  - prezzo vendita articolo
  - importo lordo
  - importo netto
  - solo fatturazione
task_tags:
  - riferimento prezzi riga fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Articolo
field_labels:
  - Prezzo
  - Importo lordo
  - Importo netto
  - Sconti
---
# Prezzi importi e listini della riga fattura

## Campi

### Prezzo
Indica il prezzo unitario della riga.

### Importo lordo
È calcolato automaticamente dal programma moltiplicando quantità per prezzo.

### Importo netto
È calcolato come quantità per prezzo al netto degli eventuali sconti.

## Regole

### Obbligatorietà del prezzo
Il prezzo è obbligatorio se l'articolo ha attiva nell'anagrafica, nel TP Dati Gestionali, l'opzione "Solo fatturazione".

### Proposta automatica del prezzo
Il prezzo può essere proposto automaticamente:
- in base al listino
- in base al prezzo di vendita presente nell'anagrafica articolo, se non viene trovato un prezzo da listino

### Priorità di ricerca prezzi
Il listino da applicare viene determinato in base alle priorità stabilite nella tabella di ricerca prezzi.

### Inserimento manuale del prezzo
Il prezzo può essere inserito manualmente dall'utente se non sono presenti automatismi che ne determinano la proposta automatica.

### Effetto degli sconti
Gli sconti presenti nella riga riducono l'importo lordo e determinano l'importo netto.
