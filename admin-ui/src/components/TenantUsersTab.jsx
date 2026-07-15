import { useState } from 'react'

import { buildTenantUserPayload, createDefaultTenantUserForm, formatDateTime } from '../lib/dashboard.js'
import { EmptyState, GhostButton, PrimaryButton, SectionHeading, StatusBadge, TextField } from './ui.jsx'

function TenantUsersTab({
  tenantUsers,
  loadingTenantUsers,
  busyAction,
  tenantUserSecret,
  onCreateUser,
  onRegeneratePassword,
  onDeleteUser,
  onDismissSecret,
  onRefreshUsers,
}) {
  const [showCreateForm, setShowCreateForm] = useState(false)
  const [createForm, setCreateForm] = useState(createDefaultTenantUserForm)
  const [copiedSecret, setCopiedSecret] = useState(false)
  const canSubmit = createForm.username.trim() && createForm.displayName.trim()

  async function handleCreateSubmit(event) {
    event.preventDefault()
    if (!canSubmit) return
    const created = await onCreateUser(buildTenantUserPayload(createForm))
    if (!created) return
    setCreateForm(createDefaultTenantUserForm())
    setShowCreateForm(false)
  }

  async function handleCopySecret() {
    if (!tenantUserSecret?.temporaryPassword || !navigator.clipboard) return
    await navigator.clipboard.writeText(tenantUserSecret.temporaryPassword)
    setCopiedSecret(true)
    window.setTimeout(() => setCopiedSecret(false), 1400)
  }

  return (
    <div className="tenant-users-pane space-y-3">
      <div className="tenant-tab-pane-header">
        <SectionHeading
          title="Utenti tenant"
          subtitle="Gestisci gli accessi degli utenti collegati all'azienda selezionata."
        />
        <div className="tenant-tab-pane-actions">
          <GhostButton type="button" disabled={loadingTenantUsers} onClick={onRefreshUsers}>
            {loadingTenantUsers ? 'Aggiornamento...' : 'Aggiorna'}
          </GhostButton>
          <PrimaryButton
            type="button"
            disabled={busyAction === 'create-tenant-user'}
            onClick={() => setShowCreateForm((current) => !current)}
          >
            <PlusIcon />
            Crea utente
          </PrimaryButton>
        </div>
      </div>

      {tenantUserSecret ? (
        <div className="tenant-user-secret" role="status">
          <div className="tenant-user-secret__copy">
            <span>Password temporanea</span>
            <strong>{tenantUserSecret.username}</strong>
          </div>
          <code>{tenantUserSecret.temporaryPassword}</code>
          <div className="tenant-user-secret__actions">
            <GhostButton type="button" onClick={handleCopySecret}>
              {copiedSecret ? 'Copiata' : 'Copia'}
            </GhostButton>
            <GhostButton type="button" onClick={onDismissSecret}>
              Chiudi
            </GhostButton>
          </div>
        </div>
      ) : null}

      {showCreateForm ? (
        <form className="admin-subsection tenant-user-create-form" onSubmit={handleCreateSubmit}>
          <div className="grid gap-3 sm:grid-cols-2">
            <TextField
              label="Username"
              value={createForm.username}
              placeholder="mario.rossi"
              autoComplete="off"
              onChange={(value) => setCreateForm((current) => ({ ...current, username: value }))}
            />
            <TextField
              label="Nome visualizzato"
              value={createForm.displayName}
              placeholder="Mario Rossi"
              autoComplete="off"
              onChange={(value) => setCreateForm((current) => ({ ...current, displayName: value }))}
            />
          </div>
          <div className="mt-3 flex flex-wrap gap-2">
            <PrimaryButton type="submit" disabled={!canSubmit || busyAction === 'create-tenant-user'}>
              {busyAction === 'create-tenant-user' ? 'Creazione...' : 'Crea e genera password'}
            </PrimaryButton>
            <GhostButton
              type="button"
              onClick={() => {
                setCreateForm(createDefaultTenantUserForm())
                setShowCreateForm(false)
              }}
            >
              Annulla
            </GhostButton>
          </div>
        </form>
      ) : null}

      {loadingTenantUsers ? (
        <div className="tenant-users-loading">Caricamento utenti...</div>
      ) : tenantUsers.length ? (
        <div className="tenant-users-table-wrap">
          <table className="tenant-users-table">
            <thead>
              <tr>
                <th>Utente</th>
                <th>Stato</th>
                <th>Creato</th>
                <th>Password</th>
                <th>Azioni</th>
              </tr>
            </thead>
            <tbody>
              {tenantUsers.map((user) => (
                <tr key={user.id}>
                  <td>
                    <strong>{user.display_name}</strong>
                    <span>{user.username}</span>
                  </td>
                  <td>
                    <StatusBadge status={user.status} />
                  </td>
                  <td>{formatDateTime(user.created_at)}</td>
                  <td>{formatDateTime(user.rotated_at)}</td>
                  <td>
                    <div className="tenant-user-row-actions">
                      <GhostButton
                        type="button"
                        className="tenant-user-regenerate-button"
                        disabled={busyAction === `regenerate-tenant-user:${user.id}`}
                        onClick={() => onRegeneratePassword(user)}
                      >
                        <RegenerateIcon />
                        {busyAction === `regenerate-tenant-user:${user.id}` ? 'Rigenero...' : 'Rigenera password'}
                      </GhostButton>
                      <button
                        type="button"
                        className="tenant-user-delete-button"
                        disabled={busyAction === `delete-tenant-user:${user.id}`}
                        aria-label={`Elimina ${user.username}`}
                        title="Elimina utente"
                        onClick={() => onDeleteUser(user)}
                      >
                        <TrashIcon />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <EmptyState
          title="Nessun utente tenant"
          message="Crea il primo utente per abilitare l'accesso alla chat con username e password."
        />
      )}
    </div>
  )
}

function PlusIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="button-icon">
      <path d="M12 5v14M5 12h14" />
    </svg>
  )
}

function RegenerateIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24" className="button-icon">
      <path d="M20 6v5h-5" />
      <path d="M4 18v-5h5" />
      <path d="M18.1 9A7 7 0 0 0 6.3 6.3L4 8.6" />
      <path d="M5.9 15a7 7 0 0 0 11.8 2.7L20 15.4" />
    </svg>
  )
}

function TrashIcon() {
  return (
    <svg aria-hidden="true" viewBox="0 0 24 24">
      <path d="M3 6h18" />
      <path d="M8 6V4h8v2" />
      <path d="M19 6l-1 14H6L5 6" />
      <path d="M10 11v5" />
      <path d="M14 11v5" />
    </svg>
  )
}

export default TenantUsersTab
