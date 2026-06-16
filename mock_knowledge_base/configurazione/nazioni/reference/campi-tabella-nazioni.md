---
title: Campi della tabella Nazioni
doc_kind: reference
domain: configurazione
feature: nazioni
keywords:
  - tabella nazioni
  - nazioni
  - stati esteri
  - codice nazione
  - blacklist
  - black list
  - codice black list
  - codice ISO2
  - codice ISO3
  - codice ISO numerico
  - gestione intrastat
  - caricamento solo prime sei colonne
  - valore statistico
task_tags:
  - riferimento campi nazioni
  - configurazione nazioni
  - configurazione intrastat
erp_versions:
  - v.1.0
role_scope:
  - admin
review_status: approved
module: Tabelle
screen_title: Nazioni
field_labels:
  - Codice
  - Descrizione
  - Blacklist
  - Codice black list
  - Codice ISO2
  - Codice ISO3
  - Codice ISO numerico
  - Gestione intrastat
  - Caricamento solo prime sei colonne
  - Valore
---
# Campi della tabella Nazioni

## Campi
### Codice
Contiene il codice univoco della nazione. Il codice può avere una lunghezza massima di tre caratteri.

### Descrizione
Contiene la descrizione dello stato estero.

### Blacklist
Identifica, tramite apposito flag, le nazioni che rientrano nella Black List.

### Codice black list
Contiene l'indicazione della nazione Black List di riferimento.

### Codice ISO2
Contiene il codice univoco di due caratteri della nazione, secondo gli standard internazionali.

### Codice ISO3
Contiene il codice alfanumerico di tre caratteri della nazione, secondo gli standard internazionali.

### Codice ISO numerico
Contiene il codice numerico di tre caratteri della nazione, secondo gli standard internazionali.

### Gestione intrastat
Consente di identificare, tramite apposito flag, le nazioni che rientrano nella gestione dell'Intrastat.

### Caricamento solo prime sei colonne
Viene utilizzato nella generazione del file Intrastat per produrre il flusso da inviare all'Agenzia delle Dogane.

### Valore
Campo numerico da indicare per il calcolo del valore statistico nella gestione dell'Intrastat.

## Regole
### Unicità del codice
Ogni nazione deve essere identificata da un codice univoco.

### Rilevanza della tabella
La corretta impostazione della tabella Nazioni è molto importante perché questa tabella viene utilizzata da diversi moduli di Magia.

### Utilizzo nella gestione Intrastat
I campi Gestione intrastat, Caricamento solo prime sei colonne e Valore sono utilizzati per la gestione e la generazione del flusso Intrastat.