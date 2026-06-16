---
title: Soluzione Pagamento
doc_kind: reference
domain: contabilita
feature: soluzione-pagamento
keywords:
  - soluzione pagamento
  - dilazioni di pagamento
  - scadenze pagamento
  - giorni di scadenza
  - imponibile iva
  - solo iva
  - solo imponibile
  - imponibile ed iva
  - descrizione in lingua
task_tags:
  - riferimento soluzione pagamento
  - configurazione dilazioni pagamento
  - configurazione scadenze
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Tabelle
screen_title: Soluzione Pagamento
aliases:
  - tabella soluzione pagamento
  - soluzioni di pagamento
field_labels:
  - Codice
  - Descrizione
  - Descrizione in lingua
  - Giorni di scadenza
  - Imponibile IVA
---
# Soluzione Pagamento

## Campi
### Codice
L'identificativo univoco di una soluzione di pagamento è un codice univoco di massimo tre caratteri.

### Descrizione
Descrizione della soluzione di pagamento.

### Descrizione in lingua
Attraverso il pannello descrizione in lingua è possibile indicare la descrizione della soluzione di pagamento nella lingua desiderata.

### Giorni di scadenza
Per ogni soluzione di pagamento devono essere indicati uno o più giorni di scadenza.

Magia utilizza questi giorni per calcolare la data di scadenza delle partite nei seguenti ambiti:
- fatturazione
- controllo fatture
- contabilità

### Imponibile IVA
Nella griglia di inserimento multiplo è possibile indicare, per ciascuna riga, il criterio di calcolo Imponibile/IVA.

Le opzioni disponibili sono:
- solo IVA
- solo imponibile
- imponibile ed IVA

## Regole
### Funzione della tabella
La tabella Soluzione Pagamento consente di codificare le dilazioni di pagamento da associare al tipo di pagamento per la determinazione delle scadenze.

### Inserimento multiplo delle scadenze
All'interno della tabella Soluzione Pagamento è possibile inserire più righe, ciascuna con propri giorni di scadenza e propria indicazione Imponibile/IVA.

### Gestione delle soluzioni singole
Le soluzioni singole impostate come solo IVA o solo imponibile vengono gestite solo se è attiva l'impostazione IVA anticipata.

### Calcolo standard degli importi delle partite
Se non viene utilizzata l'impostazione IVA anticipata, il calcolo degli importi delle partite e delle relative scadenze viene effettuato sull'importo totale dato da imponibile più imposta.

### Moduli che gestiscono la scissione automatica
La scissione automatica tra solo IVA e solo imponibile può essere effettuata dal modulo della fatturazione e dal modulo del controllo fatture.

Questa gestione non viene effettuata direttamente dalla contabilità.