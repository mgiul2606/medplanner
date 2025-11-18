"""SQLAlchemy base class and utilities."""

from sqlalchemy.ext.declarative import declarative_base

# Base class per tutti i models SQLAlchemy
Base = declarative_base()

# Import tutti i models qui per Alembic autogenerate
# from app.db.models.space import Space
# from app.db.models.service import Service
# etc...
