import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";

import { PrimaryButton, TextField, ThemeToggle } from "../components/ui.jsx";

function LoginPage({
  session,
  loadingSession,
  onLogin,
  theme,
  onToggleTheme,
  type,
}) {
  const navigate = useNavigate();
  const isAdmin = type === "admin";
  const targetPath = isAdmin ? "/admin" : "/chat";
  const [tenantCode, setTenantCode] = useState("");
  const [username, setUsername] = useState(isAdmin ? "admin" : "");
  const [password, setPassword] = useState("");
  const [errore, setErrore] = useState("");
  const [accessoInCorso, setAccessoInCorso] = useState(false);

  if (loadingSession) {
    return (
      <div className="flex min-h-screen items-center justify-center px-6 text-center text-copy">
        Verifica dell'accesso in corso...
      </div>
    );
  }

  if (session) {
    return <Navigate to={targetPath} replace />;
  }

  async function handleSubmit(event) {
    event.preventDefault();

    const cleanedTenantCode = tenantCode.trim();
    const cleanedUsername = username.trim();
    if (!cleanedUsername || !password || (!isAdmin && !cleanedTenantCode)) {
      setErrore("Completa tutti i campi richiesti.");
      return;
    }

    setAccessoInCorso(true);
    setErrore("");

    try {
      const credentials = {
        username: cleanedUsername,
        password,
      };

      if (!isAdmin) {
        credentials.tenant_code = cleanedTenantCode;
      }

      await onLogin(credentials);
      navigate(targetPath, { replace: true });
    } catch (error) {
      setErrore(error.message || "Non e stato possibile completare l'accesso.");
    } finally {
      setAccessoInCorso(false);
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
            Accesso {isAdmin ? "Amministratore" : "Chat Mia"}
          </div>
          <h1 className="text-4xl leading-tight text-ink">{isAdmin ? "Area amministratore" : "Entra nella chat"}</h1>
          <p className="text-sm leading-7 text-copy">
            {isAdmin ? "Inserisci le credenziali di amministrazione." : "Inserisci codice azienda e credenziali utente."}
          </p>
        </div>

        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          {!isAdmin ? (
            <TextField
              label="Codice azienda"
              value={tenantCode}
              placeholder="acme"
              autoComplete="organization"
              onChange={setTenantCode}
            />
          ) : null}
          <TextField
            label="Utente"
            value={username}
            placeholder={isAdmin ? "admin" : "mario.rossi"}
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

          <PrimaryButton
            type="submit"
            className="w-full"
            disabled={accessoInCorso}
          >
            {accessoInCorso ? "Accesso in corso..." : "Accedi"}
          </PrimaryButton>
        </form>
      </div>
    </div>
  );
}

export default LoginPage;
