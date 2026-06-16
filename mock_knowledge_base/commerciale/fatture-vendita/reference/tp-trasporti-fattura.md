---
title: Campi e regole del TP Trasporti
doc_kind: reference
domain: commerciale
feature: fatture-vendita
keywords:
  - tp trasporti
  - trasporto fattura
  - vettore
  - data trasporto
  - ora trasporto
  - cura mittente
task_tags:
  - riferimento trasporti fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - logistica
review_status: approved
module: Fatture
tab_name: Trasporti
field_labels:
  - Tipo trasporto
  - Data inizio trasporto
  - Ora inizio trasporto
  - Vettore
---
# Campi e regole del TP Trasporti

## Campi

### Tipo trasporto
Definisce il soggetto che esegue il trasporto della merce.

Le opzioni disponibili sono:

- A cura del mittente
- A cura del destinatario
- A cura del vettore

### Data inizio trasporto
Indica la data di inizio del trasporto.

### Ora inizio trasporto
Indica l'ora di inizio del trasporto.

### Vettore
Può essere selezionato quando il trasporto è eseguito a cura del vettore.

## Regole

### Disponibilità del TP
Il TP Trasporti è disponibile esclusivamente per le fatture di tipo accompagnatoria.

Per tutte le altre tipologie di fattura il tab viene automaticamente disabilitato.

### Proposta automatica del vettore
Se nell'anagrafica cliente, nel TP Dati commerciali, è stato configurato un vettore predefinito, questo viene proposto automaticamente durante l'inserimento della fattura.

Il valore può comunque essere modificato dall'operatore.

### Gestione automatica delle note del vettore
Se il vettore selezionato possiede note associate nella relativa tabella Vettore, tali note vengono riportate automaticamente nel TP Note della fattura.

### Aggiornamento delle note
In caso di modifica del vettore:

- le note vengono aggiornate con quelle del nuovo vettore

In caso di eliminazione del vettore:

- le note vengono eliminate

L'aggiornamento automatico viene effettuato solamente se il testo delle note non è stato modificato manualmente dall'utente.