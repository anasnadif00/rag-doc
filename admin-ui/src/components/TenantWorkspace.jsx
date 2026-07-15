import UsageChart from './UsageChart.jsx'
import {
  EmptyState,
  GhostButton,
  MetricMini,
  PrimaryButton,
  SectionCard,
  SectionHeading,
  TextArea,
  TextField,
  ToggleField,
} from './ui.jsx'
import { formatNumber } from '../lib/dashboard.js'

function TenantWorkspace({
  selectedTenant,
  editForm,
  setEditForm,
  licenseForm,
  setLicenseForm,
  keyForm,
  setKeyForm,
  usageDays,
  setUsageDays,
  usageRows,
  usageTotals,
  loadingUsage,
  busyAction,
  onSaveProfile,
  onSaveLicense,
  onRotateKey,
  onActivate,
  onSuspend,
}) {
  return (
    <SectionCard
      className="tenant-workspace-card"
      eyebrow="Dettaglio azienda"
      title={selectedTenant ? selectedTenant.display_name : 'Seleziona un\'azienda'}
      subtitle={
        selectedTenant
          ? `Codice azienda ${selectedTenant.tenant_code}`
          : 'Scegli un\'azienda dall\'elenco per modificare dati, limiti, chiavi e andamento del servizio.'
      }
      actions={
        selectedTenant ? (
          <div className="flex flex-wrap gap-2">
            <GhostButton
              type="button"
              disabled={busyAction === 'activate-tenant' || selectedTenant.status === 'active'}
              onClick={onActivate}
            >
              Attiva
            </GhostButton>
            <GhostButton
              type="button"
              disabled={busyAction === 'suspend-tenant' || selectedTenant.status === 'suspended'}
              onClick={onSuspend}
            >
              Sospendi
            </GhostButton>
          </div>
        ) : null
      }
    >
      {selectedTenant && editForm && licenseForm ? (
        <div className="space-y-5">
          <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
            <MetricMini label="Chiave attiva" value={selectedTenant.active_kid || 'Nessuna'} />
            <MetricMini label="Indirizzi autorizzati" value={String(selectedTenant.allowed_origins.length)} />
            <MetricMini label="Periodo analizzato" value={`${usageDays} giorni`} />
            <MetricMini label="Connessioni chat" value={formatNumber(usageTotals.wsConnects)} />
          </div>

          <div className="grid gap-4 xl:grid-cols-2">
            <form className="admin-subsection space-y-3" onSubmit={onSaveProfile}>
              <SectionHeading title="Dati azienda" subtitle="Informazioni principali, indirizzi autorizzati e archivio dedicato." />
              <div className="grid gap-3 sm:grid-cols-2">
                <TextField
                  label="Nome visualizzato"
                  value={editForm.displayName}
                  onChange={(value) => setEditForm((current) => ({ ...current, displayName: value }))}
                />
                <label className="block space-y-2">
                  <span className="text-xs uppercase tracking-[0.18em] text-muted">Stato</span>
                  <select
                    value={editForm.status}
                    onChange={(event) => setEditForm((current) => ({ ...current, status: event.target.value }))}
                    className="app-field w-full rounded-xl border px-3 py-2.5 text-[13px] outline-none transition"
                  >
                    <option value="active">Attiva</option>
                    <option value="suspended">Sospesa</option>
                    <option value="quota_exceeded">Limite raggiunto</option>
                  </select>
                </label>
              </div>
              <div className="grid gap-3 sm:grid-cols-2">
                <TextField
                  label="Livello"
                  value={editForm.licenseTier}
                  onChange={(value) => setEditForm((current) => ({ ...current, licenseTier: value }))}
                />
                <TextField
                  label="Archivio dedicato"
                  value={editForm.overlayCollection}
                  onChange={(value) => setEditForm((current) => ({ ...current, overlayCollection: value }))}
                />
              </div>
              <TextArea
                label="Indirizzi web autorizzati"
                rows={4}
                value={editForm.allowedOrigins}
                onChange={(value) => setEditForm((current) => ({ ...current, allowedOrigins: value }))}
              />
              <PrimaryButton type="submit" disabled={busyAction === 'save-tenant'}>
                {busyAction === 'save-tenant' ? 'Salvataggio in corso...' : 'Salva dati'}
              </PrimaryButton>
            </form>

            <form className="admin-subsection space-y-3" onSubmit={onSaveLicense}>
              <SectionHeading title="Limiti e funzioni" subtitle="Messaggi, accessi e disponibilita previsti per l'azienda selezionata." />
              <div className="grid gap-3 sm:grid-cols-2">
                <label className="block space-y-2">
                  <span className="text-xs uppercase tracking-[0.18em] text-muted">Stato servizio</span>
                  <select
                    value={licenseForm.status}
                    onChange={(event) => setLicenseForm((current) => ({ ...current, status: event.target.value }))}
                    className="app-field w-full rounded-xl border px-3 py-2.5 text-[13px] outline-none transition"
                  >
                    <option value="active">Attivo</option>
                    <option value="suspended">Sospeso</option>
                  </select>
                </label>
                <TextField
                  label="Messaggi al giorno"
                  value={licenseForm.dailyMessageLimit}
                  onChange={(value) => setLicenseForm((current) => ({ ...current, dailyMessageLimit: value }))}
                />
              </div>
              <div className="grid gap-3 sm:grid-cols-2">
                <TextField
                  label="Token al giorno"
                  value={licenseForm.dailyTokenLimit}
                  onChange={(value) => setLicenseForm((current) => ({ ...current, dailyTokenLimit: value }))}
                />
                <TextField
                  label="Limite richieste rapide"
                  value={licenseForm.burstRpsLimit}
                  onChange={(value) => setLicenseForm((current) => ({ ...current, burstRpsLimit: value }))}
                />
              </div>
              <TextField
                label="Sessioni contemporanee"
                value={licenseForm.concurrentSessionsLimit}
                onChange={(value) => setLicenseForm((current) => ({ ...current, concurrentSessionsLimit: value }))}
              />
              <div className="grid gap-3 sm:grid-cols-2">
                <ToggleField
                  label="Archivio dedicato attivo"
                  checked={licenseForm.overlayKbEnabled}
                  onChange={(checked) => setLicenseForm((current) => ({ ...current, overlayKbEnabled: checked }))}
                />
                <ToggleField
                  label="Funzioni ERP attive"
                  checked={licenseForm.erpToolsEnabled}
                  onChange={(checked) => setLicenseForm((current) => ({ ...current, erpToolsEnabled: checked }))}
                />
              </div>
              <PrimaryButton type="submit" disabled={busyAction === 'save-license'}>
                {busyAction === 'save-license' ? 'Salvataggio in corso...' : 'Salva limiti'}
              </PrimaryButton>
            </form>
          </div>

          <div className="grid gap-4 2xl:grid-cols-[minmax(0,1.35fr)_minmax(340px,0.65fr)]">
            <div className="admin-subsection">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <SectionHeading
                  title="Andamento utilizzo"
                  subtitle="Consulta il traffico recente per capire l'uso del servizio e prevenire blocchi."
                />
                <div className="flex items-center gap-2">
                  <label className="text-xs uppercase tracking-[0.18em] text-muted" htmlFor="usage-window">
                    Periodo
                  </label>
                  <select
                    id="usage-window"
                    value={usageDays}
                    onChange={(event) => setUsageDays(Number(event.target.value))}
                    className="app-field rounded-full border px-3 py-2 text-[13px] outline-none"
                  >
                    <option value={7}>7 giorni</option>
                    <option value={14}>14 giorni</option>
                    <option value={30}>30 giorni</option>
                  </select>
                </div>
              </div>
              <div className="mt-3 grid gap-3 sm:grid-cols-3">
                <MetricMini label="Messaggi" value={formatNumber(usageTotals.messages)} />
                <MetricMini label="Consumo richiesta" value={formatNumber(usageTotals.promptTokens)} />
                <MetricMini label="Consumo risposta" value={formatNumber(usageTotals.completionTokens)} />
              </div>
              <UsageChart rows={usageRows} loading={loadingUsage} />
            </div>

            <form className="admin-subsection space-y-3" onSubmit={onRotateKey}>
              <SectionHeading
                title="Aggiorna chiave di accesso"
                subtitle="Sostituisci la chiave attiva senza uscire dal pannello."
              />
              <div className="grid gap-3 sm:grid-cols-2">
                <TextField
                  label="Codice chiave"
                  value={keyForm.kid}
                  placeholder="acme-key-2026-02"
                  onChange={(value) => setKeyForm((current) => ({ ...current, kid: value }))}
                />
                <TextField
                  label="Algoritmo"
                  value={keyForm.algorithm}
                  placeholder="RS256"
                  onChange={(value) => setKeyForm((current) => ({ ...current, algorithm: value }))}
                />
              </div>
              <TextArea
                label="Chiave pubblica"
                rows={7}
                value={keyForm.publicKeyPem}
                placeholder="-----BEGIN PUBLIC KEY-----"
                onChange={(value) => setKeyForm((current) => ({ ...current, publicKeyPem: value }))}
              />
              <PrimaryButton type="submit" disabled={busyAction === 'rotate-key'}>
                {busyAction === 'rotate-key' ? 'Aggiornamento in corso...' : 'Aggiorna chiave'}
              </PrimaryButton>
            </form>
          </div>
        </div>
      ) : (
        <EmptyState
          title="Nessuna azienda selezionata"
          message="Seleziona un'azienda dall'elenco per gestire dati, limiti, chiavi e andamento del servizio."
        />
      )}
    </SectionCard>
  )
}

export default TenantWorkspace
