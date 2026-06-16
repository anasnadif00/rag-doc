---
title: Campi della tabella Registri IVA
doc_kind: reference
domain: contabilita
feature: registri-iva
keywords:
  - registri IVA
  - registro IVA
  - codice registro IVA
  - tipo IVA
  - ultimo mese stampato
  - stampa riepilogo
  - stampa liquidazione
task_tags:
  - riferimento registri iva
  - configurazione registri iva
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità
screen_title: Registri IVA
aliases:
  - tabella Registri IVA
field_labels:
  - Codice
  - Descrizione
  - Descrizione estesa
  - Tipo IVA
  - Ultimo mese stampato
  - Stampa riepilogo
  - Stampa liquidazione
---
# Campi della tabella Registri IVA

La tabella **Registri IVA** contiene la lista delle codifiche dei registri IVA relativi all'azienda.

## Campi

### Codice
Identifica in modo univoco il registro IVA.

Il codice può essere composto da un massimo di 2 caratteri.

### Descrizione
Consente di inserire la descrizione del registro IVA.

### Descrizione estesa
Consente di inserire una descrizione più lunga del registro IVA.

### Tipo IVA
Consente di selezionare la tipologia del registro IVA.

Il campo è obbligatorio.

Le tipologie disponibili sono:
- **Acquisti**
- **Vendite**
- **Corrispettivi**

### Ultimo mese stampato
Contiene l'indicazione dell'ultimo mese che è stato stampato in modalità definitiva per quel registro.

### Stampa riepilogo
Può essere impostato a **Sì** oppure **No**.

Se il campo è impostato a **Sì**, la numerazione delle pagine liquidazione IVA stampata dal riepilogo dell'applicazione **Registro IVA** sarà quella del sezionale.

### Stampa liquidazione
Può essere impostato a **Sì** oppure **No**.

Se il campo è impostato a **Sì**, la numerazione delle pagine liquidazione IVA stampata dall'applicazione **Prospetto liquidazione IVA periodica** sarà quella del sezionale.

## Regole

### Unicità del codice
Ogni registro IVA deve essere identificato da un codice univoco.

### Lunghezza massima del codice
Il codice del registro IVA può contenere al massimo 2 caratteri.

### Obbligatorietà del tipo IVA
Il campo **Tipo IVA** è obbligatorio.

### Valori ammessi per il tipo IVA
Il campo **Tipo IVA** può assumere esclusivamente uno dei seguenti valori:
- **Acquisti**
- **Vendite**
- **Corrispettivi**

### Regola di selezione per Stampa riepilogo
Per ogni società, il campo **Stampa riepilogo** può essere impostato a **Sì** per un solo registro IVA.

### Regola di selezione per Stampa liquidazione
Per ogni società, il campo **Stampa liquidazione** può essere impostato a **Sì** per un solo registro IVA.

### Effetto del flag Stampa riepilogo
Quando **Stampa riepilogo** è impostato a **Sì**, la numerazione delle pagine liquidazione IVA stampata dal riepilogo dell'applicazione **Registro IVA** utilizza quella del sezionale.

### Effetto del flag Stampa liquidazione
Quando **Stampa liquidazione** è impostato a **Sì**, la numerazione delle pagine liquidazione IVA stampata dall'applicazione **Prospetto liquidazione IVA periodica** utilizza quella del sezionale.

### Tracciamento dell'ultima stampa definitiva
Il campo **Ultimo mese stampato** memorizza il riferimento all'ultimo mese stampato in modalità definitiva per il registro IVA.