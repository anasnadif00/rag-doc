---
title: TP Sconti del DDT
doc_kind: reference
domain: logistica
feature: ddt
keywords:
  - tp sconti ddt
  - sconti testata ddt
  - sconti riga ddt
  - sconti finali
  - gestione valori bolle
  - ricerca sconti
task_tags:
  - riferimento sconti ddt
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: DDT
tab_name: TP Sconti
field_labels:
  - Sconti finali
  - Sconto di testata
  - Visibile sulle righe
---
# TP Sconti del DDT

## Regole

### Contenuto del TP Sconti
Nel TP Sconti vengono riepilogati:
- sconti inseriti nella tabella Parametri del Commerciale
- sconti con opzione sconto di testata attiva nella tabella Tipo Sconto
- sconti di riga che non hanno attiva l'opzione visibile sulle righe

### Sconti finali
Gli sconti finali sono gestiti solo a percentuale.

Vengono riportati automaticamente su tutte le righe.

### Modifica sconti di testata
Eventuali modifiche alle percentuali di sconto della testata vengono riportate sulle righe per le quali gli sconti proposti non sono stati variati.

### Modifica sconti sulle righe
Gli sconti proposti sulle righe possono essere modificati se nella tabella Tipo Sconto, per il tipo sconto utilizzato, è attiva l'opzione visibile sulle righe.

### Ricerca sconti
Gli sconti proposti vengono ricercati in base alle impostazioni della tabella Ricerca sconti.

### Attivazione TP Sconti
Il TP Sconti è visibile solo se nella tabella Parametri del Commerciale è attivo il flag bolle Gestione valori.