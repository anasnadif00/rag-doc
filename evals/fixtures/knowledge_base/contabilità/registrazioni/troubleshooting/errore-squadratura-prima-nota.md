---
title: Errore squadratura prima nota
doc_kind: troubleshooting
domain: contabilità
feature: registrazioni
keywords: [squadratura, prima nota, pn-sq-001, dare e avere]
task_tags: [risoluzione errore, controllo quadratura]
erp_versions: [v1.0]
role_scope: [amministrazione, contabilità]
review_status: approved
module: Contabilità
submenu: Registrazioni
screen_id: PN-001
screen_title: Prima nota
tab_name: Movimenti
error_codes: [PN-SQ-001]
aliases: [errore squadratura prima nota]
---

# Errore squadratura prima nota

## Sintomo

Durante il salvataggio compare il messaggio **PN-SQ-001** e la registrazione non viene confermata.

## Cause probabili

- Il totale in dare non coincide con il totale in avere
- Un movimento è stato inserito con segno errato
- È stata modificata la causale senza aggiornare i movimenti

## Risoluzione

1. Apri il tab Movimenti della prima nota.
2. Ricontrolla gli importi in dare e in avere.
3. Correggi il movimento con importo o segno errato.
4. Salva di nuovo solo dopo che la registrazione risulta quadrata.

## Quando escalare

Se la registrazione risulta quadrata ma l'errore PN-SQ-001 persiste, raccogli i dettagli della causale e segnala il caso al supporto applicativo.
