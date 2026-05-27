interface Props {
  symbol: string; shares: number; buyPrice: number; currentPrice: number
}
export default function HoldingCard({ symbol, shares, buyPrice, currentPrice }: Props) {
  const value    = shares * currentPrice
  const gain     = (currentPrice - buyPrice) * shares
  const gainPct  = ((currentPrice - buyPrice) / buyPrice) * 100
  const positive = gain >= 0
  return (
    <div className="card flex justify-between items-center">
      <div>
        <p className="font-display font-bold text-primary text-lg">{symbol}</p>
        <p className="text-sm text-gray-500">{shares} shares @ UGX {buyPrice.toLocaleString()}</p>
      </div>
      <div className="text-right">
        <p className="font-semibold">UGX {value.toLocaleString()}</p>
        <p className={`text-sm ${positive ? 'text-green-600' : 'text-red-500'}`}>
          {positive ? '+' : ''}{gainPct.toFixed(2)}%
        </p>
      </div>
    </div>
  )
}
