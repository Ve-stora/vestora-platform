import React, { useEffect, useState } from 'react'
import client from '../api/client'

export function MarketOverview() {
  const [stocks, setStocks] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchStocks = async () => {
      try {
        const response = await client.get('/market/stocks')
        setStocks(response.data)
      } catch (error) {
        console.error('Error fetching stocks:', error)
      } finally {
        setLoading(false)
      }
    }
    fetchStocks()
  }, [])

  if (loading) return <div className="p-6">Loading market data...</div>

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">Market Overview</h1>
      <div className="grid gap-4">
        {stocks.map((stock: any) => (
          <div key={stock.id} className="bg-white p-4 rounded shadow">
            <h3 className="font-bold">{stock.symbol}</h3>
            <p>{stock.name}</p>
            <p className="text-lg text-blue-600">UGX {stock.price}</p>
          </div>
        ))}
      </div>
    </div>
  )
}