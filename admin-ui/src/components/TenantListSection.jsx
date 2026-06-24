import { EmptyState, GhostButton, MiniBadge, SectionCard, StatusBadge, TextField } from './ui.jsx'
import { formatNumber, translateStatus } from '../lib/dashboard.js'

function TenantListSection({
  tenantSearch,
  setTenantSearch,
  filteredTenants,
  selectedTenantId,
  setSelectedTenantId,
  isAuthenticated,
  loadingTenants,
  onRefresh,
}) {
  return (
    <SectionCard
      eyebrow="Elenco aziende"
      title="Aziende"
      subtitle="Cerca un'azienda, aprila e aggiorna le sue impostazioni operative."
      actions={
        <GhostButton type="button" disabled={loadingTenants} onClick={onRefresh}>
          {loadingTenants ? 'Aggiornamento...' : 'Aggiorna'}
        </GhostButton>
      }
    >
      <div className="space-y-4">
        <TextField
          label="Cerca azienda"
          value={tenantSearch}
          placeholder="Cerca per nome, codice o identificativo"
          onChange={setTenantSearch}
        />
        <div className="space-y-3">
          {filteredTenants.length ? (
            filteredTenants.map((tenant) => (
              <button
                key={tenant.id}
                type="button"
                onClick={() => setSelectedTenantId(tenant.id)}
                className={`w-full rounded-2xl border px-4 py-4 text-left transition ${
                  tenant.id === selectedTenantId
                    ? 'tenant-card--selected'
                    : 'border-divider bg-surface hover:border-divider-strong hover:bg-subtle'
                }`}
              >
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <div className="text-lg text-ink">{tenant.display_name}</div>
                    <div className="mt-1 text-xs uppercase tracking-[0.24em] text-muted">{tenant.tenant_code}</div>
                  </div>
                  <StatusBadge status={tenant.status} />
                </div>
                <div className="mt-3 flex flex-wrap gap-2 text-xs text-copy">
                  <MiniBadge label={`Livello ${translateStatus(tenant.license_tier)}`} />
                  <MiniBadge label={`Limite ${formatNumber(tenant.license.daily_message_limit)} messaggi/giorno`} />
                  <MiniBadge label={tenant.license.overlay_kb_enabled ? 'Archivio dedicato attivo' : 'Archivio dedicato spento'} />
                </div>
              </button>
            ))
          ) : (
            <EmptyState
              title="Nessuna azienda da mostrare"
              message={
                isAuthenticated
                  ? 'Prova con un altro termine oppure crea la prima azienda dal pannello qui sopra.'
                  : 'Accedi per vedere e gestire le aziende disponibili.'
              }
            />
          )}
        </div>
      </div>
    </SectionCard>
  )
}

export default TenantListSection
