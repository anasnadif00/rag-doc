export function QuickLink({ href, label }) {
  return (
    <a
      className="ghost-button inline-flex items-center rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-stone-100 transition hover:border-white/20 hover:bg-white/10"
      href={href}
      target="_blank"
      rel="noreferrer"
    >
      {label}
    </a>
  )
}

export function SectionCard({ eyebrow, title, subtitle, children, actions }) {
  return (
    <section className="app-panel rounded-[2rem] border border-white/10 bg-[linear-gradient(160deg,rgba(17,21,19,0.92),rgba(18,16,13,0.9))] p-5 shadow-[0_16px_60px_rgba(0,0,0,0.22)] lg:p-6">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="space-y-2">
          <div className="text-[11px] uppercase tracking-[0.28em] text-stone-400">{eyebrow}</div>
          <div>
            <h2 className="text-2xl text-stone-50">{title}</h2>
            <p className="mt-2 max-w-2xl text-sm leading-6 text-stone-300">{subtitle}</p>
          </div>
        </div>
        {actions}
      </div>
      <div className="mt-5">{children}</div>
    </section>
  )
}

export function SectionHeading({ title, subtitle }) {
  return (
    <div>
      <h3 className="text-lg text-stone-50">{title}</h3>
      <p className="mt-1 text-sm leading-6 text-stone-400">{subtitle}</p>
    </div>
  )
}

export function MetricCard({ label, value, detail, accent = 'copper' }) {
  const accentClasses = {
    copper: 'metric-card--primary',
    emerald: 'metric-card--success',
    rose: 'metric-card--danger',
    sky: 'metric-card--info',
    amber: 'metric-card--warning',
  }

  return (
    <div className={`metric-card rounded-[1.6rem] border p-5 ${accentClasses[accent] || accentClasses.copper}`}>
      <div className="text-[11px] uppercase tracking-[0.25em] text-stone-400">{label}</div>
      <div className="mt-3 text-3xl text-stone-50">{value}</div>
      <p className="mt-2 text-sm leading-6 text-stone-300">{detail}</p>
    </div>
  )
}

export function MetricMini({ label, value }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/[0.04] px-4 py-3">
      <div className="text-[11px] uppercase tracking-[0.22em] text-stone-400">{label}</div>
      <div className="mt-2 text-lg text-stone-50">{value}</div>
    </div>
  )
}

export function TextField({
  label,
  value,
  onChange,
  placeholder = '',
  help = '',
  type = 'text',
  autoComplete,
  disabled = false,
}) {
  return (
    <label className="block space-y-2">
      <span className="text-xs uppercase tracking-[0.18em] text-stone-400">{label}</span>
      <input
        type={type}
        value={value}
        placeholder={placeholder}
        autoComplete={autoComplete}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
        className="app-field w-full rounded-2xl border border-white/10 bg-white/[0.04] px-4 py-3 text-sm text-stone-100 outline-none transition placeholder:text-stone-500 focus:border-amber-300/40 focus:bg-white/[0.06]"
      />
      {help ? <span className="block text-xs leading-5 text-stone-500">{help}</span> : null}
    </label>
  )
}

export function TextArea({ label, value, onChange, placeholder = '', rows = 5, help = '', disabled = false }) {
  return (
    <label className="block space-y-2">
      <span className="text-xs uppercase tracking-[0.18em] text-stone-400">{label}</span>
      <textarea
        rows={rows}
        value={value}
        placeholder={placeholder}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
        className="app-field w-full rounded-2xl border border-white/10 bg-white/[0.04] px-4 py-3 text-sm text-stone-100 outline-none transition placeholder:text-stone-500 focus:border-amber-300/40 focus:bg-white/[0.06]"
      />
      {help ? <span className="block text-xs leading-5 text-stone-500">{help}</span> : null}
    </label>
  )
}

