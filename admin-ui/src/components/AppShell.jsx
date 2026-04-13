import { NavLink } from 'react-router-dom'

import { GhostButton } from './ui.jsx'

const navigation = [
  { to: '/admin', label: 'Pannello' },
  { to: '/chat', label: 'Assistenza' },
]

function AppShell({ adminSession, logoutInCorso, onLogout, children }) {
  return (
    <div className="min-h-screen">
      <div className="mx-auto flex min-h-screen max-w-7xl flex-col gap-6 px-4 py-5 sm:px-6 lg:px-8 lg:py-8">
        <header className="rounded-[2rem] border border-white/10 bg-black/20 px-5 py-4 shadow-[0_14px_50px_rgba(0,0,0,0.2)] backdrop-blur lg:px-6">
          <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
            <div>
              <div className="text-[11px] uppercase tracking-[0.3em] text-stone-400">Spazio di assistenza</div>
              <div className="mt-2 flex flex-wrap items-center gap-3">
                <h1 className="text-2xl text-stone-50">Gestione e supporto</h1>
                {adminSession ? (
                  <span className="rounded-full border border-emerald-300/20 bg-emerald-300/10 px-3 py-1 text-[11px] uppercase tracking-[0.22em] text-emerald-100">
                    Accesso attivo
                  </span>
                ) : null}
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-3">
              <nav className="flex flex-wrap gap-2 rounded-full border border-white/10 bg-white/[0.04] p-1">
                {navigation.map((item) => (
                  <NavLink
                    key={item.to}
                    to={item.to}
                    className={({ isActive }) =>
                      `rounded-full px-4 py-2 text-sm transition ${
                        isActive
                          ? 'bg-amber-500 text-stone-950'
                          : 'text-stone-200 hover:bg-white/[0.08] hover:text-stone-50'
                      }`
                    }
                  >
                    {item.label}
                  </NavLink>
                ))}
              </nav>

              {adminSession ? (
                <div className="flex items-center gap-3">
                  <div className="hidden text-right md:block">
                    <div className="text-sm text-stone-50">{adminSession.display_name}</div>
                    <div className="text-xs text-stone-400">{adminSession.username}</div>
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
