import { NavLink } from 'react-router-dom'

import { GhostButton, ThemeToggle } from './ui.jsx'

const navigation = [
  { to: '/admin', label: 'Pannello' },
  { to: '/chat', label: 'Assistenza' },
]

function AppShell({ adminSession, logoutInCorso, onLogout, theme, onToggleTheme, children }) {
  return (
    <div className="min-h-screen">
      <div className="mx-auto flex min-h-screen max-w-7xl flex-col gap-6 px-4 py-5 sm:px-6 lg:px-8 lg:py-8">
        <header className="app-topbar rounded-[2rem] border px-5 py-4 lg:px-6">
          <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
            <div>
              <div className="text-[11px] uppercase tracking-[0.3em] text-muted">Spazio di assistenza</div>
              <div className="mt-2 flex flex-wrap items-center gap-3">
                <h1 className="text-2xl text-ink">Gestione e supporto</h1>
                {adminSession ? (
                  <span className="rounded-full border border-success-border bg-success-soft px-3 py-1 text-[11px] uppercase tracking-[0.22em] text-success">
                    Accesso attivo
                  </span>
                ) : null}
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-3">
              <nav className="app-nav flex flex-wrap gap-2 rounded-full border p-1">
                {navigation.map((item) => (
                  <NavLink
                    key={item.to}
                    to={item.to}
                    className={({ isActive }) =>
                      `rounded-full px-4 py-2 text-sm transition ${
                        isActive
                          ? 'nav-link-active'
                          : 'nav-link'
                      }`
                    }
                  >
                    {item.label}
                  </NavLink>
                ))}
              </nav>

              <ThemeToggle theme={theme} onToggle={onToggleTheme} />

              {adminSession ? (
                <div className="flex items-center gap-3">
                  <div className="hidden text-right md:block">
                    <div className="text-sm text-ink">{adminSession.display_name}</div>
                    <div className="text-xs text-muted">{adminSession.username}</div>
                  </div>
                  <GhostButton type="button" onClick={onLogout} disabled={logoutInCorso}>
                    {logoutInCorso ? 'Uscita in corso...' : 'Esci'}
                  </GhostButton>
                </div>
              ) : null}
            </div>
          </div>
        </header>

        <main className="flex flex-1 flex-col gap-6">{children}</main>
      </div>
    </div>
  )
}

export default AppShell
