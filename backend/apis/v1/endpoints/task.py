from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import cruds
import schemas
from common.deps import get_db

router = APIRouter()


@router.post("/", response_model=schemas.TaskCreate)
def create_task(task: schemas.task.TaskCreate, db: Session = Depends(get_db)):
    db_task = cruds.get_task_by_slug(db, task_slug=task.slug)
    if db_task:
        raise HTTPException(status_code=400, detail="This Slug already registered")
    return cruds.create_task(db=db, task=task)


@router.get("/", response_model=List[schemas.Task])
def create_task(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_tasks = cruds.get_tasks(db=db, skip=skip, limit=limit)
    return db_tasks


@router.get("/{task_id}", response_model=schemas.Task)
def create_task(task_id: int, db: Session = Depends(get_db)):
    db_task = cruds.get_task(db=db, task_id=task_id)
    if not db_task:
        raise HTTPException(status_code=400, detail="Task not found")
    return db_task
