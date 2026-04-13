import { GhostButton, SectionCard } from './ui.jsx'

function HeroSection({ adminSession, onLogout, logoutInCorso }) {
  return (
    <header className="overflow-hidden rounded-[2rem] border border-white/10 bg-[linear-gradient(135deg,rgba(14,20,18,0.94),rgba(27,20,15,0.92))] shadow-[0_24px_80px_rgba(0,0,0,0.35)]">
      <div className="grid gap-6 px-5 py-6 lg:grid-cols-[1.2fr_0.8fr] lg:px-8 lg:py-8">
        <div className="space-y-5">
          <div className="inline-flex items-center rounded-full border border-amber-500/30 bg-amber-500/10 px-3 py-1 text-[11px] uppercase tracking-[0.28em] text-amber-200">
            Pannello di controllo
          </div>
          <div className="max-w-3xl space-y-3">
            <h1 className="text-4xl leading-tight text-stone-50 sm:text-5xl">
              Gestisci aziende, contenuti e accessi da un unico spazio.
            </h1>
            <p className="max-w-2xl text-sm leading-7 text-stone-300 sm:text-base">
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
            <div className="rounded-2xl border border-white/10 bg-white/[0.04] px-4 py-4">
              <div className="text-xs uppercase tracking-[0.18em] text-stone-400">Utente</div>
              <div className="mt-2 text-lg text-stone-50">{adminSession?.username || 'admin'}</div>
            </div>
            <div className="flex flex-wrap items-center gap-3">
              <div className="rounded-full border border-emerald-300/20 bg-emerald-300/10 px-4 py-3 text-sm text-emerald-50">
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
