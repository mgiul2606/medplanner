.PHONY: help up down backend-run frontend-dev test-backend test-frontend seed lint-backend lint-frontend clean

help:
	@echo "MedPlanner - Comandi disponibili:"
	@echo ""
	@echo "  make up              - Avvia stack dev con docker-compose"
	@echo "  make down            - Ferma stack dev"
	@echo "  make backend-run     - Avvia backend in locale (senza docker)"
	@echo "  make frontend-dev    - Avvia frontend in dev mode"
	@echo "  make test-backend    - Esegui test backend"
	@echo "  make test-frontend   - Esegui test frontend"
	@echo "  make seed            - Popola DB con dati di esempio"
	@echo "  make lint-backend    - Lint e format backend"
	@echo "  make lint-frontend   - Lint frontend"
	@echo "  make clean           - Rimuovi file temporanei"
	@echo ""

up:
	docker-compose -f infra/docker-compose.yml up --build

down:
	docker-compose -f infra/docker-compose.yml down

backend-run:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend-dev:
	cd frontend && npm run dev

test-backend:
	cd backend && pytest -q

test-frontend:
	cd frontend && npm run test

seed:
	python scripts/seed_dev.py

lint-backend:
	cd backend && ruff check . || true
	cd backend && black . || true
	cd backend && isort . || true

lint-frontend:
	cd frontend && npm run lint || true

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf backend/.pytest_cache 2>/dev/null || true
	rm -rf frontend/dist 2>/dev/null || true
	rm -rf frontend/node_modules/.vite 2>/dev/null || true
