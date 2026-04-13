import { formatDay, formatNumber } from '../lib/dashboard.js'

function UsageChart({ rows, loading }) {
  if (loading) {
    return <div className="mt-6 text-sm text-stone-400">Caricamento dello storico in corso...</div>
  }

  if (!rows.length) {
    return (
      <div className="mt-6 rounded-2xl border border-dashed border-white/10 bg-white/[0.03] p-5 text-sm text-stone-400">
        Nessun evento registrato nel periodo selezionato.
      </div>
    )
  }

  const maxMessages = Math.max(...rows.map((row) => row.messages_in + row.messages_out), 1)

  return (
    <div className="mt-6 overflow-x-auto">
      <div className="flex min-w-[640px] items-end gap-3">
        {rows.map((row) => {
          const totalMessages = row.messages_in + row.messages_out
          const height = Math.max(18, Math.round((totalMessages / maxMessages) * 180))
          return (
            <div key={row.usage_date} className="flex min-w-[64px] flex-1 flex-col items-center gap-3">
              <div
                className="w-full rounded-t-[1.25rem] border border-amber-300/15 bg-[linear-gradient(180deg,rgba(251,191,36,0.72),rgba(217,119,6,0.22))]"
                style={{ height }}
              />
              <div className="space-y-1 text-center">
                <div className="text-sm text-stone-50">{formatNumber(totalMessages)}</div>
                <div className="text-xs uppercase tracking-[0.16em] text-stone-400">{formatDay(row.usage_date)}</div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default UsageChart
