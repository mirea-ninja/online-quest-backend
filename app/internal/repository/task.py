from typing import List

from sqlalchemy import delete, update
from sqlalchemy.future import select

from app.internal.handlers import collect_response
from app.internal.repository import BaseRepository
from app.internal.schemes import (
    CreateTaskCommand,
    DeleteTaskCommand,
    GetTaskCommand,
    UpdateTaskCommand,
)
from app.database import get_session
from app.database.models import Task


class TaskRepository(
    BaseRepository[
        Task,
        CreateTaskCommand,
        GetTaskCommand,
        UpdateTaskCommand,
        DeleteTaskCommand,
    ]
):
    @collect_response
    async def create(self, cmd: CreateTaskCommand) -> Task:
        async with get_session() as session:
            db_object = Task(**cmd.dict())
            session.add(db_object)
            await session.commit()
            await session.refresh(db_object)
            return db_object

    @collect_response
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Task]:
        async with get_session() as session:
            res = await session.execute(select(Task).offset(skip).limit(limit))
            return res.scalars().all()

    @collect_response
    async def get(self, cmd: GetTaskCommand) -> Task:
        async with get_session() as session:
            res = await session.execute(select(Task).where(Task.id == cmd.id).limit(1))
            return res.scalar()

    @collect_response
    async def update(self, cmd: UpdateTaskCommand) -> None:
        async with get_session() as session:
            res = await session.execute(
                update(Task)
                .where(Task.id == cmd.id)
                .values(**cmd.dict(exclude_none=True, exclude={"id"}))
                .returning(Task)
            )
            res.mappings().one()
            await session.commit()

    @collect_response
    async def delete(self, cmd: DeleteTaskCommand) -> None:
        async with get_session() as session:
            res = await session.execute(
                delete(Task).where(Task.id == cmd.id).returning(Task)
            )
            res.mappings().one()
            await session.commit()
