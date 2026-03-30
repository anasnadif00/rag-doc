# Guida KB v2 per rag-doc

## Scopo

Questa knowledge base non deve essere scritta come un manuale generico. Deve funzionare bene per retrieval, citazioni e chunking automatico. Questo significa che ogni file deve avere metadata coerenti, un argomento chiaro e headings prevedibili. Se il contenuto e' troppo misto o troppo vago, il sistema recupera chunk peggiori e l'AI risponde con meno precisione.

## Regola principale

- Un file deve coprire un solo argomento atomico: una procedura, un problema, oppure un riferimento specifico.
- Se cambiano in modo sostanziale schermata, tab, ruolo o versione ERP, crea file separati.
- Se un contenuto contiene sia procedura sia troubleshooting, separalo in due file diversi.
- Preferisci file brevi e mirati invece di documenti lunghi con molti casi diversi.

## Dove mettere i file

Per tutti i nuovi contenuti usa solo questo layout:

```text
knowledge-base/<domain>/<feature>/<doc_kind>/<slug>.md
```

Esempio:

```text
knowledge-base/contabilita/fatture/how_to/crea-fattura.md
```

Regole:

- `slug` in lowercase kebab-case: `crea-fattura`, `errore-art-val-001`, `campi-testata-fattura`
- `domain`, `feature` e `doc_kind` nel front matter devono coincidere con il path
- Non creare nuovi file nei root legacy `manuals/` o `faqs/`

## Front matter

### Campi obbligatori

Questi campi devono esserci sempre:

- `title`: titolo del documento
- `doc_kind`: uno tra `how_to`, `troubleshooting`, `reference`, `faq`, `overview`
- `domain`: dominio funzionale, ad esempio `contabilita`
- `feature`: area specifica, ad esempio `fatture`
- `keywords`: termini che gli utenti potrebbero cercare
- `task_tags`: etichette di attivita o obiettivo
- `erp_versions`: versioni ERP a cui il contenuto si applica
- `role_scope`: ruoli a cui il contenuto si applica
- `review_status`: stato del contenuto

### Campi fortemente consigliati

Compilali quando sono noti, per migliorare ranking e filtri:

- `module`
- `submenu`
- `screen_id`
- `screen_title`
- `tab_name`
- `aliases`
- `field_labels`
- `error_codes`
- `source_uri`

### Come usare i campi piu utili

- `keywords`: termini ricercabili, concreti e vicini al linguaggio utente. Evita valori troppo generici come `gestione`, `documenti`, `operazioni`.
- `task_tags`: obiettivo operativo, ad esempio `creazione fattura`, `annullamento ordine`, `verifica disponibilita`.
- `aliases`: sinonimi o nomi alternativi realmente usati in azienda, senza inventarne di nuovi.
- `field_labels`: etichette esatte visibili in schermata, ad esempio `Cliente`, `Data documento`, `Codice articolo`.
- `error_codes`: codici errore esatti, ad esempio `ART-VAL-001`.
- `source_uri`: riferimento alla fonte originale, utile per audit e manutenzione.

### Review status

- `approved`: contenuto pronto per l'ingest standard
- `review`: bozza da verificare prima della pubblicazione

Per bozze generate da AI usa come default `review`.

## Quale doc_kind usare

- `how_to`: procedura passo-passo per completare un task
- `troubleshooting`: sintomo o errore con causa e risoluzione
- `reference`: campi, regole, vincoli, definizioni
- `faq`: Q/A brevi solo se non sono modellabili meglio come `troubleshooting` o `reference`
- `overview`: contesto generale o orientamento; non sostituisce una procedura

Per nuovi contenuti, usa soprattutto `how_to`, `troubleshooting` e `reference`.

## Struttura del corpo Markdown

### how_to

Struttura consigliata:

```md
# Titolo
## Prerequisiti
...
## Procedura
1. ...
2. ...
## Verifiche finali
...
```

Regole:

- `## Procedura` e' obbligatoria
- i passi devono essere numerati
- `## Prerequisiti` e `## Verifiche finali` sono opzionali

### troubleshooting

Struttura consigliata:

```md
# Titolo
## Sintomo
...
## Cause probabili
...
## Risoluzione
...
## Quando escalare
...
```

Regole:

- `## Sintomo` e `## Risoluzione` sono obbligatori
- `## Cause probabili` e `## Quando escalare` sono opzionali

### reference

Struttura consigliata:

```md
# Titolo
## Campi
### Campo 1
...
## Regole
### Regola 1
...
```

Regole:

- deve esserci almeno uno tra `## Campi` e `## Regole`
- se ci sono piu voci, usa `###` per separarle

## Regole di scrittura

