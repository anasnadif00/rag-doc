import { useEffect, useState } from 'react'

import CreateTenantSection from '../components/CreateTenantSection.jsx'
import IngestSection from '../components/IngestSection.jsx'
import ModelSettingsSection from '../components/ModelSettingsSection.jsx'
import TenantListSection from '../components/TenantListSection.jsx'
import TenantWorkspace from '../components/TenantWorkspace.jsx'
import { GhostButton } from '../components/ui.jsx'
import {
  activateTenant,
  createTenant,
  createTenantUser,
  deleteTenantUser,
  fetchHealth,
  fetchModelSettings,
  fetchTenantUsage,
  fetchTenantUsers,
  fetchTenants,
  regenerateTenantUserPassword,
  rotateTenantKey,
  runIngestion,
  suspendTenant,
  updateTenant,
  updateTenantLicense,
  updateModelSettings,
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
  const [tenantUsers, setTenantUsers] = useState([])
  const [modelSettings, setModelSettings] = useState(null)
  const [modelForm, setModelForm] = useState(null)
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
  const [loadingTenantUsers, setLoadingTenantUsers] = useState(false)
  const [loadingModelSettings, setLoadingModelSettings] = useState(false)
  const [loadingUsage, setLoadingUsage] = useState(false)
  const [busyAction, setBusyAction] = useState('')
  const [tenantUserSecret, setTenantUserSecret] = useState(null)
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
  const serviceStatus = loadingHealth ? 'Caricamento' : health?.status === 'ok' ? 'Operativo' : 'Non disponibile'
  const serviceDetail = health
    ? `${health.knowledge_base_exists ? 'Contenuti disponibili' : 'Contenuti da verificare'} | ${
        health.lexical_index_exists ? 'Ricerca pronta' : 'Ricerca da aggiornare'
      }`
    : healthError || 'Verifica dello stato in corso.'
  const securityStatus = health?.security_configured ? 'Configurata' : 'Da completare'
  const securityDetail = health?.security_configured
    ? 'Impostazioni principali presenti.'
    : 'Controlla configurazione e chiavi.'

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
    let isActive = true
    setLoadingModelSettings(true)

    fetchModelSettings(API_BASE_URL)
      .then((payload) => {
        if (!isActive) return
        setModelSettings(payload)
        setModelForm({
          generationModel: payload.generation_model,
          rerankModel: payload.rerank_model,
        })
      })
      .catch((error) => {
        if (!isActive) return
        if (error.status === 401) {
          onSessionExpired()
          return
        }
        setModelSettings(null)
        setModelForm(null)
        setNotice({ tone: 'error', message: error.message || 'Non e stato possibile leggere i modelli AI.' })
      })
      .finally(() => {
        if (isActive) setLoadingModelSettings(false)
      })

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

  useEffect(() => {
    if (!selectedTenant) {
      setTenantUsers([])
      setTenantUserSecret(null)
      return
    }

    let isActive = true
    setTenantUserSecret(null)
    setLoadingTenantUsers(true)
    fetchTenantUsers(API_BASE_URL, selectedTenant.id)
      .then((payload) => {
        if (isActive) setTenantUsers(payload)
      })
      .catch((error) => {
        if (!isActive) return
        if (error.status === 401) {
          onSessionExpired()
          return
        }
        setTenantUsers([])
        setNotice({ tone: 'error', message: error.message || 'Non e stato possibile leggere gli utenti tenant.' })
      })
      .finally(() => {
        if (isActive) setLoadingTenantUsers(false)
      })

    return () => {
      isActive = false
    }
  }, [onSessionExpired, selectedTenant])

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

  async function refreshTenantUsers(tenantId = selectedTenant?.id) {
    if (!tenantId) {
      setTenantUsers([])
      return
    }

    setLoadingTenantUsers(true)
    try {
      const payload = await fetchTenantUsers(API_BASE_URL, tenantId)
      setTenantUsers(payload)
    } catch (error) {
      if (error.status === 401) {
        onSessionExpired()
        return
      }
      setTenantUsers([])
      setNotice({ tone: 'error', message: error.message || 'Non e stato possibile leggere gli utenti tenant.' })
    } finally {
      setLoadingTenantUsers(false)
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

  async function handleCreateTenantUser(payload) {
    if (!selectedTenant) return false
    if (!payload.username || !payload.display_name) {
      setNotice({ tone: 'error', message: 'Inserisci username e nome visualizzato.' })
      return false
    }

    const result = await runAction(
      'create-tenant-user',
      () => createTenantUser(API_BASE_URL, selectedTenant.id, payload),
      'Utente tenant creato. Salva la password temporanea.',
      "Non e stato possibile creare l'utente tenant.",
    )
    if (!result) return false
    setTenantUserSecret({
      username: result.user.username,
      temporaryPassword: result.temporary_password,
    })
    await refreshTenantUsers(selectedTenant.id)
    return true
  }

  async function handleSaveModelSettings(event) {
    event.preventDefault()
    if (!modelForm) return

    const result = await runAction(
      'save-model-settings',
      () =>
        updateModelSettings(API_BASE_URL, {
          generation_model: modelForm.generationModel,
          rerank_model: modelForm.rerankModel,
        }),
      'Modelli OpenAI aggiornati.',
      'Non e stato possibile salvare i modelli AI.',
    )
    if (!result) return
    setModelSettings(result)
    setModelForm({
      generationModel: result.generation_model,
      rerankModel: result.rerank_model,
    })
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

  async function handleRegenerateTenantUserPassword(user) {
    if (!selectedTenant) return
    const confirmed = window.confirm(`Rigenerare la password per ${user.username}?`)
    if (!confirmed) return

    const result = await runAction(
      `regenerate-tenant-user:${user.id}`,
      () => regenerateTenantUserPassword(API_BASE_URL, selectedTenant.id, user.id),
      'Password rigenerata. Salva la nuova password temporanea.',
      'Non e stato possibile rigenerare la password.',
    )
    if (!result) return
    setTenantUserSecret({
      username: result.user.username,
      temporaryPassword: result.temporary_password,
    })
    await refreshTenantUsers(selectedTenant.id)
  }

  async function handleDeleteTenantUser(user) {
    if (!selectedTenant) return
    const confirmed = window.confirm(`Eliminare l'utente ${user.username}?`)
    if (!confirmed) return

    setBusyAction(`delete-tenant-user:${user.id}`)
    setNotice(null)
    try {
      await deleteTenantUser(API_BASE_URL, selectedTenant.id, user.id)
      setTenantUserSecret(null)
      setNotice({ tone: 'success', message: 'Utente tenant eliminato.' })
      await refreshTenantUsers(selectedTenant.id)
    } catch (error) {
      if (error.status === 401) {
        onSessionExpired()
        return
      }
      setNotice({ tone: 'error', message: error.message || "Non e stato possibile eliminare l'utente tenant." })
    } finally {
      setBusyAction('')
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
    <div className="admin-page">
      <header className="admin-page-header">
        <div>
          <div className="admin-kicker">Pannello amministratore</div>
          <h1>Gestione aziende</h1>
          <p>Configura accessi, limiti, contenuti e modelli senza uscire dal pannello operativo.</p>
        </div>
        <div className="admin-page-header__actions">
          <div className="admin-user-chip">
            <span>Sessione</span>
            <strong>{adminSession?.display_name || adminSession?.username || 'Admin'}</strong>
          </div>
          <GhostButton type="button" className="admin-logout-button" onClick={onLogout}>
            Esci
          </GhostButton>
        </div>
      </header>

      {notice ? (
        <div className={`admin-notice admin-notice--${notice.tone}`}>
          {notice.message}
        </div>
      ) : null}

      <section className="admin-status-strip" aria-label="Stato pannello">
        <AdminStat
          label="Servizio"
          value={serviceStatus}
          detail={serviceDetail}
          tone={health?.status === 'ok' ? 'success' : 'neutral'}
        />
        <AdminStat
          label="Aziende"
          value={String(tenants.length)}
          detail={`${activeCount} attive | ${suspendedCount} sospese`}
          tone="primary"
        />
        <AdminStat
          label="Archivi dedicati"
          value={String(overlayEnabledCount)}
          detail="Aziende con archivio dedicato attivo"
          tone="neutral"
        />
        <AdminStat
          label="Protezione"
          value={securityStatus}
          detail={securityDetail}
          tone={health?.security_configured ? 'success' : 'danger'}
        />
      </section>

      <section className="admin-workbench">
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
          tenantUsers={tenantUsers}
          loadingTenantUsers={loadingTenantUsers}
          tenantUserSecret={tenantUserSecret}
          busyAction={busyAction}
          onSaveProfile={handleSaveProfile}
          onSaveLicense={handleSaveLicense}
          onRotateKey={handleRotateKey}
          onCreateTenantUser={handleCreateTenantUser}
          onRegenerateTenantUserPassword={handleRegenerateTenantUserPassword}
          onDeleteTenantUser={handleDeleteTenantUser}
          onDismissTenantUserSecret={() => setTenantUserSecret(null)}
          onRefreshTenantUsers={() => {
            void refreshTenantUsers(selectedTenant?.id)
          }}
          onActivate={() => {
            void handleStatusChange('active')
          }}
          onSuspend={() => {
            void handleStatusChange('suspended')
          }}
        />
      </section>

      <section className="admin-operations-grid">
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
        <ModelSettingsSection
          modelSettings={modelSettings}
          modelForm={modelForm}
          setModelForm={setModelForm}
          loading={loadingModelSettings}
          busyAction={busyAction}
          onSubmit={handleSaveModelSettings}
        />
      </section>
    </div>
  )
}

function AdminStat({ label, value, detail, tone = 'neutral' }) {
  return (
    <div className={`admin-stat admin-stat--${tone}`}>
      <div className="admin-stat__label">{label}</div>
      <div className="admin-stat__value">{value}</div>
      <div className="admin-stat__detail">{detail}</div>
    </div>
  )
}

export default AdminPage
