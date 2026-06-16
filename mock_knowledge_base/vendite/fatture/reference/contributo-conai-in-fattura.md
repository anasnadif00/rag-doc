---
title: Contributo Conai in fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - conai fattura
  - contributo conai
  - materiale conai
  - esenzione articolo conai
  - esenzione cliente conai
task_tags:
  - riferimento contributo conai
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
field_labels:
  - Tipo nota Conai
  - Tonnellate per unità di misura
---
# Contributo Conai in fattura

## Regole

### Materiale di appartenenza
Nella tabella Conai, materiale di appartenenza, devono essere codificati i materiali utilizzati dall'azienda.

Esempi:
- carta
- plastica
- altre tipologie di materiale

### Materiale contributo
Nella tabella Conai materiale contributo deve essere definito, per ogni materiale:
- codice articolo da utilizzare per la riga di contributo in fattura
- importo del contributo

### Esenzione articolo
Nella sezione esenzione articolo della tabella Conai è possibile indicare articoli da escludere dal calcolo del contributo.

### Esenzione cliente
Nella sezione esenzione cliente della tabella Conai è possibile definire la percentuale di esenzione per ogni cliente e materiale.

### Generazione automatica riga Conai
Se per l'articolo inserito sono presenti i dati Conai nel TP Dati Gestionali dell'anagrafica articolo, viene proposta automaticamente una riga in fattura.

La riga usa come codice articolo quello impostato nella tabella Conai materiale contributo per il materiale collegato all'articolo fatturato.

### Calcolo quantità contributo
La quantità del contributo viene determinata considerando:
- peso unitario del materiale
- quantità articolo
- percentuale di esenzione
- campo tonnellate per unità di misura presente nel TP Dati Gestionali dell'articolo
- percentuale di esenzione presente nella tabella Conai esenzione cliente

### Calcolo prezzo contributo
Il prezzo del contributo corrisponde all'importo del contributo presente nella tabella Conai materiale contributo.

### Nota per percentuale di esenzione
Se è presente una percentuale di esenzione, questa viene riportata nella nota con il tipo nota impostato nel campo tipo nota Conai della tabella Parametri del Commerciale.