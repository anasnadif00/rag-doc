---
title: Pannello Compenso di testata della Contabilità Generale
doc_kind: reference
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - pannello compenso
  - percipienti
  - ritenute
  - contributi
  - cassa previdenziale
  - rimborsi
  - fattura proforma
  - fattura passiva
task_tags:
  - riferimento pannello compenso contabilità generale
  - gestione compensi percipienti
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Contabilità Generale
tab_name: Compenso
field_labels:
  - Compenso
  - Causale
  - Tipologia prestazione
  - Importo compenso
  - Percentuale assoggettamento
  - Imponibile
  - Non imponibile
  - Percentuale ritenuta
  - Ritenuta
  - Rimborsi
  - IVA
  - Cassa previdenziale
  - Imponibile contributo
  - Contributo
  - Contributo collaboratore
---
# Pannello Compenso di testata della Contabilità Generale

Il pannello Compenso consente di registrare le informazioni dettagliate dei compensi a percipienti per la rilevazione della ritenuta e dei contributi.

I dati inseriti vengono ripresi ed elaborati nel modulo Percipienti.

## Campi
### Compenso
Se è spuntato vengono ripresi i dati del percipiente dall'anagrafica e applicati agli importi del movimento.

### Causale
Indica la natura del compenso.

Se impostata nell'anagrafica del fornitore viene proposta in automatico.

### Tipologia prestazione
Indica la tipologia della prestazione, ad esempio:
- regime ordinario
- occasionale
- forfettario

Viene proposta in automatico in base a quanto indicato nell'anagrafica del fornitore, ma è modificabile.

### Importo compenso
Viene proposto in base all'importo indicato nei conti del movimento diversi da quello del fornitore e dell'IVA.

Può essere modificato.

### Percentuale assoggettamento
È la percentuale del compenso assoggettata a ritenuta.

Può essere impostata nell'anagrafica del fornitore, ma può essere modificata.

### Imponibile
Viene calcolato applicando all'Importo compenso la Percentuale assoggettamento.

Se la percentuale non corrisponde al 100%, in questo campo viene calcolato l'importo corrispondente e la differenza viene inserita nel campo Non imponibile.

### Non imponibile
È l'importo calcolato sulla differenza tra Importo compenso e Imponibile.

### Percentuale ritenuta
È la percentuale da applicare al compenso per calcolare la ritenuta.

Può essere impostata nell'anagrafica del fornitore, ma è modificabile.

### Ritenuta
È l'importo calcolato sull'Imponibile in base alla Percentuale ritenuta.

Tale importo viene detratto dal netto da pagare al fornitore.

### Rimborsi
Sono le spese eventualmente sostenute dal fornitore in nome e per conto del cliente e da lui anticipate.

Possono essere indicate:
- manualmente dall'operatore
- in automatico, se nella registrazione sono presenti su un conto specifico con una modalità IVA specifica indicata nella tabella Modalità IVA rimborsi percipienti

### IVA
È l'importo dell'IVA ripreso dal corpo del pannello Dettaglio.

### Cassa previdenziale
È l'importo eventualmente indicato dal fornitore nella parcella come contributo alla cassa previdenziale di appartenenza.

Se nella registrazione è indicata in un conto separato nel dettaglio delle righe di movimento e tale conto è inserito nella tabella Conti cassa previdenziale, l'importo viene proposto direttamente. In caso contrario deve essere indicato manualmente dall'operatore.

Tale importo è un di cui dell'Importo compenso.

### Imponibile contributo
È la parte del compenso assoggettata al calcolo dei contributi.

Viene calcolata in base alla percentuale indicata nell'anagrafica del fornitore oppure impostata manualmente al momento della registrazione.

### Contributo
È l'importo calcolato in base all'Imponibile contributo e alla percentuale indicata nell'anagrafica del fornitore.

### Contributo collaboratore
È la parte del contributo calcolato che viene detratta dal netto da pagare al fornitore.

## Regole
### Condizioni di attivazione
Il pannello Compenso si attiva quando si verificano contemporaneamente le seguenti condizioni:
- il Tipo documento ha impostato Tipo IVA a Acquisti oppure Fattura IVA proforma
- il Tipo documento ha impostato il parametro Percipienti a Compenso
- il fornitore intestatario del documento ha attivato il flag Percipienti in anagrafica

### Avviso in salvataggio
Al momento del salvataggio del movimento, se le condizioni di attivazione sono presenti ma i dati non sono ancora stati compilati, compare un messaggio di avviso che ricorda la compilazione del pannello.

### Generazione del compenso
Cliccando su Genera compenso è possibile compilare i campi del pannello.

### Alimentazione automatica dei rimborsi
Il campo Rimborsi può essere alimentato automaticamente quando nella registrazione sono presenti importi su conti specifici con una modalità IVA configurata nella tabella Modalità IVA rimborsi percipienti.

### Alimentazione automatica della cassa previdenziale
Il campo Cassa previdenziale può essere alimentato automaticamente quando l'importo è registrato su un conto presente nella tabella Conti cassa previdenziale.