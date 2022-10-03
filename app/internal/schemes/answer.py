from datetime import datetime

from pydantic import BaseModel, PositiveInt

from .user import UserModel

__all__ = [
    "AnswerModel",
    "CreateAnswerCommand",
    "GetAnswerCommand",
    "UpdateAnswerBody",
    "UpdateAnswerCommand",
    "DeleteAnswerCommand",
]


class AnswerModel(BaseModel):
    id: PositiveInt
    user: UserModel
    task_unique_number: PositiveInt
    sent_at: datetime
    is_correct: bool

    class Config:
        orm_mode = True


class CreateAnswerCommand(BaseModel):
    user_id: PositiveInt
    task_unique_number: PositiveInt
    is_correct: bool


class GetAnswerCommand(BaseModel):
    id: PositiveInt


class UpdateAnswerBody(BaseModel):
    task_unique_number: PositiveInt
    is_correct: bool


class UpdateAnswerCommand(UpdateAnswerBody):
    id: PositiveInt


class DeleteAnswerCommand(BaseModel):
    id: PositiveInt
