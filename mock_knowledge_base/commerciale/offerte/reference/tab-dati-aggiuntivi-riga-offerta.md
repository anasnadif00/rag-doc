---
title: Tab Dati aggiuntivi della riga offerta
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - dati aggiuntivi riga offerta
  - articolo cliente
  - marca
  - magazzino
  - opzione
  - imballo
  - tipo fatturato
  - modalità iva
  - aliquota iva
  - vostro riferimento
task_tags:
  - riferimento dati aggiuntivi riga offerta
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Offerte
screen_title: Offerte
tab_name: Dati aggiuntivi
field_labels:
  - Articolo cliente
  - Marca
  - Magazzino
  - Opzione
  - Imballo
  - Tipo fatturato
  - Modalità IVA
  - Aliquota
  - Vostro riferimento
---
# Tab Dati aggiuntivi della riga offerta

## Campi
### Articolo cliente
Consente di indicare il codice con cui il cliente identifica il prodotto.

### Marca
Consente di indicare la marca di vendita dell'articolo specificato.

### Magazzino
Se indicato, viene utilizzato come magazzino di scarico in un eventuale DDT di vendita successivo.

### Opzione
Consente di indicare una variante rispetto al prodotto base.

### Imballo
È un campo che viene compilato automaticamente se presente nei dati gestionali dell'anagrafica articoli. In mancanza, viene proposto quello presente nel TP condizioni della testata dell'offerta, se valorizzato.

### Tipo fatturato
Consente di indicare il tipo di fatturato di vendita. Può essere usato per associare la riga a un conto di ricavo in fase di contabilizzazione della fattura collegata all'offerta.

### Modalità IVA
Indica la modalità IVA della riga.

### Aliquota
Indica l'aliquota IVA relativa alla modalità IVA inserita.

### Vostro riferimento
È un campo di libera compilazione a livello di riga. Può essere diverso dal valore inserito in testata.

## Regole
### Proposta automatica dei dati
I dati aggiuntivi possono essere proposti automaticamente in base a quanto impostato nell'articolo o nei parametri del commerciale.

### Compilazione automatica di Articolo cliente
Il campo **Articolo cliente** viene compilato automaticamente se:
- nella tabella parametri del commerciale è attiva l'opzione **articolo cliente**;
- è stato indicato il codice articolo;
- esiste la corrispondenza nella tabella **articolo cliente** tra codice articolo interno e codice cliente.

### Attivazione del campo Marca
Il campo **Marca** è attivo solo se nella tabella parametri del commerciale è attivata l'opzione **marca**.

### Origine dell'opzione
L'informazione **Opzione** è codificata nella tabella **opzioni distinta base**.

### Proposta di Tipo fatturato
Il **Tipo fatturato** viene proposto automaticamente se presente nell'anagrafica articolo.

### Proposta di Modalità IVA
La **Modalità IVA** viene proposta automaticamente dall'anagrafica articolo. In alternativa può essere proposta dalla tabella **tipo fatturato di vendita per cliente**. Se non proposta, può essere inserita manualmente.

### Obbligatorietà della Modalità IVA
La **Modalità IVA** è un dato obbligatorio.

### Proposta dell'Aliquota
L'**Aliquota** viene proposta:
- dall'anagrafica articolo, se presente;
- altrimenti dalla tabella **tipi fatturato di vendita per cliente**;
- altrimenti dalla tabella **tipi fatturato di vendita**.

### Obbligatorietà dell'Aliquota
Se la riga è soggetta a IVA, l'**Aliquota** deve essere impostata. In assenza di proposta automatica, deve essere scelta tra le aliquote disponibili nella tabella delle aliquote IVA.