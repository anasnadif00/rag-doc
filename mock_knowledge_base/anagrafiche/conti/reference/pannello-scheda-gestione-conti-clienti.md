---
title: Pannello Scheda della gestione Conti clienti
doc_kind: reference
domain: anagrafiche
feature: conti
keywords:
  - scheda conti
  - pannello scheda
  - conti clienti
  - esposizione cliente
  - saldo cliente
  - effetti cliente
  - insoluti cliente
  - fido cliente
  - dilazione media
  - scaduto a scadere
task_tags:
  - riferimento pannello scheda conti
  - consultazione situazione cliente
erp_versions:
  - v.1.0
role_scope:
  - all
review_status: approved
module: Conti
submenu: Scheda
screen_title: Conti-Scheda
tab_name: Scheda
aliases:
  - scheda conto
  - riepilogo cliente
  - situazione cliente
field_labels:
  - Ordinato non consegnato
  - In spedizione
  - Consegnato
  - Fatture non contabilizzate
  - Saldo
  - Effetti
  - Insoluti
  - Esposizione
  - Fido
  - Dilazione media
  - Dilazione media anni
  - Dilazione media concessa
  - Dilazione media concessa anni
  - Solleciti al grado
---
# Pannello Scheda della gestione Conti clienti

## Regole
### Finalità del pannello
Il pannello Scheda della gestione Conti contiene, in formato grafico, un riepilogo della situazione dei conti specificati, identificati come clienti.

## Campi
### Ordinato non consegnato
È l'importo degli ordini non consegnati con data minore alla data odierna, aventi tipo ordine da elaborare, stato ordine non consegnato oppure stato ordine bloccato ma con stato precedente non consegnato.

### In spedizione
È il valore dei buoni di spedizione inseriti senza riferimenti a bolle o fatture, con data minore o uguale alla data odierna.

### Consegnato
È il valore delle bolle non valorizzate da fatturare, con data di inserimento minore o uguale alla data odierna.

### Fatture non contabilizzate
È l'importo delle fatture non pro forma non contabilizzate, con data di inserimento minore o uguale alla data odierna e con totale fattura diverso da zero.

### Saldo
È il valore contabile alla data odierna.

### Effetti
È il valore estratto dalla contabilità in base ai tipi documento con tipo natura pari a effetti, con data di registrazione minore o uguale alla data odierna e data di scadenza maggiore o uguale alla data di esposizione. La data di esposizione corrisponde alla data di registrazione più i giorni di tolleranza indicati nelle tabelle del modulo cartellino clienti.

### Insoluti
È il valore dei movimenti estratti dalla contabilità con tipo documento impostato come insoluti, con data di registrazione minore o uguale alla data odierna.

### Esposizione
È la somma dei valori di:
- saldo
- effetti
- ordinato non consegnato
- bolle non consegnate
- fatture non contabilizzate
- spedizioni

### Fido
E' l'importo del fido dall'anagrafica oppure dalle tabelle del cartellino, in base alla versione indicata in Magia.

### Dilazione media
È la media dei giorni intercorsi tra i pagamenti e le fatture rilevati nei movimenti contabili dell'ultimo anno.

### Dilazione media anni
È la dilazione dei giorni tra i pagamenti e le fatture rilevati nei movimenti contabili dell'anno precedente.

### Dilazione media concessa
È la media dei giorni tra le scadenze e le relative fatture rilevati nei movimenti contabili dell'ultimo anno.

### Dilazione media concessa anni
È la media dei giorni tra i pagamenti e le fatture rilevati nei movimenti contabili dell'anno precedente.

### Solleciti al grado
Indica i solleciti emessi con i vari gradi impostati.

### Riepilogo finale scaduto a scadere
Il riepilogo finale scaduto a scadere viene calcolato sulle partite ed è suddiviso nelle seguenti fasce:
- tra 0 e 30 giorni
- tra 30 e 60 giorni
- tra 60 e 90 giorni
- tra 90 e 120 giorni
- oltre 120 giorni