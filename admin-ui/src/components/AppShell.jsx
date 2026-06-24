import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useLayoutEffect,
  useMemo,
  useRef,
  useState,
} from 'react'
import { NavLink, useLocation } from 'react-router-dom'

import { ThemeToggle } from './ui.jsx'

const navigation = [
  { to: '/admin', label: 'Pannello' },
  { to: '/chat', label: 'Assistenza' },
]

const AppHeaderActionContext = createContext(null)

export function useAppHeaderAction({ label, disabled = false, onClick }) {
  const registerHeaderAction = useContext(AppHeaderActionContext)
  const onClickRef = useRef(onClick)

  useLayoutEffect(() => {
    onClickRef.current = onClick
  })

  useEffect(() => {
    if (!registerHeaderAction) return undefined

    return registerHeaderAction({
      label,
      disabled,
      onClick: () => onClickRef.current?.(),
    })
  }, [disabled, label, registerHeaderAction])
}

function AppShell({ theme, onToggleTheme, children }) {
  const { pathname } = useLocation()
  const isChatPage = pathname === '/chat'
  const [headerAction, setHeaderAction] = useState(null)
  const registerHeaderAction = useCallback((action) => {
    setHeaderAction(action)

    return () => {
      setHeaderAction((currentAction) =>
        currentAction === action ? null : currentAction,
      )
    }
  }, [])
  const headerActionContext = useMemo(
    () => registerHeaderAction,
    [registerHeaderAction],
  )

  return (
    <div className={`app-shell ${isChatPage ? 'app-shell--chat' : ''}`}>
      <div className="app-shell__frame mx-auto flex flex-col gap-6 px-4 py-5 sm:px-6 lg:px-8 lg:py-8">
        <header className="app-topbar">
          <div className="app-topbar__content">
            <div className="brand-area">
            <NavLink
              to="/chat"
                className="brand-link"
              aria-label="Magia - vai alla chat"
            >
              <img
                src="/magia-logo.png"
                alt="Magia"
                  className="brand-logo"
              />
            </NavLink>
              <span className="brand-badge">AI Assistant</span>
            </div>

            <div className="header-actions">
              <nav className="app-nav" aria-label="Navigazione principale">
                {navigation.map((item) => (
                  <NavLink
                    key={item.to}
                    to={item.to}
                    className={({ isActive }) =>
                      `app-nav__item ${
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

              {headerAction ? (
                <button
                  type="button"
                  className="header-icon-button"
                  onClick={headerAction.onClick}
                  disabled={headerAction.disabled}
                  aria-label={headerAction.label}
                  data-tooltip={headerAction.label}
                  title={headerAction.label}
                >
                  <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
                    <path d="M20 11a8 8 0 1 0-2.3 5.7" />
                    <path d="M20 5v6h-6" />
                  </svg>
                </button>
              ) : null}

              <ThemeToggle theme={theme} onToggle={onToggleTheme} />
            </div>
          </div>
        </header>

        <AppHeaderActionContext.Provider value={headerActionContext}>
          <main className="flex min-h-0 flex-1 flex-col gap-6">{children}</main>
        </AppHeaderActionContext.Provider>
      </div>
    </div>
  )
}

export default AppShell
