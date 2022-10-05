from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.orm import declarative_base

from .connection import SqlAlchemyConnection

Base: DeclarativeMeta = declarative_base()
sqlalchemy_connection = SqlAlchemyConnection()


@asynccontextmanager
async def get_session() -> AsyncSession:
    async with sqlalchemy_connection.get_session() as session:
        yield session
