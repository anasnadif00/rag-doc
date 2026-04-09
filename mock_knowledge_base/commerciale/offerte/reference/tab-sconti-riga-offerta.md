---
title: Tab Sconti della riga offerta
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - sconti riga offerta
  - tipi sconto
  - sconti visibili
  - sconti non visibili
  - totale netto riga
  - riepilogo ordine
task_tags:
  - riferimento sconti riga offerta
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Offerte
screen_title: Offerte
tab_name: Sconti
---
# Tab Sconti della riga offerta

## Regole
### Tipi di sconto visualizzati
Nel tab **Sconti** vengono visualizzati tutti i tipi di sconto definiti nella tabella dei parametri del commerciale se il tipo di sconto ha impostato l'opzione "visibile sulle righe".

### Sconti visibili sulle righe
Se un tipo di sconto è impostato in tabella come visibile sulle righe, lo sconto calcolato viene visualizzato sulla riga.

### Sconti non visibili sulle righe
Gli sconti non visibili sulle righe vengono comunque calcolati in base alle regole definite nella tabella **TP sconto**, ma non rientrano nel totale netto della riga.

### Riepilogo degli sconti
Gli sconti non visibili sulle righe rientrano solo nei dati di riepilogo dell'ordine, distinti per tipo di sconto.

### Origine degli sconti
La proposta degli sconti deriva dalle impostazioni presenti in:
- anagrafica cliente;
- anagrafica articoli;
- listini di vendita.