from datetime import datetime, timedelta
from typing import List, Union

import pytz

from app.core.utils import check_user
from app.internal.schemes import GetUserCommand, TaskInRequest, TaskModel, UserIsBad
from app.tasks import get_task

from .user import UserService


class TaskService:
    users_service: UserService

    def __init__(
        self,
        users_service: UserService,
    ) -> None:
        self.users_service = users_service

    async def get(self, cmd: TaskInRequest) -> Union[TaskModel, UserIsBad]:
        # TODO: get next task for user
        user = await self.users_service.get(cmd=GetUserCommand(id=cmd.user_id))

        if not check_user(user, cmd.vk_params):
            return UserIsBad()

        return get_task(cmd.task_unique_number)
