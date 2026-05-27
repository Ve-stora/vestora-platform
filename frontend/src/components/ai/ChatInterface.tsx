import { useState } from 'react'
import { askAI } from '../../api/ai'
import { Send, Bot, User } from 'lucide-react'

interface Message { role: 'user' | 'assistant'; content: string }

const SUGGESTIONS = [
  'What is the Uganda Securities Exchange?',
  'How do dividends work?',
  'What does market capitalisation mean?',
  'How do I start investing in Uganda?',
]

export default function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput]       = useState('')
  const [loading, setLoading]   = useState(false)

  const send = async (question = input) => {
    if (!question.trim()) return
    setMessages(m => [...m, { role: 'user', content: question }])
    setInput(''); setLoading(true)
    try {
      const { answer } = await askAI(question)
      setMessages(m => [...m, { role: 'assistant', content: answer }])
    } catch {
      setMessages(m => [...m, { role: 'assistant', content: 'Sorry, I could not get a response. Please check your API key.' }])
    } finally { setLoading(false) }
  }

  return (
    <div className="card flex flex-col h-[600px]">
      <div className="flex-1 overflow-y-auto space-y-4 mb-4">
        {messages.length === 0 && (
          <div className="text-center py-8">
            <Bot size={40} className="text-primary mx-auto mb-3" />
            <p className="font-display font-semibold text-primary mb-2">Ask me anything about investing</p>
            <div className="flex flex-wrap gap-2 justify-center mt-4">
              {SUGGESTIONS.map(s => (
                <button key={s} onClick={() => send(s)}
                  className="text-xs bg-primary-pale text-primary px-3 py-1.5 rounded-full hover:bg-primary hover:text-white transition-colors">
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}
        {messages.map((m, i) => (
          <div key={i} className={`flex gap-3 ${m.role === 'user' ? 'flex-row-reverse' : ''}`}>
            <div className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0
              ${m.role === 'user' ? 'bg-primary text-white' : 'bg-primary-pale text-primary'}`}>
              {m.role === 'user' ? <User size={14} /> : <Bot size={14} />}
            </div>
            <div className={`max-w-[75%] px-4 py-2.5 rounded-2xl text-sm
              ${m.role === 'user' ? 'bg-primary text-white' : 'bg-gray-100 text-gray-800'}`}>
              {m.content}
            </div>
          </div>
        ))}
        {loading && <div className="text-sm text-gray-400 pl-11">Thinking...</div>}
      </div>
      <div className="flex gap-2">
        <input value={input} onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && send()}
          placeholder="Ask about stocks, dividends, market news..."
          className="flex-1 border border-gray-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/30" />
        <button onClick={() => send()} className="btn-primary flex items-center gap-2">
          <Send size={14} /> Send
        </button>
      </div>
    </div>
  )
}
