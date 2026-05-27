import { useQuery } from '@tanstack/react-query'
import { getCompanies } from '../../api/market'
import { TrendingUp, TrendingDown } from 'lucide-react'

export default function MarketTable() {
  const { data: companies = [], isLoading } = useQuery({ queryKey: ['companies'], queryFn: getCompanies })
  if (isLoading) return <div className="text-center py-8 text-gray-400">Loading market data...</div>
  return (
    <div className="card overflow-hidden p-0">
      <table className="w-full text-sm">
        <thead className="bg-gray-50 border-b border-gray-100">
          <tr>
            {['Symbol','Company','Sector','Market Cap','Change'].map(h => (
              <th key={h} className="text-left px-4 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wide">{h}</th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-50">
          {companies.map((c: any) => (
            <tr key={c.id} className="hover:bg-gray-50 transition-colors">
              <td className="px-4 py-3 font-semibold text-primary">{c.symbol}</td>
              <td className="px-4 py-3 font-medium">{c.name}</td>
              <td className="px-4 py-3 text-gray-500">{c.sector || '—'}</td>
              <td className="px-4 py-3">{c.market_cap ? `UGX ${c.market_cap.toLocaleString()}` : '—'}</td>
              <td className="px-4 py-3">
                <span className="flex items-center gap-1 text-green-600">
                  <TrendingUp size={14} /> 0.00%
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {companies.length === 0 && (
        <p className="text-center text-gray-400 py-8">No companies listed yet. Seed the database to get started.</p>
      )}
    </div>
  )
}
