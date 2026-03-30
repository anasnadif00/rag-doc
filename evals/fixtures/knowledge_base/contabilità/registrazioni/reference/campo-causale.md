---
title: Campo causale prima nota
doc_kind: reference
domain: contabilità
feature: registrazioni
keywords: [causale, campo causale, prima nota, registrazione]
task_tags: [configurazione campi, controllo dati]
erp_versions: [v1.0]
role_scope: [amministrazione, contabilità]
review_status: approved
module: Contabilità
submenu: Registrazioni
screen_id: PN-001
screen_title: Prima nota
tab_name: Testata
aliases: [causale prima nota]
---

# Campo causale prima nota

## Campi

### Causale

**Tipo:** Stringa
**Descrizione:** Indica il motivo della registrazione e guida i controlli contabili collegati.
**Obbligatorio:** Si per le registrazioni manuali.

### Data registrazione

**Tipo:** Data
**Descrizione:** Identifica la data competenza della registrazione contabile.

## Regole

### Causale obbligatoria

**Condizione:** La registrazione è inserita manualmente.
**Validazione:** Il campo Causale deve essere valorizzato prima del salvataggio.

### Coerenza causale e conto

**Condizione:** La causale attiva controlli specifici.
**Validazione:** La combinazione tra causale e conto deve rispettare le regole di contabilizzazione configurate.
