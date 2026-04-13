import { useEffect, useState } from 'react'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'

import AppShell from './components/AppShell.jsx'
import AdminLoginPage from './pages/AdminLoginPage.jsx'
import AdminPage from './pages/AdminPage.jsx'
import ChatPage from './pages/ChatPage.jsx'
import { fetchAdminMe, loginAdmin, logoutAdmin } from './lib/api.js'
import { normalizeBaseUrl } from './lib/dashboard.js'

const API_BASE_URL = normalizeBaseUrl(import.meta.env.VITE_API_BASE_URL || '')

function App() {
  const [adminSession, setAdminSession] = useState(null)
  const [loadingAdminSession, setLoadingAdminSession] = useState(true)
  const [logoutInCorso, setLogoutInCorso] = useState(false)

  useEffect(() => {
    let isActive = true

    async function caricaSessione() {
      setLoadingAdminSession(true)
      try {
        const sessione = await fetchAdminMe(API_BASE_URL)
        if (isActive) {
          setAdminSession(sessione)
        }
      } catch {
        if (isActive) {
          setAdminSession(null)
        }
      } finally {
        if (isActive) {
          setLoadingAdminSession(false)
        }
      }
    }

    void caricaSessione()

    return () => {
      isActive = false
    }
  }, [])

  async function handleLogin(credenziali) {
    const sessione = await loginAdmin(API_BASE_URL, credenziali)
    setAdminSession({
      username: sessione.username,
      display_name: sessione.display_name,
    })
    return sessione
  }

  async function handleLogout() {
    setLogoutInCorso(true)
    try {
      await logoutAdmin(API_BASE_URL)
    } finally {
      setAdminSession(null)
      setLogoutInCorso(false)
    }
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/admin" replace />} />
        <Route
          path="/admin/login"
          element={
            <AdminLoginPage
              adminSession={adminSession}
              loadingAdminSession={loadingAdminSession}
              onLogin={handleLogin}
            />
          }
        />
        <Route
          path="/admin"
          element={
            <ProtectedAdminRoute adminSession={adminSession} loadingAdminSession={loadingAdminSession}>
              <AppShell
                adminSession={adminSession}
                logoutInCorso={logoutInCorso}
                onLogout={() => {
                  void handleLogout()
                }}
              >
                <AdminPage
                  adminSession={adminSession}
                  onLogout={() => {
                    void handleLogout()
                  }}
                  onSessionExpired={() => setAdminSession(null)}
                />
              </AppShell>
            </ProtectedAdminRoute>
          }
        />
        <Route
          path="/chat"
          element={
            <AppShell
              adminSession={adminSession}
              logoutInCorso={logoutInCorso}
              onLogout={() => {
                void handleLogout()
              }}
            >
              <ChatPage />
            </AppShell>
          }
        />
      </Routes>
    </BrowserRouter>
  )
}

function ProtectedAdminRoute({ adminSession, loadingAdminSession, children }) {
  if (loadingAdminSession) {
    return (
      <div className="flex min-h-screen items-center justify-center px-6 text-center text-stone-200">
        Verifica dell'accesso in corso...
      </div>
    )
  }

  if (!adminSession) {
    return <Navigate to="/admin/login" replace />
  }

  return children
}

export default App
