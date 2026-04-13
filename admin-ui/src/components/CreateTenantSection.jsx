import { PrimaryButton, SectionCard, TextArea, TextField, ToggleField } from './ui.jsx'

function CreateTenantSection({ createForm, setCreateForm, onSubmit, busyAction }) {
  return (
    <SectionCard
      eyebrow="Nuova azienda"
      title="Crea una nuova azienda"
      subtitle="Inserisci i dati principali, attiva il servizio e definisci i limiti in un solo passaggio."
    >
      <form className="space-y-4" onSubmit={onSubmit}>
        <div className="grid gap-4 md:grid-cols-2">
          <TextField
            label="Codice azienda"
            value={createForm.tenantCode}
            placeholder="acme-erp"
            onChange={(value) => setCreateForm((current) => ({ ...current, tenantCode: value }))}
          />
          <TextField
            label="Nome visualizzato"
            value={createForm.displayName}
            placeholder="Acme ERP"
            onChange={(value) => setCreateForm((current) => ({ ...current, displayName: value }))}
          />
        </div>
        <TextField
          label="Codice di collegamento"
          value={createForm.issuer}
          placeholder="https://idp.acme.example"
          onChange={(value) => setCreateForm((current) => ({ ...current, issuer: value }))}
        />
        <div className="grid gap-4 md:grid-cols-2">
          <TextField
            label="Livello"
            value={createForm.licenseTier}
            placeholder="standard"
            onChange={(value) => setCreateForm((current) => ({ ...current, licenseTier: value }))}
          />
          <TextField
            label="Archivio dedicato"
            value={createForm.overlayCollection}
            placeholder="archivio_acme"
            onChange={(value) => setCreateForm((current) => ({ ...current, overlayCollection: value }))}
          />
        </div>
        <TextArea
          label="Indirizzi web autorizzati"
          value={createForm.allowedOrigins}
          placeholder="https://erp.acme.example&#10;http://localhost:3000"
          rows={3}
          onChange={(value) => setCreateForm((current) => ({ ...current, allowedOrigins: value }))}
          help="Inserisci un indirizzo per riga oppure separa con una virgola."
        />
        <div className="grid gap-4 md:grid-cols-2">
          <TextField
            label="Codice chiave"
            value={createForm.publicKeyKid}
            placeholder="acme-key-2026-01"
            onChange={(value) => setCreateForm((current) => ({ ...current, publicKeyKid: value }))}
          />
          <TextField
            label="Stato accesso"
            value={createForm.licenseStatus}
            placeholder="active"
            onChange={(value) => setCreateForm((current) => ({ ...current, licenseStatus: value }))}
          />
        </div>
        <TextArea
          label="Chiave pubblica iniziale"
          value={createForm.publicKeyPem}
          placeholder="-----BEGIN PUBLIC KEY-----"
          rows={5}
          onChange={(value) => setCreateForm((current) => ({ ...current, publicKeyPem: value }))}
        />
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          <TextField
            label="Messaggi al giorno"
            value={createForm.dailyMessageLimit}
            onChange={(value) => setCreateForm((current) => ({ ...current, dailyMessageLimit: value }))}
          />
          <TextField
            label="Token al giorno"
            value={createForm.dailyTokenLimit}
            onChange={(value) => setCreateForm((current) => ({ ...current, dailyTokenLimit: value }))}
          />
          <TextField
            label="Limite richieste rapide"
            value={createForm.burstRpsLimit}
            onChange={(value) => setCreateForm((current) => ({ ...current, burstRpsLimit: value }))}
          />
          <TextField
            label="Sessioni contemporanee"
            value={createForm.concurrentSessionsLimit}
            onChange={(value) => setCreateForm((current) => ({ ...current, concurrentSessionsLimit: value }))}
          />
        </div>
        <div className="grid gap-3 sm:grid-cols-2">
          <ToggleField
            label="Archivio dedicato attivo"
            checked={createForm.overlayKbEnabled}
            onChange={(checked) => setCreateForm((current) => ({ ...current, overlayKbEnabled: checked }))}
          />
          <ToggleField
            label="Funzioni ERP attive"
            checked={createForm.erpToolsEnabled}
            onChange={(checked) => setCreateForm((current) => ({ ...current, erpToolsEnabled: checked }))}
          />
        </div>
        <PrimaryButton type="submit" disabled={busyAction === 'create-tenant'}>
          {busyAction === 'create-tenant' ? 'Creazione in corso...' : 'Crea azienda'}
        </PrimaryButton>
      </form>
    </SectionCard>
  )
}

export default CreateTenantSection
