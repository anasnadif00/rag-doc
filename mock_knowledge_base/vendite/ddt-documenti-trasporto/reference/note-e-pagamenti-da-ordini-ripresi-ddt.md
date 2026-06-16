---
title: Note e pagamenti da ordini ripresi nel DDT
doc_kind: reference
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - note da ordine DDT
  - pagamenti da ordine DDT
  - condizioni pagamento DDT
  - righe corpo DDT
  - codice validità Note
task_tags:
  - riferimento dati ripresi da ordine
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - magazzino
  - amministrazione vendite
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Ripresa ordini
aliases:
  - bolla da ordine
  - note ordine DDT
field_labels:
  - Note di testata
  - Condizioni di pagamento
  - Codice validità Note
---
# Note e pagamenti da ordini ripresi nel DDT

## Regole

### Note di testata degli ordini
Le note di testata degli ordini ripresi diventano righe del corpo del DDT.

Queste righe assumono come codice articolo l'articolo impostato nel TPI dati gestionali.

Le righe assumono inoltre lo stesso codice di validità presente nella tabella Parameteri del commerciale con codice validità Note.

### Condizioni di pagamento diverse
Se gli ordini ripresi hanno condizioni di pagamento diverse, le condizioni vengono riportate sulle singole righe del DDT.

In testata viene riportata la condizione di pagamento di un solo ordine.

### Informazioni provenienti dagli ordini
Il DDT generato tramite ripresa ordini mantiene le informazioni presenti negli ordini selezionati, salvo le regole specifiche previste per campi con valori diversi o per campi gestiti a livello di riga.