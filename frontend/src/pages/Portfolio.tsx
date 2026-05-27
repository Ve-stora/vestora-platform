import HoldingCard from '../components/portfolio/HoldingCard'

export default function Portfolio() {
  return (
    <div className="space-y-6">
      <h2 className="font-display font-bold text-2xl text-primary">My Portfolio</h2>
      <p className="text-gray-500 text-sm">Track your holdings, returns, and dividend income.</p>
      <div className="card text-center py-12 text-gray-400">
        <p className="font-medium mb-2">No holdings yet</p>
        <p className="text-sm">Add your first investment to start tracking your portfolio.</p>
        <button className="btn-primary mt-4 inline-block">Add Holding</button>
      </div>
    </div>
  )
}
