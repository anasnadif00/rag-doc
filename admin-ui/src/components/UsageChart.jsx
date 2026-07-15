import { formatDay, formatNumber } from '../lib/dashboard.js'

function UsageChart({ rows, loading }) {
  if (loading) {
    return <div className="mt-4 text-[13px] text-muted">Caricamento dello storico in corso...</div>
  }

  if (!rows.length) {
    return (
      <div className="mt-4 rounded-xl border border-dashed border-divider bg-subtle p-4 text-[13px] text-muted">
        Nessun evento registrato nel periodo selezionato.
      </div>
    )
  }

  const maxMessages = Math.max(...rows.map((row) => row.messages_in + row.messages_out), 1)

  return (
    <div className="mt-4 overflow-x-auto">
      <div className="flex min-w-[620px] items-end gap-2.5">
        {rows.map((row) => {
          const totalMessages = row.messages_in + row.messages_out
          const height = Math.max(16, Math.round((totalMessages / maxMessages) * 150))
          return (
            <div key={row.usage_date} className="flex min-w-[58px] flex-1 flex-col items-center gap-2.5">
              <div
                className="usage-bar w-full rounded-t-xl border"
                style={{ height }}
              />
              <div className="space-y-1 text-center">
                <div className="text-[13px] text-ink">{formatNumber(totalMessages)}</div>
                <div className="text-[11px] uppercase tracking-[0.12em] text-muted">{formatDay(row.usage_date)}</div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default UsageChart
