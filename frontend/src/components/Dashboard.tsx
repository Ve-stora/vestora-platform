import React from 'react'
import { useAuthStore } from '../store/useStore'
import { TrendingUp, LogOut } from 'lucide-react'

export function Dashboard() {
  const logout = useAuthStore((state) => state.logout)
  const user = useAuthStore((state) => state.user)

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <TrendingUp className="text-blue-600" />
            <h1 className="text-2xl font-bold">Vestora</h1>
          </div>
          <button
            onClick={logout}
            className="flex items-center gap-2 bg-red-600 text-white px-4 py-2 rounded"
          >
            <LogOut size={18} /> Logout
          </button>
        </div>
      </nav>
      <div className="max-w-7xl mx-auto px-4 py-8">
        <h2 className="text-3xl font-bold mb-4">Welcome, {user?.email}!</h2>
        <p className="text-gray-600">Your investment intelligence platform for Uganda's capital markets</p>
      </div>
    </div>
  )
}