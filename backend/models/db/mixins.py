from datetime import datetime

from sqlalchemy import TIMESTAMP, Column
from sqlalchemy.orm import Mapped

__all__ = ["DateTimeMixin"]


class DateTimeMixin:
    created_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.now)
    updated_at: Mapped[datetime] = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
