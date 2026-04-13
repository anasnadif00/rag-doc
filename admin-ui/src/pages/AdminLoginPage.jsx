import { useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'

import { PrimaryButton, TextField } from '../components/ui.jsx'

function AdminLoginPage({ adminSession, loadingAdminSession, onLogin }) {
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
    <div className="flex min-h-screen items-center justify-center px-4 py-8">
      <div className="w-full max-w-md rounded-[2rem] border border-white/10 bg-[linear-gradient(145deg,rgba(15,20,19,0.94),rgba(26,18,15,0.92))] p-6 shadow-[0_24px_80px_rgba(0,0,0,0.35)]">
        <div className="space-y-3">
          <div className="inline-flex items-center rounded-full border border-amber-500/30 bg-amber-500/10 px-3 py-1 text-[11px] uppercase tracking-[0.28em] text-amber-200">
            Accesso amministratore
          </div>
          <h1 className="text-4xl leading-tight text-stone-50">Benvenuto</h1>
          <p className="text-sm leading-7 text-stone-300">
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
            <div className="rounded-2xl border border-rose-300/25 bg-rose-300/10 px-4 py-3 text-sm text-rose-100">
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
