---
title: Prezzi nei Listini vendita
doc_kind: reference
domain: vendite
feature: listini-vendita
keywords:
  - prezzi listini vendita
  - quantità fissa
  - quantità a scaglioni
  - prezzo articolo
  - scaglioni prezzo
task_tags:
  - riferimento prezzi listini vendita
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - amministrazione vendite
review_status: approved
module: Listini vendita
screen_title: Listini vendita
tab_name: Prezzo
field_labels:
  - Quantità fissa
  - Quantità a scaglioni
  - Quantità
  - Importo
---
# Prezzi nei Listini vendita

## Campi

### Quantità fissa
Il flag Quantità fissa indica che il prezzo è riferito alla quantità indicata nel campo sottostante.

Se nel documento di vendita viene inserita una quantità diversa, il prezzo viene proporzionato alla quantità indicata nell'ordine, nel DDT o nella fattura.

Esempio: impostando Quantità fissa uguale a 1, il prezzo indicato viene applicato a una singola unità dell'articolo.

### Quantità a scaglioni
Il flag Quantità a scaglioni permette di applicare prezzi diversi in base a un range di quantità.

Se il flag è attivo, è possibile inserire più scaglioni di prezzo.

Il prezzo può cambiare in relazione alla quantità immessa in:
- ordine;
- DDT;
- fattura.

### Quantità
Nel caso di prezzo a scaglioni, la quantità indicata deve essere intesa come quantità fino a.

Normalmente l'ultimo scaglione viene inserito con una quantità molto elevata, oltre la quale si presume di non dover andare nel documento.

### Importo
Indica il valore del prezzo associato all'articolo e alla quantità prevista.

## Regole

### Applicazione del prezzo a quantità fissa
Quando il prezzo è a quantità fissa, il valore indicato viene riferito alla quantità impostata.

Se la quantità movimentata è diversa, il prezzo viene proporzionato.

### Applicazione del prezzo a scaglioni
Quando il prezzo è a scaglioni, il sistema determina lo scaglione in base alla quantità inserita nel documento commerciale.

Il prezzo applicato è quello relativo allo scaglione corrispondente.