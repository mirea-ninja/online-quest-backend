from pydantic import BaseModel

__all__ = ["Success"]


class Success(BaseModel):
    message: str = "success"
