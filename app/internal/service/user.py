from typing import List

from app.internal.repository import UserRepository
from app.internal.schemes import CreateUserCommand
from app.internal.schemes import DeleteUserCommand
from app.internal.schemes import GetUserCommand
from app.internal.schemes import Success
from app.internal.schemes import UpdateUserCommand
from app.internal.schemes import UserModel

from .base import BaseService


class UserService(
    BaseService[
        UserModel,
        CreateUserCommand,
        GetUserCommand,
        UpdateUserCommand,
        DeleteUserCommand,
    ]
):
    repository: UserRepository

    def __init__(self, repository: UserRepository) -> None:
        super().__init__()
        self.repository = repository

    async def create(self, cmd: CreateUserCommand) -> UserModel:
        result = await self.repository.create(cmd=cmd)
        return UserModel.from_orm(result)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[UserModel]:
        result = await self.repository.get_all(skip=skip, limit=limit)
        return [UserModel.from_orm(row) for row in result]

    async def get(self, cmd: GetUserCommand) -> UserModel:
        result = await self.repository.get(cmd=cmd)
        return UserModel.from_orm(result)

    async def delete(self, cmd: DeleteUserCommand) -> Success:
        await self.repository.delete(cmd=cmd)
        return Success()

    async def update(self, cmd: UpdateUserCommand) -> Success:
        raise NotImplementedError
