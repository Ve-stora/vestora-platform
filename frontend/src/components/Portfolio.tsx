import React, { useEffect, useState } from 'react';
import { usePortfolioStore } from '../store/useStore';
import { Portfolio as PortfolioType } from '../types';
import client from '../api/client';

export const Portfolio: React.FC = () => {
  const { portfolios, selectedPortfolio, setPortfolios, setSelectedPortfolio } = usePortfolioStore();
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({ name: '', description: '' });

  useEffect(() => {
    const fetchPortfolios = async () => {
      try {
        const response = await client.get('/portfolio/');
        setPortfolios(response.data);
      } catch (error) {
        console.error('Failed to fetch portfolios:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolios();
  }, [setPortfolios]);

  const handleCreatePortfolio = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await client.post('/portfolio/', formData);
      setPortfolios([...portfolios, response.data]);
      setFormData({ name: '', description: '' });
      setShowForm(false);
    } catch (error) {
      console.error('Failed to create portfolio:', error);
    }
  };

  const handleSelectPortfolio = (portfolio: PortfolioType) => {
    setSelectedPortfolio(portfolio);
  };

  if (loading) return <div className="p-8">Loading portfolios...</div>;

  return (
    <div className="p-8 bg-gradient-to-br from-slate-50 to-slate-100 min-h-screen">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold text-slate-900">My Portfolios</h1>
        <button
          onClick={() => setShowForm(!showForm)}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
        >
          {showForm ? 'Cancel' : 'New Portfolio'}
        </button>
      </div>

      {showForm && (
        <form
          onSubmit={handleCreatePortfolio}
          className="bg-white p-6 rounded-lg shadow mb-8"
        >
          <div className="space-y-4">
            <input
              type="text"
              placeholder="Portfolio Name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
            <textarea
              placeholder="Description"
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="submit"
              className="w-full bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition"
            >
              Create Portfolio
            </button>
          </div>
        </form>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {portfolios.map((portfolio) => (
          <div
            key={portfolio.id}
            onClick={() => handleSelectPortfolio(portfolio)}
            className={`p-6 rounded-lg shadow cursor-pointer transition ${
              selectedPortfolio?.id === portfolio.id
                ? 'bg-blue-50 border-2 border-blue-500'
                : 'bg-white hover:shadow-lg'
            }`}
          >
            <h3 className="text-xl font-bold text-slate-900">{portfolio.name}</h3>
            <p className="text-gray-600">{portfolio.description}</p>
            <div className="mt-4 space-y-2">
              <p className="text-sm text-gray-600">
                Total Value: <span className="font-bold text-slate-900">UGX {portfolio.total_value}</span>
              </p>
              <p className="text-sm text-gray-600">
                Invested: <span className="font-bold text-slate-900">UGX {portfolio.total_invested}</span>
              </p>
            </div>
          </div>
        ))}
      </div>

      {portfolios.length === 0 && !showForm && (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <p className="text-gray-600 mb-4">No portfolios yet</p>
          <button
            onClick={() => setShowForm(true)}
            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
          >
            Create Your First Portfolio
          </button>
        </div>
      )}
    </div>
  );
};