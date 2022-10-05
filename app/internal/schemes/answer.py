from datetime import datetime

from pydantic import BaseModel
from pydantic import PositiveInt

from .user import UserModel


class AnswerModel(BaseModel):
    id: PositiveInt
    user: UserModel
    task_unique_number: PositiveInt
    sent_at: datetime
    is_correct: bool
    answer: str

    class Config:
        orm_mode = True


class CreateAnswerCommand(BaseModel):
    user_id: PositiveInt
    task_unique_number: PositiveInt
    is_correct: bool
    answer: str


class AnswerInRequestBody(BaseModel):
    """Ответ на задание. Отправляется пользователем."""

    user_id: PositiveInt
    task_unique_number: PositiveInt
    answer: str


class AnswerInRequest(AnswerInRequestBody):
    vk_params: str


class GetAnswerCommand(BaseModel):
    id: PositiveInt


class UpdateAnswerBody(BaseModel):
    task_unique_number: PositiveInt
    is_correct: bool


class UpdateAnswerCommand(UpdateAnswerBody):
    id: PositiveInt


class DeleteAnswerCommand(BaseModel):
    id: PositiveInt
