---
title: Tabelle del modulo Offerte
doc_kind: reference
domain: commerciale
feature: offerte
keywords:
  - tabella motivo avanzamento
  - numerazione offerte di vendita
  - parametri offerte
  - probabilità di chiusura
  - stato avanzamento
  - stato offerta cliente
  - stato riga offerta di vendita
  - tipo offerte di vendita
task_tags:
  - riferimento tabelle offerte
  - configurazione offerte
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Offerte
submenu: Tabelle
screen_title: Gestione Tabelle modulo Offerte
aliases:
  - tabelle offerte
  - configurazioni offerte
field_labels:
  - Codice
  - Descrizione
  - Tipo Offerta
  - Tipo Numerazione
  - Flag articolo senza prezzo
  - Calcola disponibilità
  - Tab Stato Offerta
  - Tab Stato Riga
  - Tab Società/Divisione
---
# Tabelle del modulo Offerte

## Campi
### Tabella Motivo Avanzamento
Consente di inserire i motivi dell'avanzamento delle offerte, se si decide di utilizzarli.

Con il **+ verde** si aggiungono nuovi dati in tabella.

Campi:
- **Codice**: campo alfanumerico fino a 4 caratteri.
- **Descrizione**: descrizione del motivo che comparirà nelle offerte e nel **Portafoglio offerte**.

### Tabella Numerazione offerte di Vendita
È il contatore dei progressivi delle offerte assegnati in relazione al tipo di numerazione e all'anno.

### Tabella Parametri offerte
Consente di inserire il codice articolo fittizio da utilizzare per la riga del **Paragrafo**.

### Tabella Probabilità di chiusura
Consente di codificare una serie di descrizioni sulle probabilità di chiusura, a discrezione dell'utente.

Campi:
- **Codice numero**
- **Descrizione**

Il valore inserito nell'offerta può essere utilizzato anche come filtro nel **Portafoglio offerte**.

### Tabella Stato avanzamento
Consente di definire gli stati di avanzamento dell'offerta.

Campi:
- **Codice numero**
- **Descrizione**
- **Tipologia** da assegnare tra quelle proposte, in relazione all'andamento della trattativa e alla sua evasione.

### Tabella Stato Offerta cliente
Contiene la codifica degli stati dell'offerta predefiniti del programma. Non si possono modificare o aggiungere valori.

### Tabella Stato riga Offerta di vendita
Contiene la codifica predefinita degli stati riga dell'offerta. Non si possono modificare o aggiungere valori.

### Tipo Offerte di vendita
Consente di codificare le diverse tipologie di offerte utili per distinguere i documenti nelle classificazioni necessarie all'azienda.

Campi:
- **Tipo Offerta**: codice univoco alfanumerico di 3 caratteri.
- **Descrizione**: descrizione della tipologia.
- **Tipo Numerazione**: determina la numerazione da utilizzare per quel tipo di offerta.
- **Flag articolo senza prezzo**: se attivo, consente di inserire articoli senza indicare il prezzo.
- **Calcola disponibilità**: consente di considerare o meno le offerte nella procedura di calcolo della disponibilità.
- **Tab Stato Offerta**: consente di decidere, per ogni stato, se le offerte sono inseribili e/o modificabili.
- **Tab Stato Riga**: consente di decidere, per ogni stato riga, se le offerte sono inseribili e/o modificabili.
- **Tab Società/Divisione**: consente di impostare, per ogni tipo di offerta, società e divisione, il tipo di transazione e le destinazioni da gestire in COIN.

## Regole
### Tabella Stato Offerta cliente
Gli stati presenti sono di default del programma. Non sono modificabili e non è possibile inserire nuove tipologie.

### Tabella Stato riga Offerta di vendita
Gli stati riga presenti sono di default del programma. Non sono modificabili e non è possibile inserire nuove tipologie.

### Tipo Numerazione nelle Tipologie Offerta
Se il **Tipo Numerazione** è inserito, la numerazione delle offerte è progressiva e viene sempre proposta dal programma. Se non è inserito, la numerazione può essere assegnata manualmente dall'utente.

### Condivisione o separazione delle numerazioni
È possibile gestire tipologie di offerte diverse con la stessa numerazione oppure differenziarle, in base alla configurazione scelta dall'utente.