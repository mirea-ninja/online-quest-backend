from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import List
from typing import TypeVar

from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateModelCommand = TypeVar("CreateModelCommand", bound=BaseModel)
GetModelCommand = TypeVar("GetModelCommand", bound=BaseModel)
UpdateModelCommand = TypeVar("UpdateModelCommand", bound=BaseModel)
DeleteModelCommand = TypeVar("DeleteModelCommand", bound=BaseModel)


class BaseService(
    ABC,
    Generic[
        ModelType,
        CreateModelCommand,
        GetModelCommand,
        UpdateModelCommand,
        DeleteModelCommand,
    ],
):
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def create(self, cmd: CreateModelCommand) -> ModelType:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, cmd: GetModelCommand) -> ModelType:
        raise NotImplementedError

    @abstractmethod
    async def update(self, cmd: UpdateModelCommand) -> ModelType:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, cmd: DeleteModelCommand) -> ModelType:
        raise NotImplementedError
