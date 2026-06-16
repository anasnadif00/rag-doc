---
title: Invio DDT via mail
doc_kind: how_to
domain: logistica
feature: ddt
keywords:
  - invio ddt mail
  - mail ddt
  - invio automatico ddt
  - mail messaggi
  - ddt inviati
task_tags:
  - invio ddt mail
  - gestione invio ddt
erp_versions:
  - v.1.0
role_scope:
  - magazzino
  - logistica
  - amministrazione vendite
review_status: approved
module: DDT
field_labels:
  - Stampate
  - Inviati
  - Da inviare
  - Tipo bolla
  - Data
  - Cliente
  - Ragione sociale
---
# Invio DDT via mail

## Prerequisiti
Verificare che:
- siano configurati i messaggi nella tabella "Mail messaggi"
- il cliente abbia un indirizzo mail valido
- i DDT siano selezionabili secondo i filtri impostati

## Procedura
1. Accedere alla funzione "Invio DDT via mail".
2. Impostare i filtri desiderati:
   - tipologia messaggio
   - stampate sì/no
   - inviati sì/no
   - da inviare
   - tipo bolla
   - anno
   - intervallo date
   - numero cliente
   - ragione sociale
3. Selezionare i DDT da inviare.
4. Avviare la funzione "Apri".
5. Attendere il completamento dell'elaborazione.
6. Consultare il log finale dell'elaborazione.

## Regole
### Configurazione messaggi
Le regole di invio vengono definite nella tabella:
- "Mail messaggi"

### Memorizzazione invii
Gli estremi dell'invio effettuato vengono memorizzati nella gestione:
- "TP mail inviato"

## Verifiche finali
Verificare che:
- il DDT risulti inviato
- il log non riporti errori
- il cliente abbia ricevuto il documento
