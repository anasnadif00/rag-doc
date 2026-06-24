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
            <NavLink
              to="/chat"
              className="inline-flex w-fit rounded-xl focus-visible:outline-offset-4"
              aria-label="Magia - vai alla chat"
            >
              <img
                src="/magia-logo.png"
                alt="Magia"
                className="h-12 w-auto object-contain sm:h-14"
              />
            </NavLink>

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
                <GhostButton type="button" onClick={onLogout} disabled={logoutInCorso}>
                  {logoutInCorso ? 'Uscita in corso...' : 'Esci'}
                </GhostButton>
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
