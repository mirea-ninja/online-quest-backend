from typing import Optional

from pydantic import BaseModel
from pydantic import PositiveInt


class TaskModel(BaseModel):
    task_unique_number: PositiveInt
    hint: Optional[str] = None  # подсказка
    question: str  # текст задания
    text: str  # копируемый текст, используемый в форме задания
    media_links: list[str]  # ссылки на медиафайлы, если нужно


class TaskInRequest(BaseModel):
    user_id: PositiveInt
    vk_params: str
