import React, { useState } from 'react'
import { Send } from 'lucide-react'

export function AIAssistant() {
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState<Array<{role: string, content: string}>>([])

  const handleSend = async () => {
    if (!message.trim()) return
    
    setMessages([...messages, { role: 'user', content: message }])
    
    try {
      const response = await fetch('http://localhost:8000/api/ai/assistant', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: message })
      })
      const data = await response.json()
      setMessages(prev => [...prev, { role: 'assistant', content: data.response }])
    } catch (error) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, I encountered an error.' }])
    }
    
    setMessage('')
  }

  return (
    <div className="p-6 h-screen flex flex-col">
      <h1 className="text-3xl font-bold mb-4">AI Investment Assistant</h1>
      <div className="flex-1 overflow-auto bg-gray-50 rounded p-4 mb-4">
        {messages.map((msg, i) => (
          <div key={i} className={`mb-4 ${msg.role === 'user' ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block p-2 rounded ${msg.role === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}>
              {msg.content}
            </span>
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Ask about Ugandan stocks..."
          className="flex-1 p-2 border rounded"
        />
        <button
          onClick={handleSend}
          className="bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
        >
          <Send size={20} />
        </button>
      </div>
    </div>
  )
}