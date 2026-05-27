import { BookOpen } from 'lucide-react'

const LEVEL_COLORS: Record<string, string> = {
  beginner:     'bg-green-100 text-green-700',
  intermediate: 'bg-yellow-100 text-yellow-700',
  advanced:     'bg-red-100 text-red-700',
}

interface Props { id: number; title: string; level: string; description: string }

export default function ModuleCard({ id, title, level, description }: Props) {
  return (
    <div className="card hover:shadow-md transition-shadow cursor-pointer">
      <div className="flex justify-between items-start mb-3">
        <BookOpen size={20} className="text-primary" />
        <span className={`text-xs font-medium px-2 py-1 rounded-full capitalize ${LEVEL_COLORS[level]}`}>{level}</span>
      </div>
      <h3 className="font-display font-semibold mb-2">{title}</h3>
      <p className="text-sm text-gray-500">{description}</p>
    </div>
  )
}
