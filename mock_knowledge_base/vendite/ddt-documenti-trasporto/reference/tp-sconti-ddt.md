---
title: TP Sconti del DDT
doc_kind: reference
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - TP Sconti DDT
  - sconti DDT
  - sconti finali DDT
  - sconti di testata
  - sconti di riga
  - gestione valori bolle
task_tags:
  - riferimento TP Sconti DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Sconti
aliases:
  - sconti bolla
  - sconti documento di trasporto
field_labels:
  - Sconti finali
  - Sconti di testata
  - Sconti di riga
  - Visibile sulle righe
---
# TP Sconti del DDT

## Campi

### Sconti di testata
Nel TP Sconti sono presenti gli sconti inseriti nella tabella Parametri del commerciale che hanno impostata nella tabella Tipo sconto l'opzione sconto di testata.

### Sconti di riga
Nel TP Sconti vengono riepilogati anche gli sconti di riga che non hanno impostata nella tabella Tipo sconto l'opzione visibile sulle righe.

### Sconti finali
Gli sconti finali sono gestiti solo a percentuale.

Gli sconti finali vengono riportati automaticamente su tutte le righe.

## Regole

### Attivazione del TP Sconti
Il TP Sconti è attivo solo se nella tabella Parametri del commerciale è stato impostato il flag bolle Gestione valori.

Se il flag bolle Gestione valori non è impostato, il TP Sconti non viene visualizzato.

### Modifica degli sconti di testata
Eventuali modifiche alle percentuali di sconto della testata vengono riportate sulle righe per le quali gli sconti proposti non sono stati variati.

### Modifica degli sconti sulle righe
Gli sconti proposti sulle righe possono essere modificati solo se nella tabella Tipo sconto è stata impostata, per il tipo sconto utilizzato, l'opzione visibile sulle righe.

### Ricerca degli sconti
Gli sconti proposti vengono ricercati in base all'impostazione della tabella Ricerca sconti.