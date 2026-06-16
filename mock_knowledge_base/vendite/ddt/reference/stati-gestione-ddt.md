---
title: Stati di gestione DDT
doc_kind: reference
domain: vendite
feature: ddt
keywords:
  - DDT
  - stati DDT
  - stampato
  - scaricato
  - valorizzato
  - documento di trasporto
task_tags:
  - riferimento stati DDT
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - amministrazione vendite
review_status: approved
module: DDT
aliases:
  - documento di trasporto
  - bolle
field_labels:
  - Stampato
  - Scaricato
  - Valorizzato
---
# Stati di gestione DDT

## Campi

### Stampato
Indica che il documento di trasporto è stato stampato in modo definitivo.

Il flag viene attivato nel momento in cui viene eseguita una stampa definitiva del DDT.

### Scaricato
Indica che il DDT è stato scaricato a magazzino.

Il flag viene attivato nel momento in cui viene eseguito lo scarico di magazzino tramite la relativa procedura.

### Valorizzato
Indica che il DDT è stato ripreso in fattura.

Il flag viene attivato quando il DDT è presente in una fattura ed è quindi stato valorizzato in fase di fatturazione.

## Regole

### Attivazione degli stati
Gli stati del DDT vengono aggiornati dalle procedure operative collegate alla stampa, allo scarico di magazzino e alla fatturazione.

### Stato Valorizzato
Un DDT risulta valorizzato quando viene ripreso in una fattura. La presenza del DDT nella fattura determina l'attivazione del flag Valorizzato.