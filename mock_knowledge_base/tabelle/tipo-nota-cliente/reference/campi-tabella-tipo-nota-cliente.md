---
title: Campi della tabella Tipo nota cliente
doc_kind: reference
domain: tabelle
feature: tipo-nota-cliente
keywords:
  - tipo nota cliente
  - tabella tipo nota cliente
  - note cliente
  - note commerciale
  - stampe da escludere
  - ordini clienti
  - DDT
  - fatture
  - fatture elettroniche
  - spedizioni
task_tags:
  - riferimento tabella tipo nota cliente
erp_versions:
  - v.1.0
role_scope:
  - utente
review_status: approved
module: Tabelle
screen_title: Tipo nota cliente
field_labels:
  - Codice
  - Descrizione
  - Ordini clienti
  - DDT
  - Fatture
  - Fatture elettroniche
  - Spedizioni
  - Iniziale
  - Finale
  - Stampe da escludere
  - Società
  - Divisione
  - Operatore
---
# Campi della tabella Tipo nota cliente

## Campi
### Codice
Identifica in modo univoco il tipo di nota cliente. Il codice può contenere al massimo tre caratteri.

### Descrizione
Contiene la descrizione della tipologia di nota cliente.

### Ordini clienti
Indica se la tipologia di nota cliente può essere associata agli ordini clienti.

### DDT
Indica se la tipologia di nota cliente può essere associata ai DDT.

### Fatture
Indica se la tipologia di nota cliente può essere associata alle fatture.

### Fatture elettroniche
Indica se la tipologia di nota cliente può essere associata alle fatture elettroniche.

### Spedizioni
Indica se la tipologia di nota cliente può essere associata alle spedizioni.

### Iniziale
Indica che la nota è di tipo iniziale.

### Finale
Indica che la nota è di tipo finale.

### Stampe da escludere
Consente di indicare i report sui quali la nota non deve comparire.

### Società
Permette di restringere l'esclusione della stampa a una specifica società.

### Divisione
Permette di restringere l'esclusione della stampa a una specifica divisione.

### Operatore
Permette di restringere l'esclusione della stampa a uno specifico operatore.

## Regole
### Ambito di utilizzo
La tabella Tipo nota cliente consente di classificare la tipologia delle note che possono essere associate ai moduli del commerciale.

### Associazione ai moduli
Per ogni tipologia di nota cliente è possibile definire su quali moduli commerciali la nota deve essere gestita: ordini clienti, DDT, fatture, fatture elettroniche e spedizioni.

### Posizionamento della nota
Per ogni tipologia di nota cliente è possibile indicare se la nota è di tipo iniziale oppure finale.

### Esclusione dalle stampe
Dopo avere definito le impostazioni sui vari moduli, nella sezione Stampe da escludere è possibile indicare i report sui quali la nota non deve comparire.

### Restrizioni aggiuntive
L'esclusione dalle stampe può essere ulteriormente limitata specificando società, divisione e operatore.