---
title: Riga omaggio in fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - riga omaggio fattura
  - omaggio iva
  - articolo omaggio
  - totale fattura
task_tags:
  - riferimento riga omaggio
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Articolo
field_labels:
  - Tipo riga
  - Omaggio IVA
---
# Riga omaggio in fattura

## Regole

### Elaborazione della riga omaggio
La riga di tipo omaggio consente di processare l'articolo come le altre righe.

### Effetto sul totale documento
In fase di fatturazione il valore della riga omaggio non viene sommato nel totale documento.

### Applicazione IVA
L'IVA viene applicata in base alla configurazione dell'articolo in anagrafica.

Se nei dati gestionali dell'articolo è attivo il flag "Omaggio IVA", la riga segue tale configurazione.