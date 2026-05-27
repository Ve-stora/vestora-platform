import { create } from 'zustand';
import { User, Stock, Portfolio, Alert } from '../types';

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  setUser: (user: User | null) => void;
  setToken: (token: string | null) => void;
  logout: () => void;
}

interface MarketState {
  stocks: Stock[];
  selectedStock: Stock | null;
  setStocks: (stocks: Stock[]) => void;
  setSelectedStock: (stock: Stock | null) => void;
}

interface PortfolioState {
  portfolios: Portfolio[];
  selectedPortfolio: Portfolio | null;
  setPortfolios: (portfolios: Portfolio[]) => void;
  setSelectedPortfolio: (portfolio: Portfolio | null) => void;
}

interface AlertState {
  alerts: Alert[];
  setAlerts: (alerts: Alert[]) => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  token: localStorage.getItem('access_token'),
  isAuthenticated: !!localStorage.getItem('access_token'),
  setUser: (user) => set({ user }),
  setToken: (token) => {
    if (token) {
      localStorage.setItem('access_token', token);
    } else {
      localStorage.removeItem('access_token');
    }
    set({ token, isAuthenticated: !!token });
  },
  logout: () => {
    localStorage.removeItem('access_token');
    set({ user: null, token: null, isAuthenticated: false });
  },
}));

export const useMarketStore = create<MarketState>((set) => ({
  stocks: [],
  selectedStock: null,
  setStocks: (stocks) => set({ stocks }),
  setSelectedStock: (stock) => set({ selectedStock: stock }),
}));

export const usePortfolioStore = create<PortfolioState>((set) => ({
  portfolios: [],
  selectedPortfolio: null,
  setPortfolios: (portfolios) => set({ portfolios }),
  setSelectedPortfolio: (portfolio) => set({ selectedPortfolio: portfolio }),
}));

export const useAlertStore = create<AlertState>((set) => ({
  alerts: [],
  setAlerts: (alerts) => set({ alerts }),
}));