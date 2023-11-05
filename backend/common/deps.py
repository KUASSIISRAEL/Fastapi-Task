from typing import Generator

from models.db.session import SessionLocal

__all__ = ["get_db"]


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
