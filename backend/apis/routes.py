from fastapi import APIRouter

from apis.v1.endpoints import home, task

__all__ = ["api_router"]

api_router = APIRouter()

api_router.include_router(home.router, tags=["home"])
api_router.include_router(task.router, prefix="/tasks", tags=["tasks"])
