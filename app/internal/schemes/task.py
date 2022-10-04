from pydantic import BaseModel, PositiveInt


class TaskModel(BaseModel):
    # TODO: Create Task Model
    task_unique_number: PositiveInt
    text: str
    hint: str


class TaskInRequest(BaseModel):
    user_id: PositiveInt
    vk_params: str
