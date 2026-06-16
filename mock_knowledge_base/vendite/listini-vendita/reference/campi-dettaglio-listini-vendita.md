---
title: Campi del dettaglio Listini vendita
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - dettaglio listino vendita
  - articolo listino
  - marca listino
  - unità misura listino
  - provvigione diretta
  - provvigione indiretta
task_tags:
  - riferimento campi dettaglio listini vendita
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
screen_title: Listini vendita
tab_name: Dettaglio
field_labels:
  - Articolo
  - Marca
  - Unità di misura
  - Provvigione diretta
  - Provvigione indiretta
---
# Campi del dettaglio Listini vendita

## Campi

### Articolo
Indica l'articolo al quale si riferiscono le condizioni inserite nel listino.

È il primo campo disponibile nella sezione di dettaglio.

### Marca
Indica la marca associata all'articolo.

La marca è subordinata all'articolo.

Lo stesso codice articolo può essere associato a marche diverse e avere quindi:
- prezzi differenti;
- sconti differenti;
- provvigioni differenti.

Il campo Marca non è obbligatorio.

Se viene indicata la marca, il prezzo viene proposto in ordine, DDT e fattura solo se viene trovata la stessa marca.

### Unità di misura
Indica l'unità di misura in cui è espressa la quantità dell'articolo.

Può essere scelta tra:
- unità di misura principale;
- unità di misura alternative indicate in anagrafica articolo.

Se in anagrafica articolo è indicata l'unità di misura del prezzo, questa viene proposta automaticamente.

### Provvigione diretta
Indica il valore della provvigione diretta da associare all'articolo per il listino corrente.

### Provvigione indiretta
Indica il valore della provvigione indiretta da associare all'articolo per il listino corrente.

## Regole

### Condizioni diverse per articolo e marca
Quando per lo stesso articolo sono presenti più marche, il listino può contenere condizioni diverse per ciascuna marca.

In fase di proposta prezzo nei documenti, la marca deve coincidere con quella presente nella riga di listino per applicare le condizioni specifiche.