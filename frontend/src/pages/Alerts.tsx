export default function Alerts() {
  return (
    <div className="space-y-6">
      <h2 className="font-display font-bold text-2xl text-primary">Smart Alerts</h2>
      <p className="text-gray-500 text-sm">Set price and dividend alerts for your watched stocks.</p>
      <div className="card text-center py-12 text-gray-400">
        <p className="font-medium mb-2">No alerts configured</p>
        <p className="text-sm">Set a price alert on any listed company to get notified.</p>
        <button className="btn-primary mt-4 inline-block">Create Alert</button>
      </div>
    </div>
  )
}
