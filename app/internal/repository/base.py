from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import List
from typing import TypeVar

from pydantic import BaseModel

from app.database import Base

TableType = TypeVar("TableType", bound=Base)
CreateModelCommand = TypeVar("CreateModelCommand", bound=BaseModel)
GetModelCommand = TypeVar("GetModelCommand", bound=BaseModel)
UpdateModelCommand = TypeVar("UpdateModelCommand", bound=BaseModel)
DeleteModelCommand = TypeVar("DeleteModelCommand", bound=BaseModel)


class BaseRepository(
    ABC,
    Generic[
        TableType,
        CreateModelCommand,
        GetModelCommand,
        UpdateModelCommand,
        DeleteModelCommand,
    ],
):
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def create(self, cmd: CreateModelCommand) -> TableType:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[TableType]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, cmd: GetModelCommand) -> TableType:
        raise NotImplementedError

    @abstractmethod
    async def update(self, cmd: UpdateModelCommand) -> TableType:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, cmd: DeleteModelCommand) -> TableType:
        raise NotImplementedError
