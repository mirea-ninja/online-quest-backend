from typing import List

from app.internal.repository import AnswerRepository
from app.internal.schemes import (
    AnswerModel,
    CreateAnswerCommand,
    DeleteAnswerCommand,
    GetAnswerCommand,
    Success,
    UpdateAnswerCommand,
)

from .base import BaseService


class AnswerService(
    BaseService[
        AnswerModel,
        CreateAnswerCommand,
        GetAnswerCommand,
        UpdateAnswerCommand,
        DeleteAnswerCommand,
    ]
):
    repository: AnswerRepository

    def __init__(self, repository: AnswerRepository) -> None:
        super().__init__()
        self.repository = repository

    async def create(self, cmd: CreateAnswerCommand) -> AnswerModel:
        result = await self.repository.create(cmd=cmd)
        return AnswerModel.from_orm(result)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[AnswerModel]:
        result = await self.repository.get_all(skip=skip, limit=limit)
        return [AnswerModel.from_orm(row) for row in result]

    async def get(self, cmd: GetAnswerCommand) -> AnswerModel:
        result = await self.repository.get(cmd=cmd)
        return AnswerModel.from_orm(result)

    async def delete(self, cmd: DeleteAnswerCommand) -> Success:
        await self.repository.delete(cmd=cmd)
        return Success()

    async def update(self, cmd: UpdateAnswerCommand) -> Success:
        raise NotImplementedError
