---
title: Campi della testata Listini vendita
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - testata listino vendita
  - tipologia listino
  - tipo listino
  - cliente listino
  - data inizio listino
  - data fine listino
  - divisa listino
task_tags:
  - riferimento campi testata listini vendita
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
screen_title: Listini vendita
tab_name: Testata
field_labels:
  - Tipologia
  - Tipo listino
  - Cliente
  - Data di inizio
  - Data di fine
  - Divisa
---
# Campi della testata Listini vendita

## Campi

### Tipologia
Indica l'estensione di applicazione del listino in termini di tempo e di clienti.

Può assumere i seguenti valori:
- campagna cliente;
- listino cliente;
- campagna generale;
- listino generale.

### Tipo listino
Indica il codice con cui viene classificato il listino.

Il campo si attiva solo se la Tipologia è:
- listino generale;
- campagna generale.

Il codice tipo listino viene associato al cliente nella relativa anagrafica e può essere proposto di default nei documenti in cui viene richiamato il cliente.

Dal tipo listino deriva anche il trattamento IVA del prezzo.

Se il tipo listino ha attivo il flag prezzi ivati, nei documenti il prezzo è considerato comprensivo di IVA e viene eseguito lo scorporo IVA.

Se il flag prezzi ivati non è attivo, l'IVA viene aggiunta al prezzo.

### Cliente
Indica il codice cliente al quale associare le condizioni inserite.

Il campo è attivo solo se la Tipologia è:
- listino cliente;
- campagna cliente.

Per listino generale e campagna generale il campo non è necessario, perché le condizioni sono valide per tutti i clienti.

### Data di inizio
Indica la data dalla quale decorre la validità del listino o della campagna.

### Data di fine
Indica la data fino alla quale sono valide le condizioni inserite.

Il campo si attiva solo se la Tipologia è:
- campagna generale;
- campagna cliente.

Nei listini generali e nei listini cliente è prevista solo la Data di inizio.

### Divisa
Indica la divisa nella quale sono espressi i prezzi inseriti.

La divisa deve essere scelta tra quelle gestite per il cliente.

Il campo deve essere valorizzato anche per i listini in euro, selezionando l'apposita voce dall'help.

## Regole

### Prezzi ivati per listino cliente
Quando si inserisce un listino con Tipologia uguale a listino cliente, il campo Tipo listino è disabilitato.

In questo caso, per determinare se i prezzi sono comprensivi di IVA o meno, si usa il tipo listino associato nell'anagrafica del cliente.
