export interface Company {
  id: number; symbol: string; name: string; sector: string; market_cap: number
}
export interface Holding {
  id: number; company_id: number; shares: number; buy_price: number; buy_date: string
}
export interface Portfolio {
  id: number; name: string; holdings: Holding[]
}
export interface Alert {
  id: number; company_id: number; alert_type: string; threshold: number; is_active: boolean
}
export interface EducationModule {
  id: number; title: string; level: string; description: string
}
