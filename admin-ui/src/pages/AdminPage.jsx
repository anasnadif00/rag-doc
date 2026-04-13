import { useEffect, useState } from 'react'

import CreateTenantSection from '../components/CreateTenantSection.jsx'
import HeroSection from '../components/HeroSection.jsx'
import IngestSection from '../components/IngestSection.jsx'
import TenantListSection from '../components/TenantListSection.jsx'
import TenantWorkspace from '../components/TenantWorkspace.jsx'
import { MetricCard } from '../components/ui.jsx'
import {
  activateTenant,
  createTenant,
  fetchHealth,
  fetchTenantUsage,
  fetchTenants,
  rotateTenantKey,
  runIngestion,
  suspendTenant,
  updateTenant,
  updateTenantLicense,
} from '../lib/api.js'
import {
  buildCreatePayload,
  buildIngestPayload,
  buildKeyPayload,
  buildLicenseForm,
  buildLicensePayload,
  buildTenantProfileForm,
  buildTenantProfilePayload,
  createDefaultCreateForm,
  createDefaultIngestForm,
  createDefaultKeyForm,
  normalizeBaseUrl,
} from '../lib/dashboard.js'

const API_BASE_URL = normalizeBaseUrl(import.meta.env.VITE_API_BASE_URL || '')

