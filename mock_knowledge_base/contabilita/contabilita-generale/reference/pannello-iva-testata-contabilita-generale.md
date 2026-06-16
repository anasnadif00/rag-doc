---
title: Pannello IVA di testata della Contabilità Generale
doc_kind: reference
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - pannello IVA
  - modalità IVA
  - aliquota IVA
  - imponibile
  - imposta
  - plafond
  - competenza plafond
task_tags:
  - riferimento pannello IVA contabilità generale
  - riepilogo IVA registrazione
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Contabilità Generale
tab_name: Iva
field_labels:
  - Modalità IVA
  - Descrizione
  - Aliquota IVA
  - Competenza plafond
  - Imponibile
  - Imposta
  - Plafond
---
# Pannello IVA di testata della Contabilità Generale

Il pannello IVA contiene il riepilogo delle modalità e delle aliquote IVA imputate nelle varie righe della registrazione.

## Campi
### Modalità IVA
È il codice della modalità IVA.

La stessa modalità IVA può essere presente su più righe del movimento.

### Descrizione
È la descrizione della modalità IVA codificata nella tabella Modalità IVA.

### Aliquota IVA
È l'aliquota applicata.

Vengono aggregate tutte le righe aventi la stessa aliquota a parità di Modalità IVA.

### Competenza plafond
È la competenza del movimento rispetto al calcolo dell'utilizzo del plafond.

Possono essere presenti più righe con competenza diversa nel caso in cui la fattura derivi da DDT di mesi diversi.

### Imponibile
È la somma degli importi di riga movimentati indicando una modalità IVA, anche quando la modalità è:
- non imponibile
- non soggetta
- esente
- altre modalità senza imposta

### Imposta
È l'importo dell'imposta calcolata sull'imponibile in base all'aliquota.

### Plafond
È l'importo residuo del plafond calcolato in base alle impostazioni di competenza e dei tipi documento o modalità da considerare.

## Regole
### Condizioni di attivazione
Il pannello IVA si attiva quando il Tipo documento utilizzato ha selezionato in tabella Tipo documento uno dei parametri Tipo IVA diversi da Non gestito.

Tipicamente il pannello si attiva per:
- fatture di acquisto
- fatture di vendita
- note di credito
- corrispettivi

### Logica di aggregazione
Il riepilogo aggrega i dati IVA delle righe di registrazione in base a:
- Modalità IVA
- Aliquota IVA

### Gestione della competenza plafond
La competenza plafond può differire tra righe della stessa registrazione se il documento deriva da DDT di periodi diversi.