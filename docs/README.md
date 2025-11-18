# Documentazione MedPlanner

Documentazione per il sistema di prenotazione spazi Studio Trovato.

## Indice

- [Note di Sviluppo](#note-di-sviluppo)
- [Architettura](#architettura)
- [Database Schema](#database-schema)
- [API Reference](#api-reference)

## Note di Sviluppo

### Setup Iniziale

1. Clona repository
2. Installa dipendenze backend: `cd backend && pip install -r requirements.txt`
3. Installa dipendenze frontend: `cd frontend && npm install`
4. Avvia con Docker: `docker-compose -f infra/docker-compose.yml up`

### Workflow di Sviluppo

1. Crea branch da `main`: `git checkout -b feature/nome-feature`
2. Sviluppa e testa localmente
3. Commit con messaggio descrittivo: `git commit -m "feat: descrizione"`
4. Push e crea Pull Request
5. Dopo review, merge in `main`

### Convenzioni Codice

**Backend (Python)**
- Usa type hints per tutte le funzioni
- Docstrings in formato Google
- Segui PEP 8 (applicato da black/ruff)
- Test coverage minimo: 80%

**Frontend (TypeScript)**
- Usa TypeScript strict mode
- Componenti funzionali con hooks
- Props tipizzate con interfacce
- CSS modules o styled-components

## Architettura

### Backend

```
FastAPI → Router → Service → Repository → Database
                 ↓
              Schema (Pydantic)
```

- **Router**: Gestisce HTTP requests/responses
- **Service**: Business logic
- **Repository**: Data access layer
- **Schema**: Validazione input/output con Pydantic

### Frontend

```
React Components → API Client → Backend
        ↓
   State Management
   (Context/Zustand)
```

### Database

PostgreSQL con SQLAlchemy ORM e Alembic per migrazioni.

Entità principali:
- **Operators**: Utenti del sistema (admin, operatori)
- **Spaces**: Spazi fisici prenotabili
- **Services**: Tipologie di servizi erogati
- **Bookings**: Prenotazioni
- **Fees**: Quote e tariffe

## Database Schema

Schema dettagliato sarà generato dopo implementazione dei models.

Vedere: `migrations/versions/` per DDL SQL.

## API Reference

Documentazione interattiva disponibile su:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

OpenAPI schema: http://localhost:8000/openapi.json

### Endpoints Principali (Future)

#### Autenticazione
- `POST /api/v1/auth/login` - Login
- `POST /api/v1/auth/logout` - Logout
- `POST /api/v1/auth/refresh` - Refresh token

#### Operatori
- `GET /api/v1/operators` - Lista operatori
- `POST /api/v1/operators` - Crea operatore
- `GET /api/v1/operators/{id}` - Dettaglio operatore
- `PUT /api/v1/operators/{id}` - Aggiorna operatore
- `DELETE /api/v1/operators/{id}` - Elimina operatore

#### Spazi
- `GET /api/v1/spaces` - Lista spazi
- `POST /api/v1/spaces` - Crea spazio
- Etc...

#### Servizi
- `GET /api/v1/services` - Lista servizi
- Etc...

#### Prenotazioni
- `GET /api/v1/bookings` - Lista prenotazioni (con filtri)
- `POST /api/v1/bookings` - Crea prenotazione
- `PUT /api/v1/bookings/{id}` - Modifica prenotazione
- `DELETE /api/v1/bookings/{id}` - Cancella prenotazione

#### Fee/Quote
- `GET /api/v1/fees` - Lista fee
- `GET /api/v1/fees/operator/{id}` - Fee per operatore
- Etc...

## Testing

### Backend
```bash
cd backend
pytest -v --cov=app
```

### Frontend
```bash
cd frontend
npm run test
```

## Deployment

Da definire (Supabase + hosting static frontend).

## Troubleshooting

### Backend non si avvia
- Verificare DATABASE_URL in .env
- Verificare che PostgreSQL sia in esecuzione
- Controllare logs: `docker-compose logs backend`

### Frontend non chiama backend
- Verificare proxy Vite in vite.config.ts
- Verificare CORS settings nel backend
- Controllare network tab nel browser
