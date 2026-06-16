---
title: Tabella Parametri conti automatismi partite
doc_kind: reference
domain: contabilita
feature: parametri-conti-automatismi-partite
keywords:
  - parametri conti automatismi partite
  - chiusura partite
  - gestione movimenti
  - pannello partite
  - pagamenti fornitori
  - ritenute
  - contributi previdenziali
  - differenze cambi
  - abbuoni
  - sconti
  - spese
task_tags:
  - riferimento automatismi partite
  - configurazione conti chiusura partite
  - contabilizzazione pagamenti fornitori
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
screen_title: Parametri conti automatismi partite
aliases:
  - automatismi partite
  - conti automatismi partite
field_labels:
  - Tipo documento
  - Tipo documento-mastro
  - Tipo documento-partitario
  - Differenze cambi dare
  - Differenze cambi avere
  - Abbuono dare
  - Abbuono avere
  - Sconto dare
  - Sconto avere
  - Spese
  - Ritenuta dare
  - Ritenuta avere
  - Contributi previdenziali dare
  - Contributi previdenziali avere
---
# Tabella Parametri conti automatismi partite

## Campi
### Tipo documento
Consente di impostare automatismi per la registrazione di movimenti con chiusura partite in base al tipo documento.

### Tipo documento-mastro
Consente di impostare automatismi per la registrazione di movimenti con chiusura partite in base alla combinazione tra tipo documento e mastro.

### Tipo documento-partitario
Consente di impostare automatismi per la registrazione di movimenti con chiusura partite in base alla combinazione tra tipo documento e partitario.

### Differenze cambi dare
Conto utilizzabile per registrare differenze cambi in dare.

### Differenze cambi avere
Conto utilizzabile per registrare differenze cambi in avere.

### Abbuono dare
Conto utilizzabile per registrare abbuoni in dare.

### Abbuono avere
Conto utilizzabile per registrare abbuoni in avere.

### Sconto dare
Conto utilizzabile per registrare sconti in dare.

### Sconto avere
Conto utilizzabile per registrare sconti in avere.

### Spese
Conto utilizzabile per registrare le spese.

### Ritenuta dare
Conto utilizzabile per registrare ritenute in dare.

### Ritenuta avere
Conto utilizzabile per registrare ritenute in avere.

### Contributi previdenziali dare
Conto utilizzabile per registrare contributi previdenziali in dare.

### Contributi previdenziali avere
Conto utilizzabile per registrare contributi previdenziali in avere.

## Regole
### Ambito di utilizzo
La tabella consente di impostare una serie di automatismi per la registrazione di movimenti con chiusura partite.

### Livelli di configurazione
Gli automatismi possono essere definiti per:
- tipo documento
- tipo documento-mastro
- tipo documento-partitario

### Effetto sulla registrazione
I conti indicati in questa tabella vengono aggiunti alla registrazione per l'importo indicato nei campi corrispondenti del pannello Partite della gestione movimenti.

### Utilizzo nella contabilizzazione pagamenti
I dati indicati in questa tabella sono utilizzati anche dalla funzione di contabilizzazione pagamenti del modulo Pagamenti fornitori.

### Determinazione dei conti in contabilizzazione pagamenti
Nel modulo Pagamenti fornitori, i dati della tabella vengono utilizzati per determinare i conti contabili da utilizzare per:
- ritenute
- contributi
- differenze cambi positive
- differenze cambi negative

### Contesto del bonifico contabilizzato
La determinazione dei conti contabili avviene con riferimento ai valori presenti nel bonifico che si sta contabilizzando.