---
title: Stampa etichette DDT
doc_kind: how_to
domain: logistica
feature: ddt
keywords:
  - etichette ddt
  - stampa etichette ddt
  - numero colli
  - etichette spedizione
task_tags:
  - stampa etichette ddt
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - logistica
review_status: approved
module: DDT
field_labels:
  - Tipo bolla
  - Magazzino
  - Numero etichette
  - Numero colli
---
# Stampa etichette DDT

## Procedura
1. Accedere alla funzione "Etichette DDT".
2. Impostare i filtri desiderati:
   - tipo di bolla
   - magazzino
   - intervallo numeri DDT
   - anno
   - intervallo date
   - cliente
3. Inserire il numero etichette desiderato.
4. Attivare eventualmente il flag:
   - "Numerazione per numero colli"
5. Avviare la stampa delle etichette.

## Regole
### Numero etichette
Per default viene stampata una etichetta.

### Numerazione per numero colli
Se attivo il flag:
- "Numerazione per numero colli"

vengono stampate tante etichette quanti sono i colli presenti nel DDT.

### Destinazione etichette
Le etichette possono riportare:
- il luogo di destinazione diverso dall'indirizzo del cliente

### Formati di stampa
I formati di stampa sono generalmente personalizzati per cliente.

## Verifiche finali
Verificare che:
- il numero di etichette generate sia corretto
- il destinatario riportato sia corretto
- eventuali colli siano rappresentati correttamente