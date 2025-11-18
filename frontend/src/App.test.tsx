import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import App from './App'

describe('App', () => {
  it('renders MedPlanner title', () => {
    render(<App />)
    expect(screen.getByText('MedPlanner')).toBeDefined()
  })

  it('renders health check section', () => {
    render(<App />)
    expect(screen.getByText('Backend Health Check')).toBeDefined()
  })
})
