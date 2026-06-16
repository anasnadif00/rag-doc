---
title: TP Sconti della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - tp sconti fattura
  - sconti riga fattura
  - sconti visibili sulle righe
  - sconti testata
  - gerarchie sconti
task_tags:
  - riferimento sconti riga fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Sconti
field_labels:
  - Sconti
  - Importo netto
---
# TP Sconti della riga fattura

## Regole

### Origine degli sconti
Nel TP Sconti vengono riepilogati gli sconti applicati alla riga.

Gli sconti possono derivare da:
- listini
- gerarchie sconti
- sconti inseriti nel TP Articolo nel campo sconto

### Tipi di sconto visualizzati
Nel TP Sconti vengono visualizzati i tipi di sconto presenti nella tabella Parametri del Commerciale.

### Sconti visibili sulle righe
Se il tipo sconto ha attiva l'opzione "Visibile sulle righe", lo sconto calcolato viene:
- visualizzato sulla riga
- totalizzato nell'importo netto della riga

### Sconti non visibili sulle righe
Gli sconti non visibili sulle righe:
- hanno come base di calcolo l'importo della riga
- vengono totalizzati solo nel TP Sconto di testata

### Sconto di testata
Il TP Sconto di testata contiene il riepilogo complessivo degli sconti applicati al totale del documento.

### Rilettura sconti
Attraverso l'icona superiore è possibile rileggere gli sconti quando sono state effettuate modifiche nella tabella Parametri del Commerciale dopo l'inserimento della fattura.