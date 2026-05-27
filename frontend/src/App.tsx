import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './store/useStore'
import { Login, Register } from './pages'
import { Dashboard } from './components/Dashboard'
import { Portfolio } from './components/Portfolio'
import { MarketOverview } from './components/MarketOverview'
import { AIAssistant } from './components/AIAssistant'

function App() {
  const { isAuthenticated } = useAuthStore()

  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      
      {isAuthenticated ? (
        <>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/portfolio" element={<Portfolio />} />
          <Route path="/market" element={<MarketOverview />} />
          <Route path="/ai" element={<AIAssistant />} />
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
        </>
      ) : (
        <Route path="*" element={<Navigate to="/login" replace />} />
      )}
    </Routes>
  )
}

export default App