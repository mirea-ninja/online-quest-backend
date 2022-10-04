from typing import List

from sqlalchemy import delete, update
from sqlalchemy.future import select

from app.database import get_session
from app.database.models import Answer
from app.internal.handlers import collect_response
from app.internal.schemes import (
    CreateAnswerCommand,
    DeleteAnswerCommand,
    GetAnswerCommand,
    UpdateAnswerCommand,
)


class AnswerRepository:
    @collect_response
    async def get_user_answers(self, user_id: int) -> List[Answer]:
        async with get_session() as session:
            res = await session.execute(select(Answer).where(Answer.user_id == user_id))
            return res.scalars().all()

    @collect_response
    async def create(self, cmd: CreateAnswerCommand) -> Answer:
        async with get_session() as session:
            db_object = Answer(**cmd.dict())
            session.add(db_object)
            await session.commit()
            await session.refresh(db_object)
            return db_object

    @collect_response
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Answer]:
        async with get_session() as session:
            res = await session.execute(select(Answer).offset(skip).limit(limit))
            return res.scalars().all()

    @collect_response
    async def get(self, cmd: GetAnswerCommand) -> Answer:
        async with get_session() as session:
            res = await session.execute(
                select(Answer).where(Answer.id == cmd.id).limit(1)
            )
            return res.scalar()

    @collect_response
    async def update(self, cmd: UpdateAnswerCommand) -> None:
        # async with get_session() as session:
        #     res = await session.execute(
        #         update(Answer)
        #         .where(Answer.id == cmd.id)
        #         .values(**cmd.dict(exclude_none=True, exclude={"id"}))
        #         .returning(Answer)
        #     )
        #     res.mappings().one()
        #     await session.commit()
        raise NotImplementedError

    @collect_response
    async def delete(self, cmd: DeleteAnswerCommand) -> None:
        async with get_session() as session:
            res = await session.execute(
                delete(Answer).where(Answer.id == cmd.id).returning(Answer)
            )
            res.mappings().one()
            await session.commit()