export function SelectField({ label, value, onChange, options, help = '', disabled = false }) {
  return (
    <label className="block space-y-2">
      <span className="text-xs uppercase tracking-[0.18em] text-stone-400">{label}</span>
      <select
        value={value}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
        className="app-field w-full rounded-2xl border border-white/10 bg-white/[0.04] px-4 py-3 text-sm text-stone-100 outline-none transition focus:border-amber-300/40 focus:bg-white/[0.06] disabled:cursor-not-allowed disabled:opacity-60"
      >
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
      {help ? <span className="block text-xs leading-5 text-stone-500">{help}</span> : null}
    </label>
  )
}

export function ToggleField({ label, checked, onChange }) {
  return (
    <label className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/[0.04] px-4 py-3">
      <span className="text-sm text-stone-200">{label}</span>
      <button
        type="button"
        onClick={() => onChange(!checked)}
        className={`relative inline-flex h-7 w-13 items-center rounded-full border transition ${
          checked ? 'border-emerald-300/30 bg-emerald-300/20' : 'border-white/10 bg-white/10'
        }`}
      >
        <span
          className={`h-5 w-10 rounded-full bg-stone-50 transition ${
            checked ? 'translate-x-3' : 'translate-x-1'
          }`}
        />
      </button>
    </label>
  )
}

export function PrimaryButton({ children, className = '', ...props }) {
  return (
    <button
      {...props}
      className={`primary-button inline-flex items-center justify-center rounded-full bg-amber-500 px-5 py-3 text-sm font-medium text-stone-950 transition hover:bg-amber-400 disabled:cursor-not-allowed disabled:opacity-60 ${className}`}
    >
      {children}
    </button>
  )
}

export function GhostButton({ children, className = '', ...props }) {
  return (
    <button
      {...props}
      className={`ghost-button inline-flex items-center justify-center rounded-full border border-white/10 bg-white/[0.04] px-4 py-3 text-sm text-stone-100 transition hover:border-white/20 hover:bg-white/[0.08] disabled:cursor-not-allowed disabled:opacity-60 ${className}`}
    >
      {children}
    </button>
  )
}

export function StatusBadge({ status }) {
  const label =
    {
      active: 'Attiva',
      suspended: 'Sospesa',
      quota_exceeded: 'Limite raggiunto',
    }[status] || status

  const tone =
    status === 'active'
      ? 'border-emerald-300/25 bg-emerald-300/10 text-emerald-100'
      : 'border-rose-300/25 bg-rose-300/10 text-rose-100'

  return <span className={`rounded-full border px-3 py-1 text-xs uppercase tracking-[0.18em] ${tone}`}>{label}</span>
}

export function MiniBadge({ label }) {
  return <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1">{label}</span>
}

export function EmptyState({ title, message }) {
  return (
    <div className="rounded-2xl border border-dashed border-white/10 bg-white/[0.03] px-5 py-10 text-center">
      <div className="text-lg text-stone-50">{title}</div>
      <p className="mx-auto mt-3 max-w-xl text-sm leading-6 text-stone-400">{message}</p>
    </div>
  )
}

export function ThemeToggle({ theme, onToggle }) {
  const isDark = theme === 'dark'
  const nextThemeLabel = isDark ? 'chiaro' : 'scuro'

  return (
    <button
      type="button"
      className="theme-toggle"
      onClick={onToggle}
      aria-label={`Attiva il tema ${nextThemeLabel}`}
      title={`Attiva il tema ${nextThemeLabel}`}
    >
      <span className="theme-toggle__icon" aria-hidden="true">
        {isDark ? (
          <svg viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="4" />
            <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.66 6.34l1.41-1.41" />
          </svg>
        ) : (
          <svg viewBox="0 0 24 24" fill="none">
            <path d="M20.2 15.1A8.7 8.7 0 0 1 8.9 3.8 8.7 8.7 0 1 0 20.2 15.1Z" />
          </svg>
        )}
      </span>
      <span className="theme-toggle__label">{isDark ? 'Tema chiaro' : 'Tema scuro'}</span>
    </button>
  )
}
