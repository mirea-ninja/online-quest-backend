from datetime import datetime

from pydantic import BaseModel
from pydantic import PositiveInt

__all__ = [
    "UserModel",
    "CreateUserCommand",
    "GetUserCommand",
    "UpdateUserBody",
    "UpdateUserCommand",
    "DeleteUserCommand",
]


class UserModel(BaseModel):
    id: PositiveInt
    vk_user_id: PositiveInt
    created_at: datetime

    class Config:
        orm_mode = True


class CreateUserCommand(BaseModel):
    vk_user_id: PositiveInt


class GetUserCommand(BaseModel):
    id: PositiveInt


class UpdateUserBody(BaseModel):
    vk_user_id: PositiveInt


class UpdateUserCommand(UpdateUserBody):
    id: PositiveInt


class DeleteUserCommand(BaseModel):
    id: PositiveInt
