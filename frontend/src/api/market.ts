import api from './client'
export const getCompanies  = () => api.get('/market/companies').then(r => r.data)
export const getCompany    = (symbol: string) => api.get(`/market/companies/${symbol}`).then(r => r.data)
export const getPrices     = (companyId: number) => api.get(`/market/prices/${companyId}`).then(r => r.data)
