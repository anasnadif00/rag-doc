---
title: Banca e Azienda
doc_kind: reference
domain: contabilita
feature: banca-e-azienda
keywords:
  - banca e azienda
  - banche azienda
  - pagamento fornitori
  - portafoglio effetti
  - bonifici sepa
  - sepa direct debit
  - iban
  - conto bonifici
  - conto assegni
  - tipo assegno
  - codice azienda
  - codice cook
  - cin
  - abi
  - cab
  - conto corrente
  - codice conto
  - castelletto
task_tags:
  - riferimento banca e azienda
  - configurazione banche azienda
  - configurazione bonifici sepa
  - configurazione sepa direct debit
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Tabelle
screen_title: Banca e Azienda
aliases:
  - tabella banca e azienda
  - banche dell'azienda
field_labels:
  - Codice
  - IBAN
  - Codice Cook
  - CIN
  - ABI
  - CAB
  - Conto Corrente
  - Codice Conto
  - Tipo Castelletto
  - Castelletto sconto
  - Castelletto incassi giorni incasso
  - Effetti a vista giorni incasso
  - Effetti non a vista giorni sconto
  - Tasso sconto
  - Tasso anticipo
  - Importo commissioni conto
  - Conto Bonifici
  - Conto Assegni
  - Tipo Assegno
  - Ultimo numero assegno
  - Sigla banca
  - Codice Azienda
  - Impostazione SEPA
  - Metodo di pagamento
  - Priorità
  - Addebito cumulativo
  - Identificativo del soggetto privato
---
# Banche Azienda

## Campi
### Pannelli principali
La tabella **Banche Azienda** si compone di tre pannelli principali:
- **Banca**
- **Bonifici SEPA**
- **SEPA Direct Debit**

## Campi
### Pannello Banca

#### Codice
Il campo **Codice** viene assegnato dall'utente e identifica la banca.

#### IBAN
Il campo **IBAN** viene calcolato automaticamente una volta inseriti i dati nei campi **CIN**, **ABI**, **CAB** e **Conto Corrente**.

#### Codice CUC
Il campo **Codice CUC** è presente nel pannello **Banca**.

#### CIN
Il campo **CIN** è utilizzato per il calcolo automatico dell'IBAN.

#### ABI
Il campo **ABI** è utilizzato per il calcolo automatico dell'IBAN.

#### CAB
Il campo **CAB** è utilizzato per il calcolo automatico dell'IBAN.

#### Conto Corrente
Il campo **Conto Corrente** è utilizzato per il calcolo automatico dell'IBAN.

#### Codice Conto
Il campo **Codice Conto** è il codice del conto contabile a cui associare la banca che si sta inserendo.

Viene utilizzato nel caso di tipo incasso impostato a **RID** nella tabella **tipi pagamento fornitori**.

#### Tipo Castelletto
Il campo **Tipo Castelletto** è presente nel pannello **Banca**.

#### Castelletto sconto
Il campo **Castelletto sconto** è presente nel pannello **Banca**.

#### Castelletto incassi giorni incasso
Il campo **Castelletto incassi giorni incasso** è presente nel pannello **Banca**.

#### Effetti a vista giorni incasso
Il campo **Effetti a vista giorni incasso** è presente nel pannello **Banca**.

#### Effetti non a vista giorni sconto
Il campo **Effetti non a vista giorni sconto** è presente nel pannello **Banca**.

#### Tasso sconto
Il campo **Tasso sconto** è presente nel pannello **Banca**.

#### Tasso anticipo
Il campo **Tasso anticipo** è presente nel pannello **Banca**.

#### Importo commissioni conto
Il campo **Importo commissioni conto** è presente nel pannello **Banca**.

#### Conto Bonifici
Il campo **Conto Bonifici** è il conto di contabilità che verrà addebitato al momento della contabilizzazione del pagamento.

#### Conto Assegni
Il campo **Conto Assegni** è il conto di contabilità che verrà addebitato al momento della contabilizzazione dei pagamenti nel caso in cui il tipo pagamento fornitore sia di tipo assegno.

#### Tipo Assegno
Il campo **Tipo Assegno** consente di selezionare una delle seguenti opzioni:
- **per fornitore**
- **per partita**

Con l'opzione **per fornitore** viene emesso un assegno unico per tutte le partite di quel fornitore presenti in un pagamento.

Con l'opzione **per partita** vengono emessi tanti assegni quante sono le partite.

#### Ultimo numero assegno
Il campo **Ultimo numero assegno** è presente nel pannello **Banca**.

#### Sigla banca
Il campo **Sigla banca** è presente nel pannello **Banca**.

#### Codice Azienda
Il campo **Codice Azienda** è il codice assegnato dall'associazione dell'ABI all'azienda che vuole presentare in formato elettronico i propri incassi e pagamenti.

### Pannello Bonifici SEPA

#### Impostazione SEPA
Nel pannello **Bonifici SEPA** è possibile indicare l'impostazione SEPA di default.

#### Metodo di pagamento
Nel pannello **Bonifici SEPA** è possibile indicare il metodo di pagamento di default.

#### Priorità
Nel pannello **Bonifici SEPA** è possibile indicare la priorità di default.

#### Addebito cumulativo
Nel pannello **Bonifici SEPA** è possibile indicare l'eventuale impostazione di **addebito cumulativo** di default.

### Pannello SEPA Direct Debit

#### Identificativo del soggetto privato
Nel pannello **SEPA Direct Debit** può essere indicato di default l'identificativo del soggetto privato per gli incassi SDD.

## Regole
### Funzione della tabella
La tabella **Banche Azienda** contiene tutte le banche dell'azienda.

### Moduli che utilizzano la tabella
La tabella **Banche Azienda** viene utilizzata sia dal modulo **Pagamento Fornitori** sia dal modulo **Portafoglio Effetti**.

### Calcolo automatico dell'IBAN
L'IBAN viene calcolato automaticamente in base ai valori inseriti nei campi **CIN**, **ABI**, **CAB** e **Conto Corrente**.

### Utilizzo del Codice Conto
Il **Codice Conto** viene utilizzato nel caso di tipo incasso impostato a **RID** nella tabella **tipi pagamento fornitori**.

### Utilizzo del Conto Bonifici
Il **Conto Bonifici** identifica il conto contabile da addebitare in fase di contabilizzazione del pagamento.

### Utilizzo del Conto Assegni
Il **Conto Assegni** identifica il conto contabile da addebitare in fase di contabilizzazione dei pagamenti quando il tipo pagamento fornitore è di tipo assegno.

### Gestione del Tipo Assegno
Con **Tipo Assegno = per fornitore** viene emesso un solo assegno per tutte le partite del fornitore incluse nel pagamento.

Con **Tipo Assegno = per partita** viene emesso un assegno per ciascuna partita.

### Impostazioni SEPA di default
Nel pannello **Bonifici SEPA** possono essere definite le impostazioni di default per i bonifici in formato SEPA.

### Impostazioni SDD di default
Nel pannello **SEPA Direct Debit** può essere definito di default l'identificativo del soggetto privato per gli incassi SDD.