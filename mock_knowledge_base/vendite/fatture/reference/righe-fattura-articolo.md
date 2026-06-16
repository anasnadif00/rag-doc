---
title: Righe articolo della fattura
doc_kind: reference
domain: vendite
feature: fatture
keywords:
  - righe fattura
  - articoli fattura
  - quantità fattura
  - prezzo fattura
  - sconti fattura
  - articolo cliente
task_tags:
  - riferimento righe fattura
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Fatture
field_labels:
  - Numero riga
  - Tipo riga
  - Articolo
  - Descrizione
  - Quantità
  - Prezzo
  - Importo lordo
  - Importo netto
---
# Righe articolo della fattura

## Regole

### Inserimento delle righe
Le righe della fattura possono essere:

- riprese automaticamente da ordini clienti
- riprese automaticamente da DDT
- inserite manualmente tramite il pulsante "+" verde

Nel caso di fatture generate da ordini o DDT, gli articoli vengono compilati automaticamente in base ai documenti ripresi.

### Numero riga
Il campo numero riga identifica il progressivo della riga.

La numerazione proposta da Magia parte normalmente da 10 e prosegue con incrementi successivi, multipli di 10.

Il valore può comunque essere modificato dall'operatore.

### Articolo
Il campo articolo identifica il codice dell'articolo presente in magazzino.

Il codice può essere:

- inserito manualmente
- proposto automaticamente tramite articolo cliente
- acquisito tramite barcode nelle versioni Mexp che supporta tale funzionalità

### Descrizione
Per gli articoli codificati la descrizione può essere proposta automaticamente e non è modificabile.

Per:

- articoli non codificati
- note
- spese

la descrizione può essere modificata liberamente dall'utente.

### Articoli non codificati
Gli articoli non codificati consentono di utilizzare un codice generico e inserire liberamente il contenuto della descrizione.

### Importo lordo
L'importo lordo viene calcolato automaticamente come:

- quantità × prezzo

### Importo netto
L'importo netto viene calcolato come:

- quantità × prezzo
- al netto degli sconti applicati

### Riga omaggio
Le righe di tipo omaggio vengono elaborate come normali articoli.

La differenza si presenta in fase di totalizzazione:

- il valore della riga non viene sommato al totale documento
- l'IVA viene applicata secondo le impostazioni dell'articolo

Se nell'anagrafica articolo è attivo il flag "Omaggio IVATO", il comportamento fiscale segue tale configurazione.