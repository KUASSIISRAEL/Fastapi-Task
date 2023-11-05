from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs import settings

__all__ = ["SessionLocal"]

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
