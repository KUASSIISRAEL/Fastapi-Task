from sqlalchemy.orm import Session

from models.task import Task
from schemas.task import TaskCreate

__all__ = ["get_task", "get_task_by_slug", "get_tasks", "create_task"]


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def get_task_by_slug(db: Session, task_slug: str):
    return db.query(Task).filter(Task.slug == task_slug).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        name=task.name,
        slug=task.slug,
        status=str(task.status),
        priority=task.priority,
        exec_date=task.exec_date,
        description=task.description,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
