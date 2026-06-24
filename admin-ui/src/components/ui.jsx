export function QuickLink({ href, label }) {
  return (
    <a
      className="ghost-button inline-flex items-center rounded-full border px-4 py-2 text-sm transition"
      href={href}
      target="_blank"
      rel="noreferrer"
    >
      {label}
    </a>
  );
}

export function SectionCard({ eyebrow, title, subtitle, children, actions }) {
  return (
    <section className="app-panel rounded-[2rem] border p-5 lg:p-6">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="space-y-2">
          <div className="text-[11px] uppercase tracking-[0.28em] text-muted">
            {eyebrow}
          </div>
          <div>
            <h2 className="text-2xl text-ink">{title}</h2>
            <p className="mt-2 max-w-2xl text-sm leading-6 text-copy">
              {subtitle}
            </p>
          </div>
        </div>
        {actions}
      </div>
      <div className="mt-5">{children}</div>
    </section>
  );
}

export function SectionHeading({ title, subtitle }) {
  return (
    <div>
      <h3 className="text-lg text-ink">{title}</h3>
      <p className="mt-1 text-sm leading-6 text-muted">{subtitle}</p>
    </div>
  );
}

export function MetricCard({ label, value, detail, accent = "primary" }) {
  const accentClasses = {
    primary: "metric-card--primary",
    success: "metric-card--success",
    danger: "metric-card--danger",
    info: "metric-card--info",
    neutral: "metric-card--warning",
  };

  return (
    <div
      className={`metric-card rounded-[1.6rem] border p-5 ${accentClasses[accent] || accentClasses.primary}`}
    >
      <div className="text-[11px] uppercase tracking-[0.25em] text-muted">
        {label}
      </div>
      <div className="mt-3 text-3xl text-ink">{value}</div>
      <p className="mt-2 text-sm leading-6 text-copy">{detail}</p>
    </div>
  );
}

export function MetricMini({ label, value }) {
  return (
    <div className="rounded-2xl border border-divider bg-subtle px-4 py-3">
      <div className="text-[11px] uppercase tracking-[0.22em] text-muted">
        {label}
      </div>
      <div className="mt-2 text-lg text-ink">{value}</div>
    </div>
  );
}

export function TextField({
  label,
  value,
  onChange,
  placeholder = "",
  help = "",
  type = "text",
  autoComplete,
  disabled = false,
}) {
  return (
    <label className="block space-y-2">
      <span className="text-xs uppercase tracking-[0.18em] text-muted">
        {label}
      </span>
      <input
        type={type}
        value={value}
        placeholder={placeholder}
        autoComplete={autoComplete}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
        className="app-field w-full rounded-2xl border px-4 py-3 text-sm outline-none transition"
      />
      {help ? (
        <span className="block text-xs leading-5 text-faint">{help}</span>
      ) : null}
    </label>
  );
}

export function TextArea({
  label,
  value,
  onChange,
  placeholder = "",
  rows = 5,
  help = "",
  disabled = false,
}) {
  return (
    <label className="block space-y-2">
      <span className="mb-2 text-xs uppercase tracking-[0.18em] text-muted">
        {label}
      </span>
      <textarea
        rows={rows}
        value={value}
        placeholder={placeholder}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
        className="app-field w-full rounded-2xl border px-4 py-3 text-sm outline-none transition"
      />
      {help ? (
        <span className="block text-xs leading-5 text-faint">{help}</span>
      ) : null}
    </label>
  );
}

export function SelectField({
  label,
  value,
  onChange,
  options,
  help = "",
  disabled = false,
}) {
  return (
    <label className="block space-y-2">
      <span className="text-xs uppercase tracking-[0.18em] text-muted">
        {label}
      </span>
      <select
        value={value}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
        className="app-field w-full rounded-2xl border px-4 py-3 text-sm outline-none transition disabled:cursor-not-allowed disabled:opacity-60"
      >
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
      {help ? (
        <span className="block text-xs leading-5 text-faint">{help}</span>
      ) : null}
    </label>
  );
}

export function ToggleField({ label, checked, onChange }) {
  return (
    <label className="flex items-center justify-between rounded-2xl border border-divider bg-subtle px-4 py-3">
      <span className="text-sm text-copy">{label}</span>
      <button
        type="button"
        role="switch"
        aria-checked={checked}
        onClick={() => onChange(!checked)}
        className={`relative inline-flex h-7 w-12 items-center rounded-full border transition ${
          checked ? "border-accent bg-accent" : "border-divider bg-inset"
        }`}
      >
        <span
          className={`h-5 w-5 rounded-full bg-white shadow-sm transition ${
            checked ? "translate-x-6" : "translate-x-1"
          }`}
        />
      </button>
    </label>
  );
}

export function PrimaryButton({ children, className = "", ...props }) {
  return (
    <button
      {...props}
      className={`primary-button inline-flex items-center justify-center rounded-full px-5 py-3 text-sm font-medium transition disabled:cursor-not-allowed disabled:opacity-60 ${className}`}
    >
      {children}
    </button>
  );
}

export function GhostButton({ children, className = "", ...props }) {
  return (
    <button
      {...props}
      className={`ghost-button inline-flex items-center justify-center rounded-full border px-4 py-3 text-sm transition disabled:cursor-not-allowed disabled:opacity-60 ${className}`}
    >
      {children}
    </button>
  );
}

export function StatusBadge({ status }) {
  const label =
    {
      active: "Attiva",
      suspended: "Sospesa",
      quota_exceeded: "Limite raggiunto",
    }[status] || status;

  const tone =
    status === "active"
      ? "border-success-border bg-success-soft text-success"
      : "border-danger-border bg-danger-soft text-danger";

  return (
    <span
      className={`rounded-full border px-3 py-1 text-xs uppercase tracking-[0.18em] ${tone}`}
    >
      {label}
    </span>
  );
}

export function MiniBadge({ label }) {
  return (
    <span className="rounded-full border border-divider bg-subtle px-3 py-1">
      {label}
    </span>
  );
}

export function EmptyState({ title, message }) {
  return (
    <div className="rounded-2xl border border-dashed border-divider bg-subtle px-5 py-10 text-center">
      <div className="text-lg text-ink">{title}</div>
      <p className="mx-auto mt-3 max-w-xl text-sm leading-6 text-muted">
        {message}
      </p>
    </div>
  );
}

export function ThemeToggle({ theme, onToggle }) {
  const isDark = theme === "dark";
  const nextThemeLabel = isDark ? "chiaro" : "scuro";

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
      <span className="theme-toggle__label">
        {isDark ? "Tema chiaro" : "Tema scuro"}
      </span>
    </button>
  );
}
