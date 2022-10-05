from typing import Union

from app.core.utils import check_user
from app.internal.schemes import GetUserCommand, TaskInRequest, TaskModel, UserIsBad
from app.tasks import get_task

from ..repository import AnswerRepository
from .user import UserService


class TaskService:
    users_service: UserService

    def __init__(
        self,
        repository: AnswerRepository,
        users_service: UserService,
    ) -> None:
        self.repository = repository
        self.users_service = users_service

    async def get(self, cmd: TaskInRequest) -> Union[TaskModel, UserIsBad]:
        user = await self.users_service.get(cmd=GetUserCommand(id=cmd.user_id))

        if not check_user(user, cmd.vk_params):
            return UserIsBad()

        all_user_answers = await self.repository.get_user_answers(cmd.user_id)

        if all_user_answers:
            last_answer = max(
                all_user_answers,
                key=lambda answer: answer.task_unique_number,
            )
            if last_answer.is_correct:
                task_unique_number = last_answer.task_unique_number + 1
            else:
                task_unique_number = last_answer.task_unique_number
        else:
            task_unique_number = 1

        return get_task(task_unique_number)
