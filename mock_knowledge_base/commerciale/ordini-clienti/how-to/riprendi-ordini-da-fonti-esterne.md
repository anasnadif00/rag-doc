---
title: Riprendi ordini da fonti esterne
doc_kind: how_to
domain: commerciale
feature: ordini-clienti
keywords:
  - ripresa da fonti esterne
  - acquisizione ordini
  - import ordini
  - file xml
  - file csv
  - tipologie acquisizione
  - sorgente
  - rigenerativa
  - tp esito
task_tags:
  - importazione ordini da file
  - acquisizione ordini esterni
erp_versions:
  - v.1.0
role_scope:
  - sales
review_status: approved
module: Ordini Clienti
submenu: Elaborazioni
screen_title: Ripresa da fonti esterne
aliases:
  - acquisizione ordini da file
  - ripresa ordini esterni
field_labels:
  - Società
  - Divisione
  - Tipo di tracciato
  - Tipologia
  - Sorgente
  - Rigenerativa
  - XML
  - Data
  - Tp esito
---
# Riprendi ordini da fonti esterne

## Prerequisiti
Verifica che il file da importare sia disponibile e rispetti un tracciato riconoscibile da Magia, definito in modo predefinito dal sistema.

## Procedura
1. Apri l'elaborazione **Ripresa da fonti esterne** dal modulo **Ordini Clienti**.
2. Controlla i valori di **Società** e **Divisione** proposti automaticamente in apertura della schermata. Se necessario, modificali.
3. Clicca sul **più verde** per inserire una nuova riga di ripresa.
4. Compila i dati richiesti per l'acquisizione:
   5. **Tipo di tracciato**, per indicare il tipo di ripresa che si vuole eseguire.
   6. **Tipologia**, che definisce le logiche di verifica dell'obbligatorietà dei campi e l'eventuale procedura di pretrattamento del file; il valore deriva dalla tabella **tipologie acquisizione**.
   7. **Sorgente**, cioè il file da importare. Con il **tasto destro** è possibile raggiungere la cartella da cui selezionare il file.
   8. Flag **Rigenerativa**, da attivare se devono essere cancellati eventuali dati acquisiti in precedenza da un file identico o con le stesse chiavi.
   9. Flag **XML**, da attivare per indicare il formato del file, distinguendo tra **XML** e **CSV**.
   10. **Data**, cioè la data in cui viene lanciata l'elaborazione.
11. Dopo aver completato la riga, clicca sull'icona in alto con la **freccina verde** per avviare l'elaborazione.
12. Attendi il termine dell'acquisizione e consulta il campo **Tp esito**.

## Verifiche finali
Verifica che:
1. L'acquisizione del file sia stata eseguita.
2. Nel campo **Tp esito** sia riportato il resoconto dell'importazione.
3. Eventuali errori riscontrati durante l'acquisizione siano stati elencati nel resoconto.

## Note operative
Questa elaborazione consente di acquisire uno o più ordini Magia da file esterni al gestionale. La correttezza del tracciato sorgente è fondamentale per il buon esito dell'importazione.