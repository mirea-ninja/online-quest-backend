from fastapi import APIRouter

from app.config import config

from .answer import router as answer_router
from .quest import router as quest_router
from .task import router as task_router
from .user import router as user_router

__router__ = APIRouter(prefix=config.BACKEND_API_V1_PREFIX)
__router__.include_router(task_router)
__router__.include_router(answer_router)
__router__.include_router(user_router)
__router__.include_router(quest_router)
