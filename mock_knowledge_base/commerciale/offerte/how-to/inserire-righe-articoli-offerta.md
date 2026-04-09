---
title: Inserire righe articoli in un'offerta
doc_kind: how_to
domain: commerciale
feature: offerte
keywords:
  - offerta
  - righe offerta
  - inserimento articoli
  - paragrafo
  - paragrafo base
  - paragrafo alternativa
  - codice articolo
  - descrizione articolo
  - quantità prezzo
  - quantità gestionale
  - data consegna
task_tags:
  - inserimento righe offerta
  - compilazione dettaglio offerta
  - gestione paragrafi offerta
erp_versions:
  - v.1.0
role_scope:
  - commerciale
review_status: approved
module: Offerte
screen_title: Offerte
field_labels:
  - Numero riga
  - Codice articolo
  - Descrizione
  - Tipo paragrafo
  - Quantità vendita
  - Quantità prezzo
  - Quantità gestionale
  - Colli
  - Prezzo
  - Omaggi
  - Data concordata
  - Tassativa
  - Data consegna
---
# Inserire righe articoli in un'offerta

## Prerequisiti
Verifica che la testata dell'offerta sia già stata caricata.

Verifica che gli articoli da inserire siano presenti nell'anagrafica di magazzino, se si intendono usare articoli codificati.

## Procedura
1. Dopo aver compilato la testata dell'offerta, posizionati nell'area centrale della videata, sotto la testata, dedicata al dettaglio delle righe.

2. Clicca sull'icona del più verde per aggiungere la prima riga.

3. Inserisci come prima riga un paragrafo  che viene proposto automaticamente. Il paragrafo è un insieme degli articoli che verranno poi riproposti in stampa e rappresenta un capitolo dell'offerta. Viene proposto un articolo codificato appositamente

4. Verifica il progressivo proposto per il paragrafo. Il sistema propone normalmente il valore 10 e prosegue per multipli di dieci. Il progressivo può comunque essere modificato dall'utente.

5. Seleziona il tipo di paragrafo dalla tendina:
   6. **Base** se il paragrafo deve concorrere al totale dell'offerta.
   7. **Alternativa** se il paragrafo rappresenta una proposta alternativa e non deve essere considerato nel totale dell'offerta.

8. Usa nuovamente l'icona del più verde per aggiungere le righe articolo appartenenti al paragrafo.

9. Verifica il **Numero riga** proposto dal sistema. Anche questo progressivo viene assegnato automaticamente ma può essere modificato dall'utente.

10. Posizionati sul campo **Codice articolo** e inserisci l'articolo:
   11. digitando direttamente il codice, se conosciuto;
   12. digitando una parte del codice;
   13. digitando una parte della descrizione.
   In tutti i casi il programma ricerca quanto presente nell'anagrafica articoli e propone i risultati selezionabili con il tasto destro del mouse.

14. Se il codice è già noto, digita il codice e conferma con Tab. L'articolo viene richiamato automaticamente e vengono ripresi tutti i dati inseriti nell'anagrafica articoli.

15. Valuta se usare un articolo codificato di magazzino oppure un articolo generico:
    1. per un articolo codificato, il programma riporta automaticamente codice e descrizione, dati inseriti in anagrafica articolo;
    2. per un articolo generico, la descrizione resta modificabile;
    3. per un articolo codificato da magazzino, la descrizione non è modificabile.

16. Seleziona il tipo di evasione scegliendo tra **Valore** e **Quantità**. Questo dato indica la modalità con cui si intende evadere la riga in eventuali passaggi successivi, ad esempio ordine o DDT.

17. Compila le quantità della riga considerando i diversi significati:
    1. **Quantità vendita**: non obbligatoria;
    2. **Quantità prezzo**: è la quantità che verrà moltiplicata per il prezzo;
    3. **Quantità gestionale**: è obbligatoria solo se viene inserita la quantità del prezzo, viene proposta dall'anagrafica articolo e non è modificabile. 
    Se in anagrafica non sono state specificate quantità vendita e quantità prezzo, il programma le propone normalmente uguali alla quantità gestionale. 
18. All'inserimento o modifica della quantità gestionale viene calcolata o proposta la quantità prezzo se non già presente. All'inserimento o modifica della quantità di vendita viene calcolata o proposta la quantità gestionale.

19. All'inserimento o modifica dei colli viene calcolata e proposta la quantità gestionale nel caso in cui non sia già presente e nel caso siano compilati i Dati Tecnici in anagrafica articolo.
20. Verifica il campo **Prezzo**:
    1. se esistono listini, il prezzo viene normalmente proposto in automatico;
    2. se non esistono listini, il prezzo può essere inserito manualmente.

21. Compila il campo **Omaggi** se occorre indicare quantità omaggio aggiuntive rispetto alla quantità principale della riga. Se valorizzata la quantità omaggi verrà sommata alla quantità venduta.

22. Inserisci la **Data concordata** se si vuole memorizzare una data di consegna concordata con il cliente. Questo dato ha normalmente un uso interno.

23. Attiva il flag **Tassativa** solo se la data concordata deve essere considerata vincolante.

24. Compila la **Data consegna**. Questo dato è obbligatorio per poter confermare la riga e procedere alla conferma dell'offerta.

25. Se necessario, completa i dati nei tab della riga: **Dati aggiuntivi**, **Dati di analitica**, **Agenti**, **Pagamenti**, **Sconti** e **Note**.

## Verifiche finali
Verifica che ogni riga articolo sia associata al paragrafo corretto.

Verifica che i paragrafi di tipo **Base** concorrano al totale e che quelli di tipo **Alternativa** non vengano sommati.

Verifica che la **Data consegna** sia compilata su tutte le righe che devono essere confermate.

Verifica che prezzo, quantità e eventuali dati aggiuntivi siano coerenti con quanto atteso in stampa e nei documenti successivi.