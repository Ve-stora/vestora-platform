import MarketTable from '../components/market/MarketTable'

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="font-display font-bold text-2xl text-primary">Market Overview</h2>
        <p className="text-gray-500 text-sm mt-1">Uganda Securities Exchange — Live Data</p>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {[
          { label: 'Total Market Cap', value: 'UGX —', sub: 'Listed Companies' },
          { label: 'Daily Volume',     value: '—',    sub: 'Shares traded today' },
          { label: 'Listed Companies', value: '—',    sub: 'Across all sectors' },
        ].map(s => (
          <div key={s.label} className="card">
            <p className="text-xs text-gray-400 uppercase tracking-wide">{s.label}</p>
            <p className="font-display font-bold text-2xl text-primary mt-1">{s.value}</p>
            <p className="text-xs text-gray-400 mt-1">{s.sub}</p>
          </div>
        ))}
      </div>
      <MarketTable />
    </div>
  )
}
