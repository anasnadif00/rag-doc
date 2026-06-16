---
title: Pannello Dettaglio di testata della Contabilità Generale
doc_kind: reference
domain: contabilita
feature: contabilita-generale
keywords:
  - contabilità generale
  - pannello dettaglio testata
  - data registrazione
  - numero registrazione
  - tipo documento
  - competenza IVA
  - protocollo
  - registro
  - competenza plafond
  - data operazione
  - ID SDI
  - data SDI
task_tags:
  - riferimento campi testata contabilità generale
  - gestione estremi registrazione
erp_versions:
  - v.1.0
role_scope:
  - accounting
review_status: approved
module: Contabilità generale
screen_title: Contabilità Generale
tab_name: Dettaglio
field_labels:
  - Data registrazione
  - Numero registrazione
  - Operatore
  - Tipo documento
  - Numero documento
  - Data documento
  - Competenza IVA
  - Registro
  - Protocollo
  - Competenza Plafond
  - Competenza IVA presunta
  - Data operazione
  - ID SDI
  - Data SDI
---
# Pannello Dettaglio di testata della Contabilità Generale

Il pannello Dettaglio di testata contiene i dati che rappresentano gli estremi della registrazione contabile.

## Campi
### Data registrazione
Assieme al Numero registrazione identifica univocamente l'operazione contabile, sia per rintracciarla nella gestione movimenti sia nelle stampe contabili.

È utilizzabile qualsiasi data all'interno del periodo in linea definito nella tabella Società.

Il campo è modificabile solo se:
- non è stato ancora eseguito il consolidamento dei movimenti
- per le registrazioni IVA non è ancora stato stampato in definitiva il relativo registro

### Numero registrazione
È il numero che identifica univocamente, assieme alla Data registrazione, l'operazione contabile.

Essendo un progressivo giornaliero, viene proposto in automatico in base alla data di registrazione, ma può essere modificato dall'operatore.

Se in tabella Versioni di contabilità è attivata l'opzione Utilizzo numeri di registrazione cancellati, vengono recuperati gli eventuali numeri liberi derivanti da registrazioni cancellate.

### Operatore
Viene proposto l'operatore corrispondente all'utente con cui si è entrati in Magia Cube.

Il campo non è modificabile.

### Tipo documento
Determina il tipo di operazione contabile che si intende inserire e definisce la configurazione della maschera in base ai parametri chiave attivati nella tabella Tipo documento.

Gli aspetti peculiari gestiti dal Tipo documento sono:
- Iva
- Partite
- Percipienti
- Dati COIN

Per la gestione IVA si distinguono registrazioni di:
- prima nota, senza gestione dell'IVA
- fatture attive e passive e relative note di credito
- corrispettivi

Per la gestione Partite, insieme ai dati strettamente contabili viene richiesta anche l'imputazione o la creazione delle scadenze collegate.

Per la gestione Percipienti si attivano compensi, ritenute e contributi per le parcelle ricevute.

Per la gestione Dati COIN viene regolata l'attivazione e la gestione dei dati di contabilità industriale.

### Numero documento
È obbligatorio per i documenti di tipo IVA.

Il campo è modificabile fino a quando non ci sono partite collegate al movimento.

### Data documento
È obbligatoria per i documenti di tipo IVA.

Il campo è modificabile fino a quando non ci sono partite collegate al movimento.

### Competenza IVA
Si attiva per le registrazioni che hanno i parametri IVA attivati in tabella Tipo documento, con esclusione:
- del parametro Fattura IVA Proforma
- dei tipi documento che hanno attivato il parametro IVA a esigibilità differita

Per i documenti di vendita viene proposta uguale al mese del documento.

Per i documenti di acquisto:
- se in tabella Versioni di contabilità è impostata la competenza su Data registrazione, la data di competenza viene proposta uguale alla Data registrazione
- se in tabella Versioni di contabilità è impostata la competenza su Data documento, la data di competenza IVA viene proposta pari alla Data documento se la registrazione avviene entro il 15 del mese successivo, altrimenti pari alla Data registrazione

Per le fatture a cavallo dell'anno la competenza IVA viene impostata sempre pari alla Data registrazione.

Il campo è modificabile dall'utente.

Nel caso di documenti con IVA ad esigibilità differita, il campo non viene valorizzato nemmeno dopo il relativo incasso o pagamento della partita, perché in presenza di chiusure rateali si possono avere competenze diverse in base alla data registrazione. In questo caso la data di competenza viene associata alla partita.

### Registro
Si attiva per i documenti che hanno i parametri IVA attivati in tabella Tipo documento, tranne che per l'IVA proforma.

### Protocollo
Si attiva per i tipi documento che hanno impostato il parametro tipo IVA a Acquisti in tabella Tipo documento.

Viene proposto in automatico in base alla data della registrazione.

Può essere modificato dall'utente, ma sempre nel rispetto della sequenzialità della numerazione.

Se il protocollo non è in sequenza, viene dato un messaggio che può essere:
- solo di avviso
- bloccante

Il comportamento del messaggio dipende da quanto impostato nella tabella Errori di contabilità.

La sequenzialità può essere controllata:
- solo sulla data, tramite l'errore Protocollo non in sequenza su data
- per data e numero di registrazione, tramite l'errore Protocollo non in sequenza

### Competenza Plafond
Si attiva in caso di utilizzo di tipi documento o modalità IVA presenti nella tabella Parametri calcolo PLAFOND.

Viene proposta in automatico in base alla versione del parametro Plafond sulla data nella tabella Versioni di contabilità.

Il campo è modificabile dall'utente.

### Competenza IVA presunta
Si attiva per le registrazioni il cui Tipo documento ha attivato il parametro IVA ad esigibilità differita.

Indica la competenza IVA massima che può assumere la fattura nel caso in cui non venga incassata o pagata entro il limite di un anno disposto dalla legge.

La competenza viene proposta:
- uguale alla Data documento se la fattura è inserita direttamente in Contabilità Generale
- in base alla data del documento di trasporto se la fattura proviene dal Controllo fatture
- in base alla data di inizio trasporto del DDT se la fattura proviene dalla Fatturazione
- in base alla Data fattura se le fatture sono inserite da Fatturazione o Controllo fatture senza ripresa dei documenti di trasporto

Il campo è modificabile dall'utente.

### Data operazione
Per le vendite è la data in cui è effettuata l'operazione.

### ID SDI
È l'ID numerico della fattura sul Sistema di Interscambio.

### Data SDI
È la data di ricezione del Sistema di Interscambio.

## Regole
### Identificazione univoca della registrazione
La registrazione è identificata univocamente dalla coppia:
- Data registrazione
- Numero registrazione

### Modificabilità degli estremi IVA
Numero documento e Data documento possono essere modificati solo fino a quando non esistono partite collegate al movimento.

### Effetto del Tipo documento
Il Tipo documento determina sia la configurazione grafica della maschera sia i dati richiesti in registrazione.

### Gestione della competenza IVA differita
Per i documenti con IVA ad esigibilità differita la competenza IVA non viene gestita sul movimento, ma sulla partita.