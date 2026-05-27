import { useQuery } from '@tanstack/react-query'
import { getModules } from '../api/education'
import ModuleCard from '../components/education/ModuleCard'

export default function Education() {
  const { data: modules = [], isLoading } = useQuery({ queryKey: ['modules'], queryFn: getModules })
  return (
    <div className="space-y-6">
      <h2 className="font-display font-bold text-2xl text-primary">Investor Education Hub</h2>
      <p className="text-gray-500 text-sm">Learn the fundamentals of investing in Uganda's capital markets.</p>
      {isLoading
        ? <div className="text-center text-gray-400 py-8">Loading modules...</div>
        : <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {modules.map((m: any) => <ModuleCard key={m.id} {...m} />)}
          </div>
      }
    </div>
  )
}
