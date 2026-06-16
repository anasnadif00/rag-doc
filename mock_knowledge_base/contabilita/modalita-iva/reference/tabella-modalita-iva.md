---
title: Tabella Modalità IVA
doc_kind: reference
domain: contabilita
feature: modalita-iva
keywords:
  - modalità IVA
  - tabella modalità IVA
  - tipo IVA
  - spese bollo
  - plafond
  - IVA CEE
  - split payment
  - reverse charge
  - natura operazione dati fatture
  - dichiarazioni d'intento
  - esterometro
  - autofattura
  - modalità iva indetraibile
  - modalità detraibile
  - percentuale indetraibile
  - nota fattura
task_tags:
  - riferimento modalità IVA
  - configurazione tabella IVA
  - gestione parametri IVA
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità
screen_title: Modalità IVA
aliases:
  - tabella modalità iva
field_labels:
  - Codice
  - Descrizione
  - Tipo IVA
  - Spese bollo
  - Plafond
  - IVA CEE
  - Escludi da comunicazione IVA
  - Escludi da esterometro
  - Modalità IVA CEE
  - Modalità IVA Indetraibile
  - Percentuale indetraibile
  - Modalità detraibile
  - Split Payment
  - Forma pagamento
  - Esponi in black list
  - Dichiarazioni d'intento
  - Reverse charge
  - Escludi da autofattura
  - Natura operazione dati fatture
  - Nota fattura
---
# Tabella Modalità IVA

La tabella Modalità IVA consente di codificare la lista delle modalità IVA utilizzate all'interno di Magia.

## Campi

### Codice
È un identificativo univoco di al massimo tre caratteri.

### Descrizione
È la descrizione della modalità IVA.

### Tipo IVA
Indica l'assoggettamento o l'esclusione dal campo di applicazione dell'aliquota IVA.

I valori possibili sono:
- esente, non imponibile
- imponibile
- imponibile indetraibile
- IVA indetraibile

### Spese bollo
Il flag spese bollo viene richiamato in fase di contabilizzazione fatture dal modulo fatturazione. Se questo è attivato, vengono applicate alla fattura le spese di bollo per l'importo indicato nella tabella tipi fatturato vendite.

### Plafond
Se il flag è attivato, consente di considerare i movimenti con questa Modalità IVA ai fini del calcolo del plafond. Devono essere attivate anche le altre impostazioni previste per questa gestione; per i dettagli vedere la gestione movimenti plafond.

I movimenti con questa Modalità IVA vengono inoltre esposti nel registro plafond della stampa registro IVA.

### IVA CEE
Se il flag è attivato, consente la separata esposizione degli importi relativi a questa Modalità IVA:
- nel registro IVA riepiloghi
- nel prospetto di liquidazione IVA periodica

### Escludi da comunicazione IVA
Se attivato, consente di non considerare gli importi associati alla modalità IVA all'interno della comunicazione liquidazione IVA periodica.

### Escludi da esterometro
Se attivato, consente di non considerare gli importi associati alla modalità IVA all'interno dell'esterometro.

### Modalità IVA CEE
Indica la modalità IVA che verrà utilizzata nella registrazione automatica delle fatture intra CEE.

Per ulteriori dettagli vedere anche l'utilizzo della tabella Parametri registrazione IVA comunitaria.

### Modalità IVA Indetraibile
Si attiva nel caso in cui il Tipo IVA sia impostato a imponibile indetraibile. In questo caso deve essere indicata la modalità IVA indetraibile da associare.

### Percentuale indetraibile
Si attiva solo nel caso di Tipo IVA impostato a imponibile indetraibile.

Indica la percentuale di indetraibilità sull'IVA. L'importo relativo viene riportato in una nuova riga della registrazione contabile con lo stesso conto della riga di imponibile.

### Modalità detraibile
Si attiva solo nel caso di Tipo IVA impostato a imponibile indetraibile.

Indica la modalità IVA con cui viene registrata la parte di IVA detraibile.

### Split Payment
Se il flag è attivato, consente di identificare la modalità IVA utilizzata all'interno della Fatturazione per riconoscere la scissione dei pagamenti.

### Forma pagamento
Il campo forma pagamento permette di impostare la forma di pagamento da inserire sulla partita generata con l'importo relativo allo split payment.

### Esponi in black list
Se attivato, consente di estrarre i valori associati alla modalità IVA all'interno della black list.

### Dichiarazioni d'intento
Questo flag viene utilizzato dai programmi di fatturazione per riconoscere, qualora l'impostazione sia attivata, le condizioni che fanno scattare i controlli relativi alla dichiarazione d'intento e ai plafond.

### Reverse charge
Se attivato, permette di identificare le modalità IVA soggette a inversione contabile e quindi di attivare, tramite la tabella Parametri registrazione IVA comunitaria, gli automatismi adeguati alla compilazione delle varie registrazioni.

### Escludi da autofattura
Se attivato, permette di identificare le modalità IVA da escludere nella generazione, da parte degli automatismi di Magia, delle autofatture.

### Natura operazione dati fatture
Contiene l'indicazione del codice N associato alla modalità IVA, in base alle disposizioni ministeriali relative alla fatturazione elettronica.

### Nota fattura
Ad ogni modalità IVA codificata è possibile associare, dal pannello Nota fattura, una particolare tipologia di nota cliente e descrizione. Questa informazione viene caricata automaticamente nei documenti di vendita quando viene utilizzata la modalità IVA collegata.

## Regole

### Attivazione dei campi per imponibile indetraibile
I campi Modalità IVA Indetraibile, Percentuale indetraibile e Modalità detraibile si attivano solo quando il Tipo IVA è impostato a imponibile indetraibile.

### Applicazione delle spese di bollo
Il flag Spese bollo viene utilizzato in fase di contabilizzazione fatture dal modulo Fatturazione e applica l'importo definito nella tabella tipi fatturato vendite.

### Gestione plafond
Perché i movimenti siano considerati ai fini del plafond non è sufficiente il solo flag Plafond: devono essere attivate anche le ulteriori impostazioni previste nella gestione movimenti plafond.

### Gestione intra CEE e reverse charge
I campi Modalità IVA CEE e Reverse charge sono collegati agli automatismi governati dalla tabella Parametri registrazione IVA comunitaria.

### Esclusioni da adempimenti
I flag Escludi da comunicazione IVA, Escludi da esterometro ed Escludi da autofattura consentono di escludere gli importi associati alla modalità IVA dai rispettivi automatismi e adempimenti.

### Associazione automatica delle note
Se per una modalità IVA è configurata una Nota fattura, la relativa tipologia di nota cliente e descrizione viene proposta automaticamente nei documenti di vendita che utilizzano quella modalità IVA.