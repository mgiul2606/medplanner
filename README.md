# MedPlanner - Sistema di Prenotazione Spazi Studio Trovato

Sistema di gestione e prenotazione spazi per lo Studio Trovato, che permette la gestione di prenotazioni, operatori, servizi e calcolo automatico delle quote.

## Stack Tecnologico

### Backend
- Python 3.11+
- FastAPI
- SQLAlchemy
- Alembic (migrazioni)
- Pydantic (validazione)
- PostgreSQL (produzione con Supabase)
- pytest + httpx (testing)

### Frontend
- TypeScript
- React 18
- Vite
- zod (validazione)
- vitest + @testing-library/react (testing)

### Infra
- Docker & Docker Compose (ambiente dev)
- PostgreSQL 15 (database)
- GitHub Actions (CI/CD)

## Struttura del Progetto

```
medplanner/
├── backend/          # API FastAPI
├── frontend/         # App React + Vite
├── migrations/       # Migrazioni Alembic
├── infra/           # Docker Compose e configurazioni infra
├── scripts/         # Script utili (seed, etc.)
├── docs/            # Documentazione
└── .github/         # GitHub Actions
```

## Quick Start - Ambiente di Sviluppo

### Prerequisiti
- Docker e Docker Compose
- Python 3.11+
- Node.js 18+ e npm/pnpm

### 1. Avvio completo con Docker Compose

```bash
# Avvia database + backend + frontend
docker-compose -f infra/docker-compose.yml up --build

# Backend disponibile su: http://localhost:8000
# Frontend disponibile su: http://localhost:5173
# API docs: http://localhost:8000/docs
```

### 2. Sviluppo Backend (locale)

```bash
cd backend

# Crea virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oppure: venv\Scripts\activate  # Windows

# Installa dipendenze
pip install -r requirements.txt

# Avvia server di sviluppo
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Sviluppo Frontend (locale)

```bash
cd frontend

# Installa dipendenze
npm install

# Avvia dev server
npm run dev

# Build per produzione
npm run build
```

## Comandi Utili

### Test

```bash
# Test backend
cd backend
pytest -q

# Test frontend
cd frontend
npm run test
```

### Database

```bash
# Applica migrazioni
cd backend
alembic upgrade head

# Crea nuova migrazione
alembic revision --autogenerate -m "descrizione"

# Seed database con dati di esempio
python scripts/seed_dev.py
```

### Linting e Formattazione

```bash
# Backend
cd backend
ruff check .
black .
isort .

# Frontend
cd frontend
npm run lint
npm run format
```

## Verifica Installazione

Dopo aver avviato il sistema, verifica che tutto funzioni:

```bash
# Test endpoint health
curl -sS http://localhost:8000/health | jq .

# Output atteso:
# {"status":"ok"}
```

## Configurazione

### Variabili d'Ambiente

Crea file `.env` nella root del progetto:

```env
# Database
DATABASE_URL=postgresql://medplanner:medplanner@localhost:5432/medplanner

# Backend
BACKEND_PORT=8000
ENVIRONMENT=development

# Frontend
VITE_API_BASE_URL=http://localhost:8000
```

## Branching e Git Workflow

- `main` - branch protetto, solo merge da PR
- `develop` - branch di sviluppo
- `feature/*` - nuove funzionalità
- `fix/*` - correzioni bug

Commit seguono convenzione: `type: description`
- `feat:` nuove funzionalità
- `fix:` correzioni bug
- `chore:` task di manutenzione
- `docs:` documentazione
- `test:` aggiunta/modifica test

## Prossimi Step

1. **Database Design**: Creazione modelli SQLAlchemy completi (Spaces, Services, Operators, Bookings, Fees)
2. **API Endpoints**: Implementazione CRUD per tutte le entità
3. **Frontend UI**: Interfaccia utente completa con calendario e gestione prenotazioni
4. **Autenticazione**: JWT e gestione ruoli (Admin/Operator)
5. **Business Logic**: Validazione prenotazioni, calcolo fee, notifiche

## Documentazione

Vedi cartella `docs/` per documentazione dettagliata:
- Note di sviluppo
- Architettura
- API Reference (generata da OpenAPI)

## Supporto

Per problemi o domande, aprire issue su GitHub repository.