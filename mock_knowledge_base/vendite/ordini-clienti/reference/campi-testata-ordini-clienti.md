---
title: Campi della testata Ordini clienti
doc_kind: reference
domain: vendite
feature: ordini-clienti
keywords:
  - campi testata ordine cliente
  - tipo ordine
  - numero ordine
  - data ordine
  - cliente
  - divisa
  - CIG
  - CUP
  - stato ordine
task_tags:
  - riferimento campi testata ordine cliente
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Ordini clienti
screen_title: Ordini clienti
tab_name: Testata
aliases:
  - testata ordine cliente
field_labels:
  - Operatore
  - Data inserimento
  - Tipo
  - Numero
  - Data ordine
  - Cliente
  - Divisa
  - Riferimento
  - Nostro riferimento
  - Vostro riferimento
  - CUP
  - CIG
  - All'attenzione
  - Stato
---
# Campi della testata Ordini clienti

## Campi

### Operatore
Indica l'operatore che ha inserito l'ordine.

### Data inserimento
Viene normalmente proposta dal sistema e non è modificabile dall'operatore.

### Tipo
Il campo **Tipo** definisce il comportamento di alcuni parametri e di alcune funzioni dell'ordine.

Oltre a classificare la tipologia dell'ordine, il tipo consente di definire:
- la numerazione da adottare
- l'eventuale condivisione o separazione della numerazione rispetto ad altre tipologie
- parametri di default dell'ordine
- dati COIN di default
- regole di modifica in funzione dello stato dell'ordine o della riga
- sequenza di inserimento dei vari campi

### Numero
È il campo nel quale viene attribuita la numerazione dell'ordine. Solitamente viene proposto automaticamente, ma può anche essere inserito manualmente.

### Data ordine
Viene normalmente proposta con la data odierna, ma può essere modificata.

### Cliente
Indica il conto al quale viene intestato l'ordine.

### Divisa
Viene proposta in base alla divisa impostata nell'anagrafica del cliente selezionato.


### Nostro riferimento
Campo descrittivo libero per indicare il referente interno relativo all'ordine.

### Vostro riferimento
Campo descrittivo libero per indicare il referente esterno relativo all'ordine.

### CUP
Consente di inserire il **Codice Unico di Progetto**. È un dato normalmente utilizzato per la pubblica amministrazione e viene riportato nei documenti successivi all'ordine.

### CIG
Consente di inserire il **Codice Identificativo di Gara**. È un dato normalmente utilizzato negli appalti con la pubblica amministrazione e viene riportato nei documenti successivi all'ordine.

### Attenzione
Campo libero che consente di indicare il nominativo o il riferimento al quale inviare l'ordine.

### Stato
Indica lo stato dell'ordine. I valori disponibili derivano da una tabella sottostante non modificabile dall'utente.

## Regole

### Stato Inserito
Lo stato **Inserito** viene assunto automaticamente al momento dell'inserimento dell'ordine.

### Stato Annullato
Lo stato **Annullato** viene impostato manualmente quando l'ordine non deve più essere considerato in alcuna elaborazione.

### Stato Bloccato
Lo stato **Bloccato** viene assunto automaticamente quando il cliente ha una categoria amministrativa che provoca il blocco, come definito nella tabella **Categorie amministrative**.

### Stato Confermato
Lo stato **Confermato** viene assunto automaticamente quando viene eseguita la stampa definitiva dell'ordine.

### Stato Evaso
Lo stato **Evaso** viene assunto quando l'ordine viene evaso con DDT, fattura oppure tramite evasione forzata.