import api from './client'
export const getModules = () => api.get('/education/modules').then(r => r.data)
export const getModule  = (id: number) => api.get(`/education/modules/${id}`).then(r => r.data)
