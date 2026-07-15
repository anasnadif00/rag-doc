import { NavLink, useLocation } from "react-router-dom";

import { ThemeToggle } from "./ui.jsx";

function AppShell({ theme, onToggleTheme, children }) {
  const { pathname } = useLocation();
  const isChatPage = pathname === "/chat";
  const isAdminPage = pathname.startsWith("/admin");

  if (isAdminPage) {
    return (
      <div className="admin-shell">
        <header className="admin-topbar">
          <div className="admin-topbar__inner">
            <NavLink
              to="/admin"
              className="admin-brand"
              aria-label="Magia admin"
            >
              <span className="admin-brand__mark">M</span>
              <span>
                <strong>Magia</strong>
                <small>Admin</small>
              </span>
            </NavLink>

            <div className="admin-topbar__controls">
              <ThemeToggle theme={theme} onToggle={onToggleTheme} />
              <nav className="admin-nav" aria-label="Sezioni principali">
                <NavLink
                  to="/admin"
                  className={({ isActive }) =>
                    `admin-nav__link ${isActive ? "admin-nav__link--active" : ""}`
                  }
                >
                  Admin
                </NavLink>
                <NavLink
                  to="/chat"
                  className={({ isActive }) =>
                    `admin-nav__link ${isActive ? "admin-nav__link--active" : ""}`
                  }
                >
                  Chat
                </NavLink>
              </nav>
            </div>
          </div>
        </header>

        <main className="admin-main">{children}</main>
      </div>
    );
  }

  return (
    <div className={`app-shell ${isChatPage ? "app-shell--chat" : ""}`}>
      <div className="app-shell__frame mx-auto flex max-w-7xl flex-col gap-6 px-4 py-5 sm:px-6 lg:px-8 lg:py-8">
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
              <ThemeToggle theme={theme} onToggle={onToggleTheme} />
              <nav
                className="app-nav inline-flex rounded-full border p-1"
                aria-label="Sezioni principali"
              >
                <NavLink
                  to="/admin"
                  className={({ isActive }) =>
                    `nav-link inline-flex rounded-full px-3 py-2 text-sm transition ${
                      isActive ? "nav-link-active" : ""
                    }`
                  }
                >
                  Admin
                </NavLink>
                <NavLink
                  to="/chat"
                  className={({ isActive }) =>
                    `nav-link inline-flex rounded-full px-3 py-2 text-sm transition ${
                      isActive ? "nav-link-active" : ""
                    }`
                  }
                >
                  Chat
                </NavLink>
              </nav>
            </div>
          </div>
        </header>

        <main className="flex min-h-0 flex-1 flex-col gap-6">{children}</main>
      </div>
    </div>
  );
}

export default AppShell;
