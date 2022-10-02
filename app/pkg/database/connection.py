from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import config

__all__ = ["SqlAlchemyConnection"]


class SqlAlchemyConnection:
    def __init__(self):
        self._session_maker = self.__get_session_maker()

    def __get_session_maker(self) -> sessionmaker:

        self._session_maker = sessionmaker(
            create_async_engine(self.get_dsn(), echo=config.TEST_MODE),
            class_=AsyncSession,
            expire_on_commit=False,
        )

        return self._session_maker

    @staticmethod
    def get_dsn() -> str:
        return f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_SERVER}:5432/{config.POSTGRES_DB}"

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        """Connect to a database."""
        async with self._session_maker() as session:
            try:
                yield session
            finally:
                await session.close()
