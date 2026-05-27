import api from './client'
export const getPortfolio = (userId: number) => api.get(`/portfolio/${userId}`).then(r => r.data)
export const addHolding   = (userId: number, data: object) => api.post(`/portfolio/${userId}/holdings`, data).then(r => r.data)
