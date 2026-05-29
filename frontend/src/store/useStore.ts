import { create } from 'zustand'

interface AuthStore {
  isAuthenticated: boolean
  user: any
  token: string | null
  login: (email: string, password: string) => Promise<void>
  register: (email: string, username: string, password: string, fullName: string) => Promise<void>
  logout: () => void
}

export const useAuthStore = create<AuthStore>((set) => ({
  isAuthenticated: !!localStorage.getItem('token'),
  user: localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')!) : null,
  token: localStorage.getItem('token'),

  login: async (email: string, password: string) => {
    try {
      const response = await fetch('http://localhost:8000/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      })
      const data = await response.json()
      localStorage.setItem('token', data.access_token)
      localStorage.setItem('user', JSON.stringify({ email }))
      set({ isAuthenticated: true, token: data.access_token, user: { email } })
    } catch (error) {
      console.error('Login failed:', error)
      throw error
    }
  },

  register: async (email: string, username: string, password: string, fullName: string) => {
    try {
      const response = await fetch('http://localhost:8000/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, username, password, full_name: fullName })
      })
      const data = await response.json()
      localStorage.setItem('token', data.access_token || 'temp-token')
      localStorage.setItem('user', JSON.stringify(data))
      set({ isAuthenticated: true, user: data })
    } catch (error) {
      console.error('Registration failed:', error)
      throw error
    }
  },

  logout: () => {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    set({ isAuthenticated: false, user: null, token: null })
  }
}))