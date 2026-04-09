---
title: Stati e avanzamenti dell'offerta
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - stato offerta
  - avanzamento offerta
  - offerta inserita
  - offerta bloccata
  - offerta stampata
  - offerta evasa
  - motivi avanzamento
  - probabilità di chiusura
task_tags:
  - riferimento stati offerta
  - riferimento avanzamenti offerta
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Offerte
screen_title: Offerte
tab_name: TP Testata
field_labels:
  - Stato
  - Avanzamento
  - Data avanzamento
  - Motivo avanzamento
  - Chiusura
---
# Stati e avanzamenti dell'offerta

## Campi

### Stato
Definisce lo stato operativo in cui si trova l'offerta.

### Avanzamento
Definisce lo stato di avanzamento commerciale dell'offerta. I valori sono selezionabili dalla tendina proposta.

### Data avanzamento
Per ogni variazione dell'avanzamento è possibile inserire la relativa data nel campo dedicato.

### Motivo avanzamento
È un campo tabellare che consente di associare un motivo allo stato di avanzamento. I motivi sono codificabili nella tabella **Motivi di avanzamento**.

### Chiusura
Indica la probabilità di chiusura dell'offerta. I valori sono configurabili nella tabella **Probabilità di chiusura**.

## Regole

### Stati gestiti
Gli stati descritti per l'offerta sono i seguenti:

#### Inserito
È lo stato iniziale da cui parte normalmente l'offerta.

#### Annullato
Può essere impostato nel caso in cui l'offerta non venga accettata dal cliente.

#### Bloccato
Viene impostato automaticamente dal programma se nell'anagrafica del cliente è presente una categoria amministrativa con il blocco in offerte attivato.

#### Stampato
Viene impostato quando l'offerta viene stampata in definitiva.

#### Evasa
Viene impostato automaticamente quando dall'offerta viene creato l'ordine cliente e quindi l'offerta viene trasformata in ordine. Può essere impostato anche in caso di evasione forzata.

### Avanzamenti descritti
Gli avanzamenti riportati sono:

#### Rivisto
Indica che l'offerta ha subito revisioni.

#### In corso
Indica che l'offerta è ancora in corso di valutazione.

#### Vinta parzialmente
Indica che è stata accettata solo una parte dell'offerta.

#### Vinta totalmente
Indica che l'intera offerta è stata accettata dal cliente.

#### Persa
Indica che il cliente non ha accettato l'offerta.

### Gestione della probabilità di chiusura
Il campo **Chiusura** non è un testo libero. I valori devono essere impostati nella tabella **Probabilità di chiusura** e possono essere descritti secondo le esigenze dell'utente.