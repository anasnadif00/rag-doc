---
title: Prezzi sconti e listini nelle righe fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - prezzo fattura
  - listino vendita
  - sconti fattura
  - importo netto
  - importo lordo
task_tags:
  - riferimento prezzi fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
field_labels:
  - Prezzo
  - Importo lordo
  - Importo netto
  - Sconti
---
# Prezzi sconti e listini nelle righe fattura

## Regole

### Obbligatorietà del prezzo
Il prezzo è obbligatorio se nell'anagrafica articolo, nel TP Dati Gestionali, è attiva l'opzione:

- Solo fatturazione

### Determinazione del prezzo
Il prezzo può essere proposto:

- dal listino di vendita
- dal prezzo di vendita dell'anagrafica articolo

se non viene trovato un prezzo valido nel listino.

### Ricerca del listino
Il listino da applicare viene determinato secondo le priorità definite nella tabella di ricerca prezzi.

### Inserimento manuale
Se non sono presenti automatismi specifici il prezzo può essere modificato o inserito manualmente dall'utente.

### Sconti
Gli sconti vengono determinati in base alle regole presenti nel TP Sconti.

Possono derivare da:

- listini
- gerarchie sconti
- sconti inseriti direttamente nella riga articolo

### Sconti visibili sulle righe
Se il tipo sconto ha attiva l'opzione:

- Visibile sulle righe

lo sconto viene applicato e totalizzato direttamente nell'importo netto della riga.

### Sconti non visibili sulle righe
Gli sconti non visibili sulle righe:

- utilizzano come base di calcolo l'importo della riga
- vengono riepilogati esclusivamente negli sconti di testata

### Aggiornamento degli sconti
È disponibile una funzione che consente di rileggere e ricalcolare gli sconti nel caso siano state effettuate modifiche successive nelle tabelle di configurazione parametri del commerciale.