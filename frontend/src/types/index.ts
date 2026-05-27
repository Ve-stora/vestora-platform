export interface User {
  id: number;
  email: string;
  username: string;
  full_name?: string;
  is_active: boolean;
  created_at: string;
}

export interface Stock {
  id: number;
  symbol: string;
  name: string;
  price: number;
  opening_price?: number;
  high_price?: number;
  low_price?: number;
  volume?: number;
  market_cap?: number;
  pe_ratio?: number;
  dividend_yield?: number;
  sector?: string;
  last_updated: string;
}

export interface Portfolio {
  id: number;
  user_id: number;
  name: string;
  description?: string;
  total_value: number;
  total_invested: number;
  created_at: string;
  updated_at: string;
}

export interface PortfolioHolding {
  id: number;
  portfolio_id: number;
  stock_id: number;
  quantity: number;
  purchase_price: number;
  current_value: number;
  purchase_date: string;
}

export interface Alert {
  id: number;
  user_id: number;
  stock_id: number;
  alert_type: string;
  target_value?: number;
  is_active: boolean;
  message?: string;
  created_at: string;
  triggered_at?: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface ChatMessage {
  user_message: string;
  assistant_message: string;
}