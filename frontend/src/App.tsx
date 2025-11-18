import { useState, useEffect } from 'react'
import './App.css'

interface HealthResponse {
  status: string
}

function App() {
  const [healthStatus, setHealthStatus] = useState<string>('checking...')
  const [isLoading, setIsLoading] = useState<boolean>(true)
  const [error, setError] = useState<string | null>(null)

  const checkHealth = async () => {
    setIsLoading(true)
    setError(null)

    try {
      // Usa proxy Vite per chiamare backend
      const response = await fetch('/api/health')

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data: HealthResponse = await response.json()
      setHealthStatus(data.status)
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error'
      setError(errorMessage)
      setHealthStatus('error')
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(() => {
    checkHealth()
  }, [])

  return (
    <>
      <h1>MedPlanner</h1>
      <p>Sistema di Prenotazione Spazi - Studio Trovato</p>

      <div className="card">
        <h2>Backend Health Check</h2>

        {isLoading && (
          <div className="status loading">
            Verifica connessione al backend...
          </div>
        )}

        {!isLoading && !error && (
          <div className="status success">
            Backend Status: <strong>{healthStatus}</strong>
          </div>
        )}

        {error && (
          <div className="status error">
            Errore: {error}
            <br />
            <small>Assicurati che il backend sia in esecuzione su http://localhost:8000</small>
          </div>
        )}

        <button onClick={checkHealth} style={{ marginTop: '1rem' }}>
          Ricontrolla
        </button>
      </div>

      <div className="card">
        <h3>Prossimi passi</h3>
        <ul style={{ textAlign: 'left', lineHeight: '2' }}>
          <li>Implementazione modelli database (Spaces, Services, Operators, Bookings)</li>
          <li>API CRUD per tutte le entità</li>
          <li>Sistema di autenticazione (JWT)</li>
          <li>Interfaccia calendario prenotazioni</li>
          <li>Gestione fee e reportistica</li>
        </ul>
      </div>
    </>
  )
}

export default App
