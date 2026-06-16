---
title: Inserire DDT da ripresa ordini
doc_kind: how_to
domain: vendite
feature: ddt-documenti-trasporto
keywords:
  - inserire DDT
  - ripresa ordini
  - creare DDT da ordine
  - bolla da ordine
  - riprendi ordini
task_tags:
  - creazione DDT da ordine
erp_versions:
  - v.1.0
role_scope:
  - commerciale
  - magazzino
  - amministrazione vendite
review_status: approved
module: DDT documenti di trasporto
screen_title: DDT documenti di trasporto
tab_name: Testata
aliases:
  - bolla da ordine
  - documento di trasporto da ordine
field_labels:
  - Tipo
  - Magazzino
  - Causale
  - Cliente
  - Riprendi ordini
---
# Inserire DDT da ripresa ordini

## Prerequisiti
Verificare che il tipo DDT utilizzato consenta la gestione del DDT da ordine.

Prima di avviare la ripresa ordini devono essere impostati almeno:

- Tipo;
- Magazzino;
- Causale.

La causale deve essere valida per area commerciale con il relativo flag attivato e deve avere impostato tipo causale di scarico.

## Procedura

1. Aprire il modulo DDT documenti di trasporto.
2. Premere il tasto "+" verde nella sezione di sinistra per avviare l'inserimento di un nuovo DDT.
3. Compilare il campo Tipo con la tipologia di documento di trasporto da utilizzare.
4. Verificare o lasciare proporre il Numero del DDT.
5. Verificare o modificare la Data DDT.
6. Compilare il campo Magazzino con il magazzino da cui verrà prelevato il materiale.
7. Compilare il campo Causale con una causale di magazzino di scarico valida per commerciale.
8. Compilare o verificare il Cliente, se richiesto dal flusso operativo.
9. Se necessario, verificare la Divisa proposta dall'anagrafica del cliente.
10. Se necessario, compilare Nostro riferimento e Vostro riferimento.
11. Cliccare l'icona a forma di cartellina per avviare la funzione di ripresa ordini.
12. Nella sezione di sinistra della videata di ripresa ordini, impostare i filtri necessari per individuare gli ordini da riprendere.
13. Verificare gli ordini estratti nella parte destra della videata.
14. Selezionare tutte le righe ordine da riprendere oppure solo alcune righe.
15. Se necessario, modificare le quantità delle righe da riprendere.
16. Lasciare attiva l'opzione Ricalcola se si vuole ricalcolare automaticamente pesi, colli, altre unità di misura, prezzo e vendita.
17. Proseguire con la freccia verde nella parte sottostante.
18. Nella videata di conferma, verificare i dati di testata degli ordini selezionati e i dettagli riportati sotto.
19. Se i dati sono corretti, cliccare Riprendi ordini.
20. Verificare che le righe degli ordini selezionati siano state riportate nel dettaglio del DDT.
21. Integrare, mantenere o modificare le informazioni riprese dagli ordini in base alla necessità.
22. Salvare il DDT.

## Verifiche finali
Controllare che il DDT riporti correttamente:

- le righe ordine selezionate;
- le quantità da spedire;
- il cliente di fatturazione;
- la divisa;
- gli agenti;
- gli sconti finali;
- eventuali condizioni di pagamento;
- eventuali note trasformate in righe di corpo.

Verificare inoltre che nella parte sottostante della ripresa ordini non siano presenti errori bloccanti.