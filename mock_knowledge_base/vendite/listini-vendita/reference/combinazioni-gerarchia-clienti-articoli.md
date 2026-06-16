---
title: Combinazioni gerarchia clienti articoli
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - gerarchia clienti articoli
  - combinazione cliente articolo
  - combinazione gerarchia clienti
  - combinazione gerarchia articoli
  - sconti cliente articolo
task_tags:
  - riferimento combinazioni gerarchia clienti articoli
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
submenu: Gestione dei listini vendita
screen_title: Gerarchia sconti
tab_name: Gerarchia clienti articoli
field_labels:
  - Cliente
  - Articolo
  - Gerarchia clienti
  - Gerarchia articoli
---
# Combinazioni gerarchia clienti articoli

## Regole

### Scontistica per combinazione
Nel TP Gerarchia clienti articoli è possibile gestire una scontistica diversa in relazione a diverse combinazioni di Gerarchia clienti e Gerarchia articoli.

La compilazione dei campi di testata consente di determinare a quali clienti e articoli applicare gli sconti.

### Articolo e cliente
Se vengono compilati Articolo e Cliente, gli sconti inseriti vengono applicati solo in presenza dello specifico codice cliente e dello specifico codice articolo.

### Articolo e gerarchia clienti
Se vengono compilati Articolo e Gerarchia clienti, gli sconti vengono applicati a tutti i clienti appartenenti alla gerarchia indicata, ma solo per l'articolo indicato.

### Gerarchia articoli e cliente
Se vengono compilati Gerarchia articoli e Cliente, gli sconti vengono applicati solo al cliente indicato e agli articoli appartenenti alla gerarchia articoli selezionata.

### Gerarchia articoli e gerarchia clienti
Se vengono compilati Gerarchia articoli e Gerarchia clienti, gli sconti vengono applicati solo ai clienti appartenenti alla gerarchia clienti indicata e solo agli articoli appartenenti alla gerarchia articoli indicata.

### Uso della gerarchia di base
La gerarchia indicata, sia per gli articoli sia per i clienti, può essere la gerarchia di base.

In questo caso l'applicazione viene generalizzata a tutti i clienti e a tutti gli articoli non inseriti in una gerarchia specifica.