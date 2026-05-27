import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { useAuthStore } from '../store/authStore'
import api from '../api/client'

export default function Login() {
  const [email, setEmail]     = useState('')
  const [password, setPassword] = useState('')
  const [error, setError]     = useState('')
  const setAuth   = useAuthStore(s => s.setAuth)
  const navigate  = useNavigate()

  const submit = async (e: React.FormEvent) => {
    e.preventDefault(); setError('')
    try {
      const form = new FormData()
      form.append('username', email); form.append('password', password)
      const { data } = await api.post('/auth/login', form)
      setAuth(data.access_token, 1)
      navigate('/')
    } catch { setError('Invalid email or password') }
  }

  return (
    <div className="min-h-screen bg-surface flex items-center justify-center">
      <div className="card w-full max-w-sm">
        <h1 className="font-display font-bold text-2xl text-primary mb-1">USE Insight</h1>
        <p className="text-gray-500 text-sm mb-6">Sign in to your account</p>
        {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
        <form onSubmit={submit} className="space-y-4">
          <input type="email" value={email} onChange={e => setEmail(e.target.value)}
            placeholder="Email" required
            className="w-full border border-gray-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/30" />
          <input type="password" value={password} onChange={e => setPassword(e.target.value)}
            placeholder="Password" required
            className="w-full border border-gray-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/30" />
          <button type="submit" className="btn-primary w-full text-center">Sign In</button>
        </form>
        <p className="text-center text-sm text-gray-500 mt-4">
          No account? <Link to="/register" className="text-primary font-medium">Register</Link>
        </p>
      </div>
    </div>
  )
}
