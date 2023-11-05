from pydantic import BaseModel

__all__ = ["Home"]


class Home(BaseModel):
    message: str
