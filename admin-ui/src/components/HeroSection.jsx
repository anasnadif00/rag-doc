import { GhostButton, SectionCard } from './ui.jsx'

function HeroSection({ adminSession, onLogout, logoutInCorso }) {
  return (
    <header className="app-hero overflow-hidden rounded-[2rem] border">
      <div className="grid gap-6 px-5 py-6 lg:grid-cols-[1.2fr_0.8fr] lg:px-8 lg:py-8">
        <div className="space-y-5">
          <div className="brand-badge inline-flex items-center rounded-full border px-3 py-1 text-[11px] uppercase tracking-[0.28em]">
            Pannello di controllo
          </div>
          <div className="max-w-3xl space-y-3">
            <h1 className="text-4xl leading-tight text-ink sm:text-5xl">
              Gestisci aziende, contenuti e accessi da un unico spazio.
            </h1>
            <p className="max-w-2xl text-sm leading-7 text-copy sm:text-base">
              Qui puoi controllare lo stato del servizio, aggiornare i materiali di supporto e organizzare le aziende
              in modo semplice e ordinato.
            </p>
          </div>
        </div>

        <SectionCard
          eyebrow="Profilo attivo"
          title={adminSession?.display_name || 'Amministratore'}
          subtitle="L'accesso al pannello e protetto. Quando hai finito puoi uscire in sicurezza con un solo clic."
        >
          <div className="space-y-4">
            <div className="rounded-2xl border border-divider bg-subtle px-4 py-4">
              <div className="text-xs uppercase tracking-[0.18em] text-muted">Utente</div>
              <div className="mt-2 text-lg text-ink">{adminSession?.username || 'admin'}</div>
            </div>
            <div className="flex flex-wrap items-center gap-3">
              <div className="rounded-full border border-success-border bg-success-soft px-4 py-3 text-sm text-success">
                Accesso confermato
              </div>
              <GhostButton type="button" onClick={onLogout} disabled={logoutInCorso}>
                {logoutInCorso ? 'Uscita in corso...' : 'Esci'}
              </GhostButton>
            </div>
          </div>
        </SectionCard>
      </div>
    </header>
  )
}

export default HeroSection
