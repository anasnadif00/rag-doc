---
title: Parametri di Imposta data di trasporto
doc_kind: reference
domain: vendite
feature: ddt
keywords:
  - parametri Imposta data di trasporto
  - Elabora tutto
  - data inizio trasporto
  - ora inizio trasporto
  - DDT con data maggiore di un mese
task_tags:
  - riferimento parametri data trasporto DDT
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - amministrazione vendite
review_status: approved
module: DDT
submenu: Elaborazioni
aliases:
  - documento di trasporto
  - bolle
field_labels:
  - Parametri di inserimento
  - Data di inizio trasporto
  - Ora di inizio trasporto
  - Minuti
  - Elabora tutto
  - Ignora DDT con data maggiore di un mese
---
# Parametri di Imposta data di trasporto

## Campi

### Data di inizio trasporto
Definisce la data di inizio trasporto da impostare sui DDT elaborati.

### Ora di inizio trasporto
Definisce l'ora di inizio trasporto da impostare sui DDT elaborati.

### Minuti
Definisce i minuti dell'ora di inizio trasporto.

L'ora e i minuti sono gestiti in due campi separati.

### Elabora tutto
Determina se l'elaborazione deve essere applicata solo ai DDT selezionati oppure a tutti i DDT che soddisfano i filtri.

Se impostato a **No**, la procedura elabora solo i DDT selezionati nella parte a video.

Se impostato a **Sì**, la procedura elabora tutti i DDT che soddisfano il filtro, indipendentemente dai documenti visualizzati e selezionati.

### Ignora DDT con data maggiore di un mese
Determina il comportamento rispetto ai DDT per i quali la differenza tra la data del documento e la data del trasporto è maggiore di un mese.

Se impostato a **Sì**, la procedura considera anche i DDT in cui la differenza tra data documento e data trasporto è maggiore di un mese.

Se non impostato a **Sì**, questi DDT non vengono considerati.

## Regole

### Visualizzazione parziale dei risultati
La parte a video può mostrare un numero massimo di righe. Per questo motivo, potrebbero esistere DDT che soddisfano il filtro ma non sono visibili nella griglia.

### Elaborazione completa dei DDT filtrati
Per aggiornare tutti i DDT che soddisfano i filtri, anche quelli non visualizzati nella griglia, impostare **Elabora tutto** a **Sì**.