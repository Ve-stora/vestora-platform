import React, { useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { useMarketStore } from '../store/useStore';
import client from '../api/client';

export const MarketOverview: React.FC = () => {
  const { stocks, setStocks } = useMarketStore();
  const [loading, setLoading] = React.useState(true);

  useEffect(() => {
    const fetchMarketData = async () => {
      try {
        const response = await client.get('/market/market-overview');
        setStocks(response.data.stocks || []);
      } catch (error) {
        console.error('Failed to fetch market overview:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchMarketData();
  }, [setStocks]);

  if (loading) return <div className="p-8">Loading market data...</div>;

  const chartData = stocks.slice(0, 10).map((stock) => ({
    name: stock.symbol,
    price: stock.price,
    volume: stock.volume || 0,
  }));

  return (
    <div className="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-screen">
      <h1 className="text-4xl font-bold text-slate-900 mb-8">Market Overview</h1>

      <div className="bg-white p-6 rounded-lg shadow mb-8">
        <h2 className="text-2xl font-bold text-slate-900 mb-4">Stock Prices</h2>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="price" stroke="#2563eb" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-2xl font-bold text-slate-900 mb-4">Stock Details</h2>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-gray-300">
                <th className="text-left py-2 px-4 font-semibold text-slate-900">Symbol</th>
                <th className="text-left py-2 px-4 font-semibold text-slate-900">Name</th>
                <th className="text-right py-2 px-4 font-semibold text-slate-900">Price</th>
                <th className="text-right py-2 px-4 font-semibold text-slate-900">PE Ratio</th>
                <th className="text-right py-2 px-4 font-semibold text-slate-900">Dividend Yield</th>
              </tr>
            </thead>
            <tbody>
              {stocks.map((stock) => (
                <tr key={stock.id} className="border-b border-gray-200 hover:bg-gray-50">
                  <td className="py-3 px-4 font-semibold text-slate-900">{stock.symbol}</td>
                  <td className="py-3 px-4 text-gray-600">{stock.name}</td>
                  <td className="py-3 px-4 text-right font-semibold text-slate-900">
                    UGX {stock.price.toFixed(2)}
                  </td>
                  <td className="py-3 px-4 text-right text-gray-600">
                    {stock.pe_ratio ? stock.pe_ratio.toFixed(2) : 'N/A'}
                  </td>
                  <td className="py-3 px-4 text-right text-gray-600">
                    {stock.dividend_yield ? `${stock.dividend_yield.toFixed(2)}%` : 'N/A'}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};