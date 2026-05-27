import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import api from '../api/client'

export default function Register() {
  const [form, setForm] = useState({ email: '', full_name: '', password: '' })
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const submit = async (e: React.FormEvent) => {
    e.preventDefault(); setError('')
    try {
      await api.post('/auth/register', form)
      navigate('/login')
    } catch (err: any) { setError(err.response?.data?.detail || 'Registration failed') }
  }

  return (
    <div className="min-h-screen bg-surface flex items-center justify-center">
      <div className="card w-full max-w-sm">
        <h1 className="font-display font-bold text-2xl text-primary mb-1">Create Account</h1>
        <p className="text-gray-500 text-sm mb-6">Join USE Insight today</p>
        {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
        <form onSubmit={submit} className="space-y-4">
          {(['full_name','email','password'] as const).map(f => (
            <input key={f} type={f === 'password' ? 'password' : f === 'email' ? 'email' : 'text'}
              placeholder={f === 'full_name' ? 'Full Name' : f === 'email' ? 'Email' : 'Password'}
              value={form[f]} onChange={e => setForm(p => ({ ...p, [f]: e.target.value }))} required
              className="w-full border border-gray-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/30" />
          ))}
          <button type="submit" className="btn-primary w-full text-center">Create Account</button>
        </form>
        <p className="text-center text-sm text-gray-500 mt-4">
          Have an account? <Link to="/login" className="text-primary font-medium">Sign In</Link>
        </p>
      </div>
    </div>
  )
}
