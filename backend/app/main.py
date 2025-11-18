"""Main FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_router
from app.core.config import settings

# Crea applicazione FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Sistema di prenotazione spazi per Studio Trovato",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers API
app.include_router(api_router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "MedPlanner API",
        "version": settings.VERSION,
        "docs": "/docs",
    }
