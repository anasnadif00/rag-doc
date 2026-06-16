---
title: Campi del TP Testata Fattura
doc_kind: reference
domain: commerciale
feature: fatture-vendita
keywords:
  - tp testata
  - campi fattura
  - tipo fattura
  - numero fattura
  - conto cliente
  - cig
  - cup
task_tags:
  - riferimento campi testata fattura
erp_versions:
  - v.1.0
role_scope:
  - amministrazione
  - commerciale
review_status: approved
module: Fatture
tab_name: Testata
field_labels:
  - Operatore
  - Data inserimento
  - Tipo
  - Numero
  - Data fattura
  - Magazzino
  - Causale
  - Conto
  - Divisa
  - Nostro riferimento
  - Vostro riferimento
  - CIG
  - CUP
---
# Campi del TP Testata Fattura

## Campi

### Operatore
Visualizza l'utente che sta inserendo il documento.

Il valore viene proposto automaticamente e non è modificabile.

### Data inserimento
Data di sistema relativa all'inserimento del documento.

Non è modificabile.

### Tipo
Definisce la tipologia della fattura.

Determina:

- numerazione del documento
- impostazioni predefinite
- comportamento della fattura

È possibile selezionarlo tramite elenco oppure digitando il codice se noto.

### Numero
Numero progressivo della fattura.

Può essere proposto automaticamente oppure inserito manualmente.

Si consiglia l'utilizzo della numerazione automatica per garantire continuità e progressività.

### Data fattura
Data del documento.

Viene proposta la data corrente ma può essere modificata.

### Magazzino
Campo disponibile esclusivamente per fatture accompagnatorie.

Indica il magazzino dal quale verrà prelevata la merce in uscita.

### Causale
Campo disponibile esclusivamente per fatture accompagnatorie.

Definisce la causale di magazzino utilizzata per la generazione dei movimenti.

Sono selezionabili esclusivamente causali con:

- Tipo causale = Scarico
- Flag Valida per il commerciale

### Conto
Cliente intestatario della fattura.

Può essere ricercato:

- tramite codice
- tramite digitazione parziale della descrizione

### Divisa
Se la fattura deriva da un ordine cliente viene ripresa automaticamente dall'ordine.

### Nostro riferimento
Campo descrittivo libero.

### Vostro riferimento
Campo descrittivo libero.

### CIG
Codice Identificativo Gara.

Utilizzato principalmente nei rapporti con la Pubblica Amministrazione.

L'informazione viene riportata nei documenti successivi.

### CUP
Codice Unico di Progetto.

Utilizzato principalmente per appalti pubblici.

L'informazione viene riportata nei documenti successivi.

## Regole

### Numerazione consigliata
Per evitare discontinuità numeriche e problematiche normative è consigliato utilizzare esclusivamente numerazioni automatiche.