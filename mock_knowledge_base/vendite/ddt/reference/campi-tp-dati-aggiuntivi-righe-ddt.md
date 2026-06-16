---
title: Campi del TP dati aggiuntivi nelle righe DDT
doc_kind: reference
domain: vendite
feature: ddt
keywords:
  - DDT
  - TP dati aggiuntivi
  - articolo cliente
  - magazzino DDT
  - marca
  - opzione
  - tipo fatturato
  - modalità IVA
  - aliquota IVA
task_tags:
  - riferimento TP dati aggiuntivi DDT
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
  - magazzino
review_status: approved
module: Vendite
screen_title: DDT
tab_name: TP dati aggiuntivi
field_labels:
  - Articolo cliente
  - Magazzino
  - Marca
  - Opzione
  - Tipo fatturato
  - Modalità IVA
  - Aliquota IVA
  - Vostro riferimento
  - Ordine della riga
---
# Campi del TP dati aggiuntivi nelle righe DDT

## Campi

### Articolo cliente
Il campo Articolo cliente permette di indicare il codice con cui il cliente identifica il proprio prodotto.

Se nella tabella Parametri del commerciale è attiva l'opzione Articolo cliente e il codice articolo è già stato indicato, il campo viene compilato automaticamente quando viene richiamato l'articolo di magazzino.

L'informazione può essere ripresa dalla tabella Articolo cliente, dove sono memorizzate le corrispondenze tra:

- codici articoli interni;
- codici articoli del cliente.

### Magazzino
Il campo Magazzino indica il magazzino da movimentare.

Normalmente viene proposto il magazzino indicato in testata, ma può essere modificato sulla singola riga.

### Marca
Il campo Marca è attivo solo se l'opzione Marca è stata attivata nella tabella Parametri del commerciale.

Permette di indicare la marca di vendita per l'articolo specificato.

### Opzione
Il campo Opzione permette di indicare una variante rispetto al prodotto base.

L'informazione è codificata nella tabella Opzione distinta base imballo.

Il campo può essere compilato automaticamente se il valore è presente nel TP dati gestionali della grafica articoli. In mancanza, viene proposto il valore presente nel TP condizioni dei diritti.

### Tipo fatturato
Il campo Tipo fatturato permette di dichiarare il tipo fatturato di vendita della riga.

Il tipo fatturato di vendita identifica il conto che verrà movimentato quando sarà generato il relativo movimento contabile.

Viene proposto il tipo di fatturato presente nell'anagrafica degli articoli, ma resta modificabile.

### Modalità IVA
Il campo Modalità IVA indica il tipo di assoggettamento IVA da applicare alla singola riga del DDT.

La modalità IVA viene proposta secondo questa priorità:

1. modalità IVA presente nell'anagrafica cliente;
2. modalità IVA presente nell'anagrafica articolo, se codificata;
3. modalità IVA presente nella tabella Tipo fatturato di vendita per cliente;
4. modalità IVA presente nella tabella Tipo fatturato di vendita.

Se non viene trovata alcuna modalità IVA, deve essere inserita manualmente dall'operatore scegliendo tra le modalità IVA presenti nella tabella.

### Aliquota IVA
Il campo Aliquota IVA permette di indicare l'aliquota IVA quando la riga è soggetta ad IVA.

L'aliquota IVA viene proposta secondo questa priorità:

1. aliquota presente nell'anagrafica dell'articolo, se codificata;
2. aliquota presente nella tabella Tipi di fatturato di vendita per cliente;
3. aliquota presente nella tabella Tipo fatturato di vendita.

Se non viene trovata alcuna aliquota, deve essere inserita manualmente dall'operatore.

### Vostro riferimento
Il campo Vostro riferimento permette di indicare un riferimento interno del cliente per la riga inserita o gestita.

### Ordine della riga
Il campo Ordine della riga viene compilato automaticamente se la riga è stata ripresa da un ordine.

In questo caso riporta i riferimenti dell'ordine ripreso nel DDT.

## Regole

### Proposta dei dati aggiuntivi
I dati aggiuntivi di riga possono essere proposti automaticamente in base a:

- testata del DDT;
- articolo di magazzino;
- anagrafica cliente;
- anagrafica articolo;
- Parametri del commerciale;
- tabella Articolo cliente;
- tabella Tipo fatturato di vendita per cliente;
- tabella Tipo fatturato di vendita;
- ordine ripreso.

### Modificabilità dei dati
I valori proposti nei campi del TP dati aggiuntivi sono modificabili quando la procedura lo consente.
