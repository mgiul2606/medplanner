# Frontend - MedPlanner

Applicazione React + TypeScript + Vite per il sistema di prenotazione spazi Studio Trovato.

## Stack
- React 18
- TypeScript
- Vite (build tool)
- zod (validazione)
- vitest + @testing-library/react (testing)

## Setup

### 1. Installa Dipendenze

```bash
npm install
```

### 2. Configurazione

Crea file `.env` nella cartella frontend (opzionale):

```env
VITE_API_BASE_URL=http://localhost:8000
```

Il proxy Vite è già configurato per `/api` -> `http://localhost:8000`

### 3. Avvia Dev Server

```bash
npm run dev
```

Applicazione disponibile su: http://localhost:5173

## Comandi

```bash
# Development
npm run dev

# Build per produzione
npm run build

# Preview build produzione
npm run preview

# Test
npm run test

# Linting
npm run lint

# Formattazione
npm run format
```

## Struttura

```
frontend/
├── src/
│   ├── main.tsx           # Entry point
│   ├── App.tsx            # Componente principale
│   ├── pages/             # Componenti pagina
│   │   └── Home.tsx       # Pagina home (placeholder)
│   ├── api/               # Client API
│   │   └── placeholder.ts # Placeholder per chiamate API
│   ├── index.css          # Stili globali
│   └── App.css            # Stili App
├── public/                # Asset statici
├── index.html             # HTML template
├── vite.config.ts         # Configurazione Vite
├── tsconfig.json          # Configurazione TypeScript
└── package.json           # Dipendenze npm
```

## Features Attuali

- Health check backend con UI
- Setup Vite + React + TypeScript completo
- Proxy configurato per chiamate API al backend
- ESLint + Prettier configurati
- Dark/Light mode CSS

## Prossimi Step

1. **Routing**: React Router per navigazione multi-pagina
2. **State Management**: Context API o Zustand
3. **API Client**: Generazione automatica con orval da OpenAPI
4. **UI Components**: Componenti per calendario, form prenotazioni, ecc.
5. **Autenticazione**: Login, gestione token JWT
6. **Forms**: React Hook Form + zod validation
7. **Calendario**: Libreria per visualizzazione prenotazioni

## Note

- Il dev server Vite usa porta 5173 di default
- Hot Module Replacement (HMR) attivo in development
- Build ottimizzato per produzione con code splitting
