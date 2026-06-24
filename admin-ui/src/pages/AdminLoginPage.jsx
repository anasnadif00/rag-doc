import { useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'

import { PrimaryButton, TextField, ThemeToggle } from '../components/ui.jsx'

function AdminLoginPage({ adminSession, loadingAdminSession, onLogin, theme, onToggleTheme }) {
  const navigate = useNavigate()
  const [username, setUsername] = useState('admin')
  const [password, setPassword] = useState('')
  const [errore, setErrore] = useState('')
  const [accessoInCorso, setAccessoInCorso] = useState(false)

  if (!loadingAdminSession && adminSession) {
    return <Navigate to="/admin" replace />
  }

  async function handleSubmit(event) {
    event.preventDefault()
    setAccessoInCorso(true)
    setErrore('')

    try {
      await onLogin({
        username: username.trim(),
        password,
      })
      navigate('/admin', { replace: true })
    } catch (error) {
      setErrore(error.message || "Non e stato possibile completare l'accesso.")
    } finally {
      setAccessoInCorso(false)
    }
  }

  return (
    <div className="relative flex min-h-screen items-center justify-center px-4 py-24 sm:py-8">
      <div className="absolute right-4 top-5 sm:right-6">
        <ThemeToggle theme={theme} onToggle={onToggleTheme} />
      </div>
      <div className="app-login-panel w-full max-w-md rounded-[2rem] border p-6">
        <div className="space-y-3">
          <div className="brand-badge inline-flex items-center rounded-full border px-3 py-1 text-[11px] uppercase tracking-[0.28em]">
            Accesso amministratore
          </div>
          <h1 className="text-4xl leading-tight text-ink">Benvenuto</h1>
          <p className="text-sm leading-7 text-copy">
            Inserisci le tue credenziali per aprire il pannello di gestione.
          </p>
        </div>

        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          <TextField
            label="Utente"
            value={username}
            placeholder="admin"
            autoComplete="username"
            onChange={setUsername}
          />
          <TextField
            label="Password"
            type="password"
            value={password}
            placeholder="Inserisci la password"
            autoComplete="current-password"
            onChange={setPassword}
          />

          {errore ? (
            <div className="rounded-2xl border border-danger-border bg-danger-soft px-4 py-3 text-sm text-danger">
              {errore}
            </div>
          ) : null}

          <PrimaryButton type="submit" className="w-full" disabled={accessoInCorso}>
            {accessoInCorso ? 'Accesso in corso...' : 'Accedi'}
          </PrimaryButton>
        </form>
      </div>
    </div>
  )
}

export default AdminLoginPage
