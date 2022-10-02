from typing import List

from sqlalchemy import delete, update
from sqlalchemy.future import select

from app.internal.handlers import collect_response
from app.internal.repository import BaseRepository
from app.internal.schemes import (
    CreateUserCommand,
    DeleteUserCommand,
    GetUserCommand,
    UpdateUserCommand,
)
from app.database import get_session
from app.database.models import User


class UserRepository(
    BaseRepository[
        User,
        CreateUserCommand,
        GetUserCommand,
        UpdateUserCommand,
        DeleteUserCommand,
    ]
):
    @collect_response
    async def create(self, cmd: CreateUserCommand) -> User:
        async with get_session() as session:
            db_object = User(**cmd.dict())
            session.add(db_object)
            await session.commit()
            await session.refresh(db_object)
            return db_object

    @collect_response
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        async with get_session() as session:
            res = await session.execute(select(User).offset(skip).limit(limit))
            return res.scalars().all()

    @collect_response
    async def get(self, cmd: GetUserCommand) -> User:
        async with get_session() as session:
            res = await session.execute(select(User).where(User.id == cmd.id).limit(1))
            return res.scalar()

    @collect_response
    async def update(self, cmd: UpdateUserCommand) -> None:
        async with get_session() as session:
            res = await session.execute(
                update(User)
                .where(User.id == cmd.id)
                .values(**cmd.dict(exclude_none=True, exclude={"id"}))
                .returning(User)
            )
            res.mappings().one()
            await session.commit()

    @collect_response
    async def delete(self, cmd: DeleteUserCommand) -> None:
        async with get_session() as session:
            res = await session.execute(
                delete(User).where(User.id == cmd.id).returning(User)
            )
            res.mappings().one()
            await session.commit()
