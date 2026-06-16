---
title: Stampare il portafoglio a quantità
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - portafoglio a quantità
  - stampa portafoglio ordini
  - ordini clienti a quantità
  - quantità residua ordini
  - portafoglio ordini clienti
  - export excel ordini
task_tags:
  - stampa portafoglio ordini
  - controllo quantità residue
  - analisi ordini clienti
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - backoffice
review_status: approved
module: Ordini clienti
submenu: Stampe ordini
screen_title: Portafoglio a quantità
aliases:
  - portafoglio ordini a quantità
  - portafoglio ordini clienti
field_labels:
  - da data a data
  - da numero a numero
  - categorie merceologiche
  - cliente
  - agente
  - categorie amministrative o commerciali
  - tipo di ordine
  - zona
  - commessa
  - nazioni
  - ordinamento
---
# Stampare il portafoglio a quantità

## Prerequisiti
Verificare i criteri con cui devono essere selezionati gli ordini da includere nella stampa.

Se necessario, verificare se deve essere utilizzato un formato standard oppure un formato personalizzato richiesto dal cliente.

## Procedura
1. Aprire la stampa **Portafoglio a quantità** tra le stampe disponibili del modulo **Ordini clienti**.

2. Impostare i filtri di selezione in base agli ordini da estrarre. I filtri disponibili comprendono:
   - **da data a data**;
   - **da numero a numero**;
   - **categoria merceologica**;
   - **cliente**;
   - **agente**;
   - **categorie amministrative e/o commerciali**;
   - **tipo di ordine**;
   - **zona**;
   - **commessa**, se viene utilizzata;
   - **nazioni**.

3. Nel campo **nazioni**, scegliere se:
   - includere **tutte** le nazioni;
   - estrarre solo gli ordini **Italia**;
   - estrarre solo gli ordini **estero**.

1. Impostare il campo **ordinamento** per ottenere la stampa con l'ordine desiderato, si può scegliere ordinamento per Cliente, Ragione Sociale, Ordine, Articolo.

2. Selezionare il formato di stampa da utilizzare. La stampa è disponibile nei formati standard e, se previsti, anche nei formati personalizzati.

3. Eseguire l'output desiderato:
   - aprire la stampa;
   - stampare il documento;
   - esportare in **Excel** per eseguire eventuali ulteriori combinazioni sul foglio.

## Verifiche finali
Verificare che gli ordini riportati nella stampa siano coerenti con i filtri impostati.

Controllare che l'ordinamento visualizzato corrisponda al valore selezionato nel campo **ordinamento**.

Se è stato prodotto un file Excel, verificare che i dati esportati siano completi e riutilizzabili per le elaborazioni successive.

## Regole di selezione per nazione
Se nel filtro **nazioni** si seleziona **Italia**, vengono estratti:
- gli ordini dei clienti che non hanno la nazione impostata in anagrafica;
- gli ordini dei clienti che hanno in anagrafica una nazione con codice ISO uguale a quello indicato nella tabella **Società** come **codice ISO nazione**.

Se nel filtro **nazioni** si seleziona **estero**, vengono estratti gli ordini dei clienti che hanno in anagrafica una qualsiasi nazione diversa da quella il cui codice ISO è indicato nella tabella **Società** come **codice ISO nazione**.

## Contenuto della stampa
La stampa **Portafoglio a quantità** riporta le seguenti informazioni:
- estremi dell'ordine;
- cliente;
- nazione;
- zona;
- agente;
- stato dell'ordine;
- per ogni riga, **quantità ordinata**;
- **quantità consegnata**;
- **quantità evasa forzatamente**;
- **quantità residua**.

Questi dati consentono di controllare le quantità residue ancora da evadere sugli ordini clienti.