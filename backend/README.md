# Backend - MedPlanner API

FastAPI backend per il sistema di prenotazione spazi Studio Trovato.

## Stack
- Python 3.11+
- FastAPI
- SQLAlchemy (ORM)
- Alembic (migrazioni DB)
- PostgreSQL
- Pydantic (validazione)
- pytest (testing)

## Setup Locale

### 1. Crea Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oppure: venv\Scripts\activate  # Windows
```

### 2. Installa Dipendenze

```bash
pip install -r requirements.txt
```

### 3. Configura Variabili d'Ambiente

Crea file `.env` nella cartella backend:

```env
DATABASE_URL=postgresql://medplanner:medplanner@localhost:5432/medplanner
# Oppure per dev locale con SQLite:
# DATABASE_URL=sqlite:///./medplanner.db

ENVIRONMENT=development
SECRET_KEY=your-secret-key-change-in-production
```

### 4. Applica Migrazioni

```bash
alembic upgrade head
```

### 5. Avvia Server

```bash
# Modalità development con reload automatico
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Server disponibile su:
# - API: http://localhost:8000
# - Docs interattiva: http://localhost:8000/docs
# - ReDoc: http://localhost:8000/redoc
```

## Testing

```bash
# Esegui tutti i test
pytest

# Con output verbose
pytest -v

# Con coverage
pytest --cov=app --cov-report=html

# Solo test specifici
pytest app/tests/test_health.py
```

## Struttura

```
backend/
├── app/
│   ├── main.py              # Entry point FastAPI
│   ├── core/                # Configurazioni core
│   │   ├── config.py        # Settings e configurazione
│   │   └── security.py      # Autenticazione e sicurezza
│   ├── db/                  # Database
│   │   ├── base.py          # Base SQLAlchemy
│   │   ├── session.py       # Database session
│   │   └── models/          # SQLAlchemy models
│   ├── api/                 # Endpoints API
│   │   └── v1/              # API versione 1
│   │       └── health.py    # Health check endpoint
│   ├── schemas/             # Pydantic schemas (request/response)
│   └── tests/               # Test suite
│       └── test_health.py   # Test health endpoint
├── alembic.ini              # Configurazione Alembic
├── requirements.txt         # Dipendenze Python
└── README.md               # Questa documentazione
```

## API Endpoints

### Health Check
- `GET /health` - Verifica stato del servizio

### Future endpoints (prossimi step):
- `/api/v1/spaces` - Gestione spazi
- `/api/v1/services` - Gestione servizi
- `/api/v1/operators` - Gestione operatori
- `/api/v1/bookings` - Gestione prenotazioni
- `/api/v1/fees` - Gestione quote

## Sviluppo

### Linting e Formattazione

```bash
# Ruff (linting)
ruff check .

# Black (formatting)
black .

# isort (import sorting)
isort .
```

### Creazione Migrazioni

```bash
# Auto-genera migrazione da modifiche models
alembic revision --autogenerate -m "descrizione modifiche"

# Applica migrazioni
alembic upgrade head

# Rollback ultima migrazione
alembic downgrade -1
```

## Note

- Il backend usa CORS permissivo in development per permettere chiamate da frontend (localhost:5173)
- In production, configurare CORS in modo restrittivo
- Database di default: PostgreSQL (Supabase in produzione)
- Per test locali veloci, si può usare SQLite in-memory
