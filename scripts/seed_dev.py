#!/usr/bin/env python
"""Script per popolare il database con dati di esempio."""

import argparse
import os
import sys

# Aggiungi backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def seed_database(database_url: str | None = None):
    """
    Popola il database con dati di esempio.

    Args:
        database_url: URL del database (opzionale, usa settings di default)
    """
    # Usa database_url fornito o settings
    db_url = database_url or settings.DATABASE_URL

    print(f"Connessione al database: {db_url}")

    # Crea engine e session
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = SessionLocal()

    try:
        # Verifica connessione
        db.execute(text("SELECT 1"))
        print("✓ Connessione al database riuscita")

        # TODO: Inserire dati di esempio quando i models saranno creati
        # Per ora, solo placeholder

        print("\n--- Seed dati di esempio ---")
        print("(Placeholder - i models non sono ancora stati creati)")
        print("\nFuture entità da creare:")
        print("  - 1 Amministratore")
        print("  - 2-3 Operatori (psicologi, medici)")
        print("  - 3-4 Spazi (Studio 1, Studio 2, Sala TMS, ecc.)")
        print("  - 4-5 Servizi (Psicoterapia, EMDR, TMS, Supervisione)")
        print("  - Alcune prenotazioni di esempio")

        # Example quando i models saranno pronti:
        # from app.db.models.operator import Operator
        # from app.db.models.space import Space
        # from app.db.models.service import Service
        #
        # admin = Operator(
        #     email="admin@studiotrovato.it",
        #     name="Amministratore",
        #     is_admin=True
        # )
        # db.add(admin)
        #
        # space1 = Space(name="Studio 1", capacity=2)
        # db.add(space1)
        #
        # db.commit()

        print("\n✓ Seed completato con successo")

    except Exception as e:
        print(f"\n✗ Errore durante il seed: {e}")
        db.rollback()
        sys.exit(1)
    finally:
        db.close()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Seed database con dati di esempio")
    parser.add_argument(
        "--db-url",
        help="Database URL (default: da settings)",
        default=None
    )

    args = parser.parse_args()

    seed_database(args.db_url)


if __name__ == "__main__":
    main()
