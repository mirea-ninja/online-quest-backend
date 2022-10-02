from pydantic import BaseModel, PositiveInt

__all__ = [
    "TaskModel",
    "CreateTaskCommand",
    "GetTaskCommand",
    "UpdateTaskBody",
    "UpdateTaskCommand",
    "DeleteTaskCommand",
]


class TaskModel(BaseModel):
    id: PositiveInt
    answer: str

    class Config:
        orm_mode = True


class CreateTaskCommand(BaseModel):
    answer: str


class GetTaskCommand(BaseModel):
    id: PositiveInt


class UpdateTaskBody(BaseModel):
    answer: str


class UpdateTaskCommand(UpdateTaskBody):
    id: PositiveInt


class DeleteTaskCommand(BaseModel):
    id: PositiveInt
