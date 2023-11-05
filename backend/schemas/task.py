from datetime import datetime

from pydantic import BaseModel

from common import StatusType

__all__ = ["TaskCreate", "TaskUpdate", "Task"]


class BaseTask(BaseModel):
    name: str
    slug: str
    status: StatusType
    priority: int
    description: str
    exec_date: datetime


class TaskCreate(BaseTask):
    pass


class TaskUpdate(BaseTask):
    pass


class Task(BaseTask):
    id: int
    created_at: datetime
    updated_at: datetime

    class ConfigDict:
        from_attributes = True
