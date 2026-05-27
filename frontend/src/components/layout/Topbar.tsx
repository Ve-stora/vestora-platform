import { useAuthStore } from '../../store/authStore'
import { LogOut } from 'lucide-react'

export default function Topbar() {
  const logout = useAuthStore(s => s.logout)
  return (
    <header className="h-16 border-b border-gray-100 bg-white flex items-center justify-between px-6">
      <p className="text-sm text-gray-500">Uganda Securities Exchange — Live Market Platform</p>
      <button onClick={logout} className="flex items-center gap-2 text-sm text-gray-500 hover:text-gray-800">
        <LogOut size={16} /> Logout
      </button>
    </header>
  )
}
