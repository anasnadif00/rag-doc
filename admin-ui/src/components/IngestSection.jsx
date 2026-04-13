import { MetricMini, PrimaryButton, SectionCard, TextField, ToggleField } from './ui.jsx'

function IngestSection({ ingestForm, setIngestForm, onSubmit, busyAction, ingestResult }) {
  return (
    <SectionCard
      eyebrow="Contenuti"
      title="Aggiorna contenuti"
      subtitle="Usa questa sezione per ricaricare i materiali, limitare l'operazione a un gruppo specifico o aggiornare la ricerca."
    >
      <form className="space-y-4" onSubmit={onSubmit}>
        <div className="grid gap-4 md:grid-cols-2">
          <TextField
            label="Numero massimo"
            value={ingestForm.limit}
            placeholder="500"
            onChange={(value) => setIngestForm((current) => ({ ...current, limit: value }))}
            help="Lascia vuoto per elaborare tutto."
          />
          <TextField
            label="Versione ERP"
            value={ingestForm.erpVersion}
            placeholder="v1.0"
            onChange={(value) => setIngestForm((current) => ({ ...current, erpVersion: value }))}
          />
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <TextField
            label="Tipi di documento"
            value={ingestForm.docTypes}
            placeholder="how_to, reference, troubleshooting"
            onChange={(value) => setIngestForm((current) => ({ ...current, docTypes: value }))}
            help="Separali con una virgola o con una nuova riga."
          />
          <TextField
            label="Stati di revisione"
            value={ingestForm.reviewStatuses}
            placeholder="approved"
            onChange={(value) => setIngestForm((current) => ({ ...current, reviewStatuses: value }))}
          />
        </div>
        <div className="grid gap-3 sm:grid-cols-3">
          <ToggleField
            label="Ricrea archivio"
            checked={ingestForm.recreateCollection}
            onChange={(checked) => setIngestForm((current) => ({ ...current, recreateCollection: checked }))}
          />
          <ToggleField
            label="Controllo rigoroso"
            checked={ingestForm.strictValidation}
            onChange={(checked) => setIngestForm((current) => ({ ...current, strictValidation: checked }))}
          />
          <ToggleField
            label="Aggiorna indice di ricerca"
            checked={ingestForm.rebuildLexicalIndex}
            onChange={(checked) => setIngestForm((current) => ({ ...current, rebuildLexicalIndex: checked }))}
          />
        </div>
        <PrimaryButton type="submit" disabled={busyAction === 'run-ingest'}>
          {busyAction === 'run-ingest' ? 'Aggiornamento in corso...' : 'Avvia aggiornamento'}
        </PrimaryButton>
      </form>

      {ingestResult ? (
        <div className="mt-5 grid gap-3 rounded-2xl border border-white/10 bg-black/20 p-4 md:grid-cols-2">
          <MetricMini label="Stato" value={ingestResult.status} />
          <MetricMini label="Archivio" value={ingestResult.collection_name} />
          <MetricMini label="Documenti elaborati" value={String(ingestResult.documents_processed)} />
          <MetricMini label="Sezioni create" value={String(ingestResult.chunks_created)} />
        </div>
      ) : null}
    </SectionCard>
  )
}

export default IngestSection
