---
title: TP Articolo della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - tp articolo fattura
  - numero riga fattura
  - tipo riga fattura
  - codice articolo
  - descrizione articolo
task_tags:
  - riferimento tp articolo fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Articolo
field_labels:
  - Numero riga
  - Tipo riga
  - Articolo
  - Descrizione
  - Quantità
  - Prezzo
  - Sconti
---
# TP Articolo della riga fattura

## Campi

### Numero riga
Definisce il progressivo della riga articolo esposta nella fattura.

In Magia la numerazione viene normalmente proposta partendo da 10 e prosegue con multipli di 10.

### Tipo riga
Identifica la tipologia della riga.

Il valore viene proposto progressivamente ma può essere modificato.

### Articolo
Identifica il codice articolo presente in magazzino.

Il codice articolo può essere:
- inserito manualmente
- acquisito tramite barcode nelle versioni abilitate
- proposto automaticamente in base al codice inserito nel campo articolo cliente

### Descrizione
La descrizione viene proposta automaticamente per gli articoli codificati, se nei Parametri del Commerciale è attiva l'opzione relativa.

### Quantità
Indica la quantità della riga.

### Prezzo
Indica il prezzo unitario applicato alla riga.

### Sconti
Il campo sconti viene compilato in base agli sconti presenti nel TP Sconti.

## Regole

### Descrizione articoli codificati
Per gli articoli codificati la descrizione proposta automaticamente non può essere modificata.

### Descrizione modificabile
La descrizione può essere modificata per:
- articoli non codificati
- note
- spese

### Articoli non codificati
Gli articoli non codificati possono essere richiamati tramite il loro codice e utilizzati con una descrizione libera.