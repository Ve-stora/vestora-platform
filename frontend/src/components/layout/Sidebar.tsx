import { NavLink } from 'react-router-dom'
import { BarChart2, BookOpen, BellRing, Briefcase, MessageSquare } from 'lucide-react'

const links = [
  { to: '/',           icon: BarChart2,    label: 'Market' },
  { to: '/portfolio',  icon: Briefcase,    label: 'Portfolio' },
  { to: '/education',  icon: BookOpen,     label: 'Education' },
  { to: '/ai',         icon: MessageSquare,label: 'AI Assistant' },
  { to: '/alerts',     icon: BellRing,     label: 'Alerts' },
]

export default function Sidebar() {
  return (
    <aside className="w-64 bg-primary text-white flex flex-col py-6 px-4 shrink-0">
      <div className="mb-8 px-2">
        <h1 className="font-display font-bold text-2xl">USE Insight</h1>
        <p className="text-primary-pale text-xs mt-1">Uganda Capital Markets</p>
      </div>
      <nav className="flex-1 space-y-1">
        {links.map(({ to, icon: Icon, label }) => (
          <NavLink key={to} to={to} end={to === '/'}
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors
               ${isActive ? 'bg-primary-light text-white' : 'text-primary-pale hover:text-white hover:bg-primary-light/50'}`}>
            <Icon size={18} />
            {label}
          </NavLink>
        ))}
      </nav>
    </aside>
  )
}
