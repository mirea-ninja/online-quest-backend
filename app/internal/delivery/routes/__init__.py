from fastapi import APIRouter

from app.config import config

# from .auth_route import router as auth_router

__router__ = APIRouter(prefix=config.BACKEND_API_V1_PREFIX)
# __router__.include_router(auth_router)
