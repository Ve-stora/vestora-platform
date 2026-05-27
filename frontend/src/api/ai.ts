import api from './client'
export const askAI = (question: string, context = '') =>
  api.post('/ai/ask', { question, context }).then(r => r.data)
