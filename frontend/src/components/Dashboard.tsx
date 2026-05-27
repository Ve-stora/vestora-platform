import React, { useEffect, useState } from 'react';
import { useMarketStore, usePortfolioStore } from '../store/useStore';
import { Stock, Portfolio } from '../types';
import client from '../api/client';

export const Dashboard: React.FC = () => {
  const { stocks, setStocks } = useMarketStore();
  const { portfolios } = usePortfolioStore();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMarketData = async () => {
      try {
        const response = await client.get('/market/stocks');
        setStocks(response.data);
      } catch (error) {
        console.error('Failed to fetch stocks:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchMarketData();
  }, [setStocks]);

  if (loading) return <div className="p-8">Loading market data...</div>;

  return (
    <div className="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-screen">
      <h1 className="text-4xl font-bold text-slate-900 mb-8">Vestora Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow">
          <p className="text-gray-600 text-sm">Total Portfolios</p>
          <p className="text-3xl font-bold text-slate-900">{portfolios.length}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <p className="text-gray-600 text-sm">Active Stocks</p>
          <p className="text-3xl font-bold text-slate-900">{stocks.length}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <p className="text-gray-600 text-sm">Market Status</p>
          <p className="text-2xl font-bold text-green-600">Open</p>
        </div>
      </div>

      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-2xl font-bold text-slate-900 mb-4">Market Overview</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {stocks.slice(0, 6).map((stock: Stock) => (
            <div key={stock.id} className="border-l-4 border-blue-500 pl-4 py-2">
              <p className="font-semibold text-slate-900">{stock.symbol}</p>
              <p className="text-gray-600">{stock.name}</p>
              <p className="text-lg font-bold text-blue-600">UGX {stock.price}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};