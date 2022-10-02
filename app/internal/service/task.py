from typing import List

from app.internal.schemes import (
    TaskModel,
    CreateTaskCommand,
    GetTaskCommand,
    UpdateTaskCommand,
    DeleteTaskCommand,
)

from app.internal.schemes import Success
from app.internal.repository import TaskRepository
from app.internal.service import BaseService


class TaskService(
    BaseService[
        TaskModel,
        CreateTaskCommand,
        GetTaskCommand,
        UpdateTaskCommand,
        DeleteTaskCommand,
    ]
):
    repository: TaskRepository

    def __init__(self, repository: TaskRepository) -> None:
        super().__init__()
        self.repository = repository

    async def create(self, cmd: CreateTaskCommand) -> TaskModel:
        result = await self.repository.create(cmd=cmd)
        return TaskModel.from_orm(result)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[TaskModel]:
        result = await self.repository.get_all(skip=skip, limit=limit)
        return [TaskModel.from_orm(row) for row in result]

    async def get(self, cmd: GetTaskCommand) -> TaskModel:
        result = await self.repository.get(cmd=cmd)
        return TaskModel.from_orm(result)

    async def delete(self, cmd: DeleteTaskCommand) -> Success:
        await self.repository.delete(cmd=cmd)
        return Success()

    async def update(self, cmd: UpdateTaskCommand) -> Success:
        raise NotImplementedError
