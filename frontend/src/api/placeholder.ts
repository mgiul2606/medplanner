/**
 * API client placeholder.
 * Future: generato automaticamente con orval da OpenAPI spec.
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

export async function fetchHealth(): Promise<{ status: string }> {
  const response = await fetch(`${API_BASE_URL}/health`)
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`)
  }
  return response.json()
}

// Future API functions:
// - fetchSpaces()
// - createBooking()
// - etc.
