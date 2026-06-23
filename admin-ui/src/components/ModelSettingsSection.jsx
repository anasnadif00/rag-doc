import { PrimaryButton, SectionCard, SelectField } from './ui.jsx'

function ModelSettingsSection({
  modelSettings,
  modelForm,
  setModelForm,
  loading,
  busyAction,
  onSubmit,
}) {
  const options = modelSettings?.available_models || []

  return (
    <SectionCard
      eyebrow="Configurazione AI"
      title="Modelli OpenAI"
      subtitle="Scegli i modelli usati dal reranking semantico dei chunk e dalla generazione della risposta. Le modifiche valgono per tutte le aziende."
    >
      {loading || !modelForm ? (
        <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-5 py-6 text-sm text-stone-400">
          Caricamento della configurazione dei modelli...
        </div>
      ) : (
        <form className="grid gap-5 lg:grid-cols-[1fr_1fr_auto] lg:items-end" onSubmit={onSubmit}>
          <SelectField
            label="Modello reranking chunk"
            value={modelForm.rerankModel}
            options={options}
            onChange={(value) => setModelForm((current) => ({ ...current, rerankModel: value }))}
            help="Valuta e riordina i chunk recuperati prima che venga generata la risposta."
            disabled={busyAction === 'save-model-settings'}
          />
          <SelectField
            label="Modello generazione risposta"
            value={modelForm.generationModel}
            options={options}
            onChange={(value) => setModelForm((current) => ({ ...current, generationModel: value }))}
            help="Genera la risposta finale usando i chunk selezionati dal reranking."
            disabled={busyAction === 'save-model-settings'}
          />
          <PrimaryButton type="submit" disabled={busyAction === 'save-model-settings'}>
            {busyAction === 'save-model-settings' ? 'Salvataggio...' : 'Salva modelli'}
          </PrimaryButton>
        </form>
      )}
    </SectionCard>
  )
}

export default ModelSettingsSection
