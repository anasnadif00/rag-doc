---
title: Campi del pannello Dettaglio in Società
doc_kind: reference
domain: contabilita
feature: societa
keywords:
  - società dettaglio
  - campi società
  - partita IVA società
  - liquidazione IVA
  - primo giorno in linea
  - ultimo giorno in linea
  - percorso condiviso allegati
task_tags:
  - riferimento campi società
  - configurazione società
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilita
screen_title: Società
tab_name: Dettaglio
field_labels:
  - Codice
  - Descrizione
  - Descrizione estesa
  - Divisa
  - Mese inizio
  - Mese fine
  - Partita IVA
  - Liquidazione IVA
  - Gestione
  - Data Euro
  - Primo giorno in linea
  - Ultimo giorno in linea
  - Data ultima registrazione stampata
  - Ultimo numero stampato
  - Intestazione giornale 1
  - Intestazione giornale 2
  - Percorso condiviso allegati
  - Percorso condiviso allegati su Linux
source_uri: trascrizione-utentee-tabella-societa
---
# Campi del pannello Dettaglio in Società

## Campi

### Codice
Contiene l'identificativo della società. È un campo di due caratteri.

### Descrizione
Contiene il nome della società. Ha una lunghezza di 20 caratteri.

### Descrizione estesa
Contiene il nome della società. Ha una lunghezza fino a 45 caratteri.

### Divisa
Contiene la valuta della moneta di conto gestita abitualmente in Magia. Di default la divisa viene impostata a euro.

### Mese inizio
Contiene il codice (numero) del mese di inizio dell'esercizio fiscale contabile.

### Mese fine
Contiene il codice (numero) del mese di fine dell'esercizio fiscale contabile.

### Partita IVA
Contiene l'identificativo fiscale della società.

### Liquidazione IVA
Può essere impostata a **mensile** o **trimestrale** a seconda della periodicità della liquidazione dell'IVA della società.

### Gestione
Contiene i flag relativi alla gestione:

- dei corrispettivi
- delle partite aperte
- della numerazione automaitca delle pagine del libro giornale, dei registri e della liquidazione IVA.

### Data Euro
Contiene la data di inizio gestione in moneta euro dopo le lire. La data viene normalmente già impostata al primo gennaio 2002.

### Primo giorno in linea
Contiene il primo giorno del periodo in cui è possibile operare all'interno dei dati contabili di Magia.

### Ultimo giorno in linea
Contiene la data di fine del periodo in cui è possibile operare all'interno dei dati contabili di Magia.

### Data ultima registrazione stampata
Contiene l'ultima data di registrazione stampata in definitiva dal libro giornale.

### Ultimo numero stampato
Contiene l'ultimo numero di registrazione stampato all'interno del libro giornale in definitivo.

### Intestazione giornale 1
Contiene la prima riga di descrizione dell'intestazione della società per la stampa del libro giornale.

### Intestazione giornale 2
Contiene la seconda riga di descrizione dell'intestazione della società per la stampa del libro giornale.

### Percorso condiviso allegati
Contiene il percorso della cartella per gli allegati.

### Percorso condiviso allegati su Linux
Contiene il percorso della cartella degli allegati su Linux.

## Regole

### Periodo operativo
I campi **Primo giorno in linea** e **Ultimo giorno in linea** definiscono l'intervallo temporale entro il quale è possibile operare nei dati contabili di Magia.

### Gestione valuta
La **Divisa** viene impostata di default a euro.

### Gestione della liquidazione IVA
La periodicità della **Liquidazione IVA** deve essere coerente con la modalità di liquidazione prevista per la società.