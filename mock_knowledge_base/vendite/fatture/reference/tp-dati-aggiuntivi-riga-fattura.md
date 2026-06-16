---
title: TP Dati Aggiuntivi della riga fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - tp dati aggiuntivi fattura
  - articolo cliente
  - marca
  - magazzino
  - imballo
  - tipo fatturato
task_tags:
  - riferimento dati aggiuntivi riga fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
tab_name: TP Dati Aggiuntivi
field_labels:
  - Articolo cliente
  - Marca
  - Magazzino
  - Imballo
  - Tipo fatturato
  - Modalità IVA
  - Aliquota IVA
  - Vostro riferimento
---
# TP Dati Aggiuntivi della riga fattura

## Campi

### Articolo cliente
Consente di indicare il codice con cui il cliente identifica il prodotto.

Se nei Parametri del Commerciale è attiva l'opzione "Articolo cliente gestito" e il codice articolo è già stato indicato, il campo viene compilato automaticamente prelevando l'informazione dalla relativa tabella.

### Marca
È attivo solo se nei Parametri del Commerciale è attiva l'opzione "Marca".

Consente di indicare la marca di vendita dell'articolo.

La marca viene normalmente proposta dall'anagrafica articolo ma può essere modificata.

### Magazzino
È attivo se la fattura è di tipo accompagnatorio.

Indica il magazzino da movimentare e quindi da scaricare.

Viene proposto il magazzino indicato in testata ma può essere modificato riga per riga.

Se la fattura non è accompagnatoria, il campo è disattivato.

### Imballo
Viene proposto dal TP Condizioni dell'ordine o del DDT precedente.

È collegato alla tabella Imballo.

### Tipo fatturato
Indica il fatturato di vendita e determina il conto che verrà movimentato con la contabilizzazione della fattura.

Solitamente viene proposto dall'anagrafica articolo ma può essere modificato.

### Vostro riferimento
Campo libero che consente di indicare un riferimento interno del cliente per la riga articolo.

### Riferimenti ordine e DDT
I campi di riferimento ordine e DDT vengono compilati automaticamente dal programma quando la fattura deriva da ripresa ordine o valorizzazione DDT.

## Regole

### Effetto della marca sul prezzo
La marca può influenzare il prezzo proposto se il listino è agganciato alla marca.