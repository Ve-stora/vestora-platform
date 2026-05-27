import ChatInterface from '../components/ai/ChatInterface'

export default function AIAssistant() {
  return (
    <div className="space-y-6 max-w-3xl">
      <h2 className="font-display font-bold text-2xl text-primary">AI Financial Assistant</h2>
      <p className="text-gray-500 text-sm">Ask any question about investing, the USE, or Uganda's capital markets.</p>
      <ChatInterface />
    </div>
  )
}
