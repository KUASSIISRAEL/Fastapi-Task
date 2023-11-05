from sqlalchemy import Column, Date, Enum, Integer, String, Text
from sqlalchemy.orm import Mapped

from common import StatusType
from models.db.base import Base
from models.db.mixins import DateTimeMixin


class Task(Base, DateTimeMixin):
    __tablename__ = "tasks"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String(255), nullable=False)
    slug: Mapped[str] = Column(String(255), nullable=False, index=True)
    priority: Mapped[int] = Column(Integer, nullable=False)
    status: Mapped[str] = Column(Enum(StatusType), nullable=False, index=True)
    description: Mapped[str] = Column(Text(1000), nullable=False)
    exec_date: Mapped[str] = Column(Date, nullable=False)
