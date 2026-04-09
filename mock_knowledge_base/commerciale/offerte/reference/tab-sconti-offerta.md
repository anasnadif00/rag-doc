---
title: Campi e regole del tab TP Sconti dell'offerta
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - tp sconti offerta
  - sconti testata offerta
  - sconti riga offerta
  - visibile sulle righe
  - ricerca sconti
  - parametri commerciale
task_tags:
  - riferimento sconti offerta
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Offerte
screen_title: Offerte
tab_name: TP Sconti
field_labels:
  - Sconti iniziali
  - Sconti finali
---
# Campi e regole del tab TP Sconti dell'offerta

## Campi

### Sconti iniziali
Consentono di applicare sconti di testata all'offerta.

### Sconti finali
Consentono di applicare sconti di testata all'offerta.

## Regole

### Origine degli sconti di testata
Nel tab vengono proposti gli sconti inseriti nei parametri del commerciale che, nella tabella **Tipi di sconto**, hanno l'opzione **Sconto di testata** attivata.

### Riepilogo degli sconti di riga non visibili
Nel tab vengono riepilogati anche gli sconti di riga che, nella tabella **Tipo di sconto**, non hanno impostata l'opzione **Visibile sulle righe**.

### Gestione percentuale
Gli sconti iniziali e finali sono gestiti solo in percentuale.

### Riporto automatico sulle righe
Gli sconti di testata vengono riportati automaticamente su tutte le righe.

### Aggiornamento delle righe
Le modifiche alle percentuali di sconto in testata vengono riportate su tutte le righe per le quali gli sconti non sono stati variati manualmente.

### Modifica degli sconti proposti sulle righe
Gli sconti proposti sulle righe possono essere modificati solo se, nella tabella **Tipo di sconto**, per il tipo di sconto utilizzato è stata impostata l'opzione **Visibile sulle righe**.

### Criterio di ricerca degli sconti
Gli sconti proposti vengono ricercati in base all'impostazione della tabella **Ricerca sconti**.