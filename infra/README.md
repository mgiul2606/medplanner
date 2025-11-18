# Infrastruttura

Configurazione Docker Compose per ambiente di sviluppo.

## Servizi

- **db**: PostgreSQL 15 (porta 5432)
- **backend**: FastAPI (porta 8000)

## Avvio

```bash
# Dalla root del progetto
docker-compose -f infra/docker-compose.yml up --build

# In background
docker-compose -f infra/docker-compose.yml up -d

# Stop
docker-compose -f infra/docker-compose.yml down

# Stop e rimuovi volumi (ATTENZIONE: cancella i dati del DB)
docker-compose -f infra/docker-compose.yml down -v
```

## Accesso ai Servizi

- Backend API: http://localhost:8000
- Backend Docs: http://localhost:8000/docs
- PostgreSQL: localhost:5432
  - User: `medplanner`
  - Password: `medplanner`
  - Database: `medplanner`

## Logs

```bash
# Tutti i servizi
docker-compose -f infra/docker-compose.yml logs -f

# Solo backend
docker-compose -f infra/docker-compose.yml logs -f backend

# Solo database
docker-compose -f infra/docker-compose.yml logs -f db
```

## Exec nei Container

```bash
# Shell nel backend
docker-compose -f infra/docker-compose.yml exec backend bash

# psql nel database
docker-compose -f infra/docker-compose.yml exec db psql -U medplanner -d medplanner
```

## Note

- I dati del database sono persistiti nel volume Docker `postgres-data`
- Il backend usa reload automatico in development (volume mount)
- Per produzione, usare configurazione separata con build ottimizzate