function AdminPage({ adminSession, onLogout, onSessionExpired }) {
  const [health, setHealth] = useState(null)
  const [healthError, setHealthError] = useState('')
  const [tenants, setTenants] = useState([])
  const [selectedTenantId, setSelectedTenantId] = useState(null)
  const [usageDays, setUsageDays] = useState(14)
  const [usageRows, setUsageRows] = useState([])
  const [ingestForm, setIngestForm] = useState(createDefaultIngestForm)
  const [ingestResult, setIngestResult] = useState(null)
  const [createForm, setCreateForm] = useState(createDefaultCreateForm)
  const [editForm, setEditForm] = useState(null)
  const [licenseForm, setLicenseForm] = useState(null)
  const [keyForm, setKeyForm] = useState(createDefaultKeyForm)
  const [tenantSearch, setTenantSearch] = useState('')
  const [loadingHealth, setLoadingHealth] = useState(false)
  const [loadingTenants, setLoadingTenants] = useState(false)
  const [loadingUsage, setLoadingUsage] = useState(false)
  const [busyAction, setBusyAction] = useState('')
  const [notice, setNotice] = useState(null)

  const selectedTenant = tenants.find((tenant) => tenant.id === selectedTenantId) || null
  const filteredTenants = tenants.filter((tenant) => {
    const term = tenantSearch.trim().toLowerCase()
    if (!term) return true
    return [tenant.display_name, tenant.tenant_code, tenant.issuer]
      .filter(Boolean)
      .some((value) => value.toLowerCase().includes(term))
  })

  const activeCount = tenants.filter((tenant) => tenant.status === 'active').length
  const suspendedCount = tenants.filter((tenant) => tenant.status === 'suspended').length
  const overlayEnabledCount = tenants.filter((tenant) => tenant.license?.overlay_kb_enabled).length
  const usageTotals = usageRows.reduce(
    (accumulator, row) => ({
      messages: accumulator.messages + row.messages_in + row.messages_out,
      promptTokens: accumulator.promptTokens + row.prompt_tokens,
      completionTokens: accumulator.completionTokens + row.completion_tokens,
      wsConnects: accumulator.wsConnects + row.ws_connects,
    }),
    { messages: 0, promptTokens: 0, completionTokens: 0, wsConnects: 0 },
  )

  useEffect(() => {
    let isActive = true
    setLoadingHealth(true)
    fetchHealth(API_BASE_URL)
      .then((payload) => {
        if (!isActive) return
        setHealth(payload)
        setHealthError('')
      })
      .catch(() => {
        if (!isActive) return
        setHealth(null)
        setHealthError('Servizio non raggiungibile.')
      })
      .finally(() => {
        if (isActive) setLoadingHealth(false)
      })

    return () => {
      isActive = false
    }
  }, [])

  useEffect(() => {
    let isActive = true

    async function caricaAziende() {
      setLoadingTenants(true)
      try {
        const payload = await fetchTenants(API_BASE_URL)
        if (!isActive) return
        setTenants(payload)
        setSelectedTenantId((currentId) =>
          payload.some((tenant) => tenant.id === currentId) ? currentId : payload[0]?.id || null,
        )
      } catch (error) {
        if (!isActive) return
        if (error.status === 401) {
          onSessionExpired()
          return
        }
        setTenants([])
        setSelectedTenantId(null)
        setNotice({ tone: 'error', message: error.message || 'Non e stato possibile leggere le aziende.' })
      } finally {
        if (isActive) {
          setLoadingTenants(false)
        }
      }
    }

    void caricaAziende()

    return () => {
      isActive = false
    }
  }, [onSessionExpired])

  useEffect(() => {
    if (!selectedTenant) {
      setEditForm(null)
      setLicenseForm(null)
      setKeyForm(createDefaultKeyForm())
      return
    }

    setEditForm(buildTenantProfileForm(selectedTenant))
    setLicenseForm(buildLicenseForm(selectedTenant))
    setKeyForm(createDefaultKeyForm())
  }, [selectedTenant])

  useEffect(() => {
    if (!selectedTenant) {
      setUsageRows([])
      return
    }

    let isActive = true
    setLoadingUsage(true)
    fetchTenantUsage(API_BASE_URL, selectedTenant.id, usageDays)
      .then((payload) => {
        if (isActive) setUsageRows(payload)
      })
      .catch((error) => {
        if (!isActive) return
        if (error.status === 401) {
          onSessionExpired()
          return
        }
        setUsageRows([])
        setNotice({ tone: 'error', message: error.message || "Non e stato possibile leggere l'utilizzo." })
      })
      .finally(() => {
        if (isActive) setLoadingUsage(false)
      })

    return () => {
      isActive = false
    }
  }, [onSessionExpired, selectedTenant, usageDays])

  async function refreshTenants(preferredTenantId = null) {
    setLoadingTenants(true)
    try {
      const payload = await fetchTenants(API_BASE_URL)
      setTenants(payload)
      setSelectedTenantId((currentId) => {
        if (preferredTenantId && payload.some((tenant) => tenant.id === preferredTenantId)) return preferredTenantId
        return payload.some((tenant) => tenant.id === currentId) ? currentId : payload[0]?.id || null
      })
    } catch (error) {
      if (error.status === 401) {
        onSessionExpired()
        return
      }
      setTenants([])
      setSelectedTenantId(null)
      setNotice({ tone: 'error', message: error.message || 'Non e stato possibile leggere le aziende.' })
    } finally {
      setLoadingTenants(false)
    }
  }

  async function runAction(actionKey, action, successMessage, fallbackMessage) {
    setBusyAction(actionKey)
    setNotice(null)
    try {
      const result = await action()
      if (successMessage) setNotice({ tone: 'success', message: successMessage })
      return result
    } catch (error) {
      if (error.status === 401) {
        onSessionExpired()
        return null
      }
      setNotice({ tone: 'error', message: error.message || fallbackMessage })
      return null
    } finally {
      setBusyAction('')
    }
  }

  async function handleCreateTenant(event) {
    event.preventDefault()
    const tenant = await runAction(
      'create-tenant',
      () => createTenant(API_BASE_URL, buildCreatePayload(createForm)),
      'Azienda creata con successo.',
      "Non e stato possibile creare l'azienda.",
    )
    if (!tenant) return
    await refreshTenants(tenant.id)
    setCreateForm(createDefaultCreateForm())
  }

  async function handleSaveProfile(event) {
    event.preventDefault()
    if (!selectedTenant || !editForm) return

    const result = await runAction(
      'save-tenant',
      () => updateTenant(API_BASE_URL, selectedTenant.id, buildTenantProfilePayload(editForm)),
      'Dati azienda aggiornati.',
      "Non e stato possibile salvare i dati dell'azienda.",
    )
    if (result) {
      await refreshTenants(selectedTenant.id)
    }
  }

  async function handleSaveLicense(event) {
    event.preventDefault()
    if (!selectedTenant || !licenseForm) return

    const result = await runAction(
      'save-license',
      () => updateTenantLicense(API_BASE_URL, selectedTenant.id, buildLicensePayload(licenseForm)),
      'Limiti aggiornati.',
      'Non e stato possibile salvare i limiti.',
    )
    if (result) {
      await refreshTenants(selectedTenant.id)
    }
  }

  async function handleRotateKey(event) {
    event.preventDefault()
    if (!selectedTenant) return

    const payload = buildKeyPayload(keyForm)
    if (!payload.public_key_pem) {
      setNotice({ tone: 'error', message: 'Inserisci una chiave pubblica prima di continuare.' })
      return
    }

    const result = await runAction(
      'rotate-key',
      () => rotateTenantKey(API_BASE_URL, selectedTenant.id, payload),
      'Chiave aggiornata con successo.',
      'Non e stato possibile aggiornare la chiave.',
    )
    if (result) {
      await refreshTenants(selectedTenant.id)
      setKeyForm(createDefaultKeyForm())
    }
  }

  async function handleStatusChange(nextStatus) {
    if (!selectedTenant) return

    const result =
      nextStatus === 'active'
        ? await runAction(
            'activate-tenant',
            () => activateTenant(API_BASE_URL, selectedTenant.id),
            'Azienda attivata.',
            "Non e stato possibile attivare l'azienda.",
          )
        : await runAction(
            'suspend-tenant',
            () => suspendTenant(API_BASE_URL, selectedTenant.id),
            'Azienda sospesa.',
            "Non e stato possibile sospendere l'azienda.",
          )

    if (result) {
      await refreshTenants(selectedTenant.id)
    }
  }

  async function handleIngest(event) {
    event.preventDefault()
    const result = await runAction(
      'run-ingest',
      () => runIngestion(API_BASE_URL, buildIngestPayload(ingestForm)),
      'Aggiornamento completato.',
      'Non e stato possibile aggiornare i contenuti.',
    )
    if (result) {
      setIngestResult(result)
    }
  }

  return (
    <>
      <HeroSection adminSession={adminSession} onLogout={onLogout} />

      {notice ? (
        <div
          className={`rounded-2xl border px-4 py-3 text-sm ${
            notice.tone === 'success'
              ? 'border-emerald-400/30 bg-emerald-400/10 text-emerald-100'
              : 'border-rose-400/30 bg-rose-400/10 text-rose-100'
          }`}
        >
          {notice.message}
        </div>
      ) : null}

      <section className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <MetricCard
          label="Stato del servizio"
          value={loadingHealth ? 'Caricamento' : health?.status === 'ok' ? 'Operativo' : 'Non disponibile'}
          accent={health?.status === 'ok' ? 'emerald' : 'amber'}
          detail={
            health
              ? `${health.knowledge_base_exists ? 'Contenuti disponibili' : 'Contenuti da verificare'} | ${health.lexical_index_exists ? 'Ricerca pronta' : 'Ricerca da aggiornare'}`
              : healthError || 'Stiamo verificando lo stato del servizio.'
          }
        />
        <MetricCard
          label="Aziende"
          value={String(tenants.length)}
          accent="copper"
          detail={`${activeCount} attive | ${suspendedCount} sospese`}
        />
        <MetricCard
          label="Archivi dedicati"
          value={String(overlayEnabledCount)}
          accent="sky"
          detail="Aziende con archivio dedicato attivo"
        />
        <MetricCard
          label="Protezione"
          value={health?.security_configured ? 'Configurata' : 'Da completare'}
          accent={health?.security_configured ? 'emerald' : 'rose'}
          detail={health?.security_configured ? 'Le impostazioni principali risultano presenti.' : 'Alcune impostazioni di sicurezza richiedono attenzione.'}
        />
      </section>

      <section className="grid gap-6 xl:grid-cols-[0.9fr_1.1fr]">
        <IngestSection
          ingestForm={ingestForm}
          setIngestForm={setIngestForm}
          onSubmit={handleIngest}
          busyAction={busyAction}
          ingestResult={ingestResult}
        />
        <CreateTenantSection
          createForm={createForm}
          setCreateForm={setCreateForm}
          onSubmit={handleCreateTenant}
          busyAction={busyAction}
        />
      </section>

      <section className="grid gap-6 xl:grid-cols-[0.92fr_1.08fr]">
        <TenantListSection
          tenantSearch={tenantSearch}
          setTenantSearch={setTenantSearch}
          filteredTenants={filteredTenants}
          selectedTenantId={selectedTenantId}
          setSelectedTenantId={setSelectedTenantId}
          isAuthenticated
          loadingTenants={loadingTenants}
          onRefresh={() => {
            void refreshTenants(selectedTenantId)
          }}
        />
        <TenantWorkspace
          selectedTenant={selectedTenant}
          editForm={editForm}
          setEditForm={setEditForm}
          licenseForm={licenseForm}
          setLicenseForm={setLicenseForm}
          keyForm={keyForm}
          setKeyForm={setKeyForm}
          usageDays={usageDays}
          setUsageDays={setUsageDays}
          usageRows={usageRows}
          usageTotals={usageTotals}
          loadingUsage={loadingUsage}
          busyAction={busyAction}
          onSaveProfile={handleSaveProfile}
          onSaveLicense={handleSaveLicense}
          onRotateKey={handleRotateKey}
          onActivate={() => {
            void handleStatusChange('active')
          }}
          onSuspend={() => {
            void handleStatusChange('suspended')
          }}
        />
      </section>
    </>
  )
}

export default AdminPage
