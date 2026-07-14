import { useEffect, useLayoutEffect, useState } from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import AppShell from "./components/AppShell.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import AdminPage from "./pages/AdminPage.jsx";
import ChatPage from "./pages/ChatPage.jsx";
import {
  fetchAdminMe,
  fetchChatMe,
  loginAdmin,
  logoutAdmin,
  loginChat,
  logoutChat,
} from "./lib/api.js";
import { normalizeBaseUrl } from "./lib/dashboard.js";

const API_BASE_URL = normalizeBaseUrl(import.meta.env.VITE_API_BASE_URL || "");
const THEME_STORAGE_KEY = "rag-doc-theme";

function getInitialTheme() {
  if (typeof window === "undefined") return "light";

  try {
    const savedTheme = window.localStorage.getItem(THEME_STORAGE_KEY);
    if (savedTheme === "light" || savedTheme === "dark") return savedTheme;
  } catch {
    // Local storage can be disabled; the system preference still provides a stable default.
  }

  return "light";
}

function fetchAdminSession() {
  return fetchAdminMe(API_BASE_URL);
}

function fetchChatSession() {
  return fetchChatMe(API_BASE_URL);
}

function App() {
  const {
    session: adminSession,
    setSession: setAdminSession,
    loadingSession: loadingAdminSession,
  } = useSession({
    fetchSession: fetchAdminSession,
  });
  const {
    session: chatSession,
    setSession: setChatSession,
    loadingSession: loadingChatSession,
  } = useSession({
    fetchSession: fetchChatSession,
  });
  const [theme, setTheme] = useState(getInitialTheme);

  useLayoutEffect(() => {
    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;

    const themeColor = document.querySelector('meta[name="theme-color"]');
    themeColor?.setAttribute(
      "content",
      theme === "dark" ? "#161617" : "#f5f5f7",
    );

    try {
      window.localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch {
      // The selected theme remains active for the current session.
    }
  }, [theme]);

  async function handleLoginAdmin(credenziali) {
    const sessione = await loginAdmin(API_BASE_URL, credenziali);
    setAdminSession({
      username: sessione.username,
      display_name: sessione.display_name,
    });
    return sessione;
  }

  async function handleLoginChat(credenziali) {
    const sessione = await loginChat(API_BASE_URL, credenziali);
    setChatSession(sessione);
    return sessione;
  }

  async function handleLogoutAdmin() {
    try {
      await logoutAdmin(API_BASE_URL);
    } finally {
      setAdminSession(null);
    }
  }

  async function handleLogoutChat() {
    try {
      await logoutChat(API_BASE_URL);
    } finally {
      setChatSession(null);
    }
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/admin" replace />} />
        <Route
          path="/admin/login"
          element={
            <LoginPage
              session={adminSession}
              loadingSession={loadingAdminSession}
              onLogin={handleLoginAdmin}
              theme={theme}
              onToggleTheme={() =>
                setTheme((currentTheme) =>
                  currentTheme === "light" ? "dark" : "light",
                )
              }
              type="admin"
            />
          }
        />
        <Route
          path="/admin"
          element={
            <ProtectedRoute
              navPage="/admin/login"
              session={adminSession}
              loadingSession={loadingAdminSession}
            >
              <AppShell
                theme={theme}
                onToggleTheme={() =>
                  setTheme((currentTheme) =>
                    currentTheme === "light" ? "dark" : "light",
                  )
                }
              >
                <AdminPage
                  adminSession={adminSession}
                  onLogout={() => {
                    void handleLogoutAdmin();
                  }}
                  onSessionExpired={() => setAdminSession(null)}
                />
              </AppShell>
            </ProtectedRoute>
          }
        />
        <Route
          path="/chat/login"
          element={
            <LoginPage
              session={chatSession}
              loadingSession={loadingChatSession}
              onLogin={handleLoginChat}
              theme={theme}
              onToggleTheme={() =>
                setTheme((currentTheme) =>
                  currentTheme === "light" ? "dark" : "light",
                )
              }
              type="chat"
            />
          }
        />
        <Route
          path="/chat"
          element={
            <ProtectedRoute
              navPage="/chat/login"
              session={chatSession}
              loadingSession={loadingChatSession}
            >
              <AppShell
                theme={theme}
                onToggleTheme={() =>
                  setTheme((currentTheme) =>
                    currentTheme === "light" ? "dark" : "light",
                  )
                }
              >
                <ChatPage
                  chatSession={chatSession}
                  onLogout={handleLogoutChat}
                  onSessionExpired={() => setChatSession(null)}
                />
              </AppShell>
            </ProtectedRoute>
          }
        />
        <Route path="*" element={<Navigate to="/admin" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

function ProtectedRoute({ navPage, session, loadingSession, children }) {
  if (loadingSession) {
    return (
      <div className="flex min-h-screen items-center justify-center px-6 text-center text-copy">
        Verifica dell'accesso in corso...
      </div>
    );
  }

  if (!session) {
    return <Navigate to={navPage} replace />;
  }

  return children;
}

function useSession({ fetchSession }) {
  const [session, setSession] = useState(null);
  const [loadingSession, setLoadingSession] = useState(true);

  useEffect(() => {
    let isActive = true;

    async function caricaSessione() {
      setLoadingSession(true);
      try {
        const sessione = await fetchSession();
        if (isActive) {
          setSession(sessione);
        }
      } catch {
        if (isActive) {
          setSession(null);
        }
      } finally {
        if (isActive) {
          setLoadingSession(false);
        }
      }
    }

    void caricaSessione();

    return () => {
      isActive = false;
    };
  }, [fetchSession]);

  return { session, setSession, loadingSession };
}

export default App;
