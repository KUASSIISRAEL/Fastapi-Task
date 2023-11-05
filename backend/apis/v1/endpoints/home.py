from fastapi import APIRouter

from configs import settings
from schemas.home import Home as HomeSchema

router = APIRouter()


@router.get("/", response_model=HomeSchema)
def index():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}
