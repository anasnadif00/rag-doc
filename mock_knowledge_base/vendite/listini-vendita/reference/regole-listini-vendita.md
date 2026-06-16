---
title: Regole dei Listini vendita
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - listini vendita
  - prezzi vendita
  - sconti articoli
  - listino cliente
  - campagna cliente
  - listino generale
  - campagna generale
  - prezzi ivati
task_tags:
  - riferimento regole listini vendita
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
screen_title: Listini vendita
field_labels:
  - Tipologia
  - Tipo listino
  - Cliente
  - Data di inizio
  - Data di fine
  - Divisa
---
# Regole dei Listini vendita

## Regole

### Prezzi inclusi IVA o esclusi IVA
Il modulo Listini vendita permette di gestire prezzi e sconti degli articoli destinati alla vendita.

I prezzi possono essere gestiti:
- inclusi IVA;
- esclusi IVA.

Il trattamento IVA del prezzo dipende dal tipo listino e dal flag prezzi ivati configurato nella tabella dei tipi listino.

### Listini generali e listini cliente
I listini prezzi possono essere:
- generali, validi per tutti i clienti;
- specifici per cliente, validi solo per il cliente indicato.

I listini possono essere associati all'anagrafica cliente per proporre automaticamente prezzi e condizioni nei documenti commerciali.

### Listini e campagne
La differenza tra listino e campagna riguarda la validità temporale.

Il listino ha una data di inizio ma non ha una data di fine. Resta valido fino a quando non viene superato da un altro listino.

La campagna ha una data di inizio e una data di fine. Le condizioni valgono solo nell'arco temporale indicato.

### Tipologie disponibili
La tipologia indica l'estensione di applicazione del listino in termini di tempo e di clienti.

I valori gestiti sono:
- campagna cliente;
- listino cliente;
- campagna generale;
- listino generale.

### Campagna cliente
La campagna cliente contiene condizioni valide solo per il cliente al quale viene abbinata.

Ha una data di inizio e una data di fine.

### Listino cliente
Il listino cliente contiene condizioni valide solo per il cliente al quale viene abbinato.

Ha una data di inizio certa e non prevede una data di fine.

### Campagna generale
La campagna generale contiene condizioni valide per tutti i clienti.

Ha una data di inizio e una data di fine.

### Listino generale
Il listino generale contiene condizioni valide per tutti i clienti.

Ha una data di inizio e non prevede una data di fine.

### Listini per singolo articolo
Le condizioni possono essere definite direttamente per uno specifico articolo.

### Listini collegati all'anagrafica articoli
Le condizioni possono essere collegate a elementi della anagrafica articoli.

Questa gestione permette di:
- accomunare più codici articolo alle stesse condizioni;
- specificare condizioni diverse per lo stesso articolo, ad esempio in base alla marca.

### Sconti cliente-articolo
Per gli sconti è disponibile una matrice cliente-articolo.

La matrice permette di creare:
- raggruppamenti di articoli;
- raggruppamenti di clienti;
- combinazioni di sconti definite in base ai criteri scelti dall'utente.

L'utente stabilisce le regole con cui ricercare gli sconti e applicare le offerte nei documenti.

### Integrazione con altri moduli
Il modulo Listini vendita è integrato con:
- Offerte clienti;
- Ordini clienti;
- DDT;
- Fatturazione.

Questi moduli leggono e propongono prezzi e sconti in relazione al cliente e agli articoli inseriti nei documenti.

### Priorità di ricerca
Prezzi, sconti e provvigioni possono essere presenti in più punti applicativi, ad esempio:
- Listini vendita;
- Anagrafica Agente;
- Anagrafica Cliente;
- gerarchia sconti.

La priorità di ricerca è determinata dalle tabelle:
- ricerca prezzi;
- ricerca sconti;
- ricerca provvigioni.