- Usa i nomi ERP visibili all'utente, non sinonimi inventati.
- `title` nel front matter e `#` nel body devono coincidere.
- Nella `Procedura` usa passi numerati `1.` `2.` `3.`; non usare bullet list per i passi.
- Non duplicare headings principali come `## Procedura`, `## Sintomo`, `## Risoluzione` nello stesso file.
- Non nascondere informazioni critiche solo in immagini, screenshot o tabelle.
- Quando esiste un codice errore, riportalo sia nel testo sia in `error_codes`.
- Se una procedura cambia davvero per ruolo o versione, separa i file invece di spiegare troppe varianti nello stesso documento.

## Anti-pattern da evitare

- Un solo file con piu task distinti.
- Metadata mancanti o incoerenti con il path.
- `keywords` troppo generiche o troppo poche.
- Titolo del front matter diverso dal titolo `#`.
- Procedure scritte come paragrafo unico invece che come passi numerati.
- File che mescolano piu versioni ERP o piu ruoli quando il flusso cambia.

## Template pronti da copiare

### Template how_to

Percorso consigliato:

```text
knowledge-base/contabilita/fatture/how_to/crea-fattura.md
```

```md
---
title: Crea fattura
doc_kind: how_to
domain: contabilita
feature: fatture
keywords: [fattura, crea fattura, cliente]
task_tags: [creazione fattura]
erp_versions: [REL231]
role_scope: [accounting]
review_status: review
module: Contabilita
submenu: Fatture
screen_id: FAT-001
screen_title: Fatture
tab_name: Testata
aliases: [fatture clienti]
field_labels: [Cliente, Data documento]
source_uri: jira://ERP-123
---
# Crea fattura

## Prerequisiti
Verifica che il cliente sia gia presente in anagrafica.

## Procedura
1. Apri la schermata Fatture.
2. Vai nella tab Testata.
3. Compila i campi Cliente e Data documento.
4. Salva il documento.

## Verifiche finali
Controlla che il numero fattura sia stato assegnato e che il documento risulti registrato.
```

### Template troubleshooting

Percorso consigliato:

```text
knowledge-base/logistica/articoli/troubleshooting/errore-art-val-001.md
```

```md
---
title: Errore ART-VAL-001 in salvataggio articolo
doc_kind: troubleshooting
domain: logistica
feature: articoli
keywords: [ART-VAL-001, errore articolo, salvataggio articolo]
task_tags: [risoluzione errore articolo]
erp_versions: [REL231]
role_scope: [warehouse]
review_status: review
module: Logistica
submenu: Magazzino
screen_id: ART-001
screen_title: Articoli
tab_name: Anagrafica
field_labels: [Articolo, Descrizione]
error_codes: [ART-VAL-001]
source_uri: jira://ERP-456
---
# Errore ART-VAL-001 in salvataggio articolo

## Sintomo
Durante il salvataggio della schermata Articoli compare l'errore ART-VAL-001.

## Cause probabili
Il campo Articolo e' vuoto oppure contiene un valore non valido.

## Risoluzione
Compila il campo Articolo con un codice univoco, verifica la Descrizione e ripeti il salvataggio.

## Quando escalare
Escalare se l'errore compare anche con un codice articolo valido e non duplicato.
```

### Template reference

Percorso consigliato:

```text
knowledge-base/contabilita/fatture/reference/campi-testata-fattura.md
```

```md
---
title: Campi della testata Fatture
doc_kind: reference
domain: contabilita
feature: fatture
keywords: [campi fattura, testata fattura, cliente, data documento]
task_tags: [riferimento campi fattura]
erp_versions: [REL231]
role_scope: [accounting]
review_status: review
module: Contabilita
submenu: Fatture
screen_id: FAT-001
screen_title: Fatture
tab_name: Testata
field_labels: [Cliente, Data documento, Condizione pagamento]
source_uri: confluence://fatture/testata
---
# Campi della testata Fatture

## Campi
### Cliente
Identifica il cliente intestatario del documento. E' obbligatorio.

### Data documento
Definisce la data contabile del documento. E' obbligatoria.

### Condizione pagamento
Definisce le scadenze di pagamento applicate al documento.

## Regole
### Obbligatorieta minima
Per salvare una nuova fattura devono essere valorizzati almeno Cliente e Data documento.
```

## Checklist finale

- [ ] Il file e' nel path `knowledge-base/<domain>/<feature>/<doc_kind>/<slug>.md`
- [ ] `domain`, `feature` e `doc_kind` del front matter coincidono con il path
- [ ] Tutti i campi obbligatori del front matter sono presenti
- [ ] Il titolo nel front matter coincide con il titolo `#`
- [ ] I headings obbligatori del `doc_kind` scelto sono presenti
- [ ] Le etichette schermata e i nomi ERP sono esatti
- [ ] I codici errore esatti sono riportati, se esistono
- [ ] Il file e' abbastanza atomico da rispondere a una sola esigenza chiara
