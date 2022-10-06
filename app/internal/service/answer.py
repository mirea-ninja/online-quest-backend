from datetime import datetime, timedelta
from typing import List, Union

import pytz

from app.core.utils import check_user
from app.internal.repository import AnswerRepository
from app.internal.schemes import (
    AnswerInRequest,
    AnswerModel,
    CreateAnswerCommand,
    DeleteAnswerCommand,
    GetAnswerCommand,
    GetUserCommand,
    Success,
    UpdateAnswerCommand,
)
from app.internal.schemes.answer_status import (
    AnswerAlreadySent,
    CorrectAnswer,
    IncorrectAnswer,
    TaskIsNotAvaliableYet,
    TooManyAnswerRequests,
    UserIsBad,
)
from app.tasks import check_solution

from .base import BaseService
from .telegram_logger import TelegramLoggerService
from .user import UserService


class AnswerService(
    BaseService[
        AnswerModel,
        CreateAnswerCommand,
        GetAnswerCommand,
        UpdateAnswerCommand,
        DeleteAnswerCommand,
    ]
):
    repository: AnswerRepository
    users_service: UserService
    telegram_logger_service: TelegramLoggerService

    def __init__(
        self,
        repository: AnswerRepository,
        users_service: UserService,
        telegram_logger_service: TelegramLoggerService,
    ) -> None:
        super().__init__()
        self.repository = repository
        self.users_service = users_service
        self.telegram_service = telegram_logger_service

    async def create(
        self, cmd: AnswerInRequest
    ) -> Union[
        AnswerAlreadySent,
        TooManyAnswerRequests,
        CorrectAnswer,
        IncorrectAnswer,
        UserIsBad,
        TaskIsNotAvaliableYet,
    ]:
        user = await self.users_service.get(cmd=GetUserCommand(id=cmd.user_id))
        if not check_user(user, cmd.vk_params):
            return UserIsBad()

        all_user_answers = await self.repository.get_user_answers(cmd.user_id)
        last_answer = max(all_user_answers, key=lambda answer: answer.id)
        avaliable_task = 1
        if last_answer.is_correct:
            avaliable_task = last_answer.task_unique_number + 1
        else:
            avaliable_task = last_answer.task_unique_number
        if all_user_answers:
            if cmd.task_unique_number > avaliable_task:

                return TaskIsNotAvaliableYet()

            elif any(
                answer.task_unique_number == cmd.task_unique_number
                and datetime.utcnow() - answer.sent_at < timedelta(seconds=3)
                for answer in all_user_answers
            ):
                return TooManyAnswerRequests()

            elif any(
                answer.task_unique_number == cmd.task_unique_number
                and answer.answer == cmd.answer
                for answer in all_user_answers
            ):
                return AnswerAlreadySent()
        # Проверка ответа
        result = check_solution(cmd.task_unique_number, cmd.answer)

        await self.repository.create(
            cmd=CreateAnswerCommand(
                user_id=cmd.user_id,
                task_unique_number=cmd.task_unique_number,
                answer=cmd.answer,
                is_correct=result,
            )
        )
        await self.telegram_service.send_answer(
            user_id=cmd.user_id,
            answer=cmd.answer,
            time=datetime.now(tz=pytz.timezone("Europe/Moscow")).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

        if result:
            await self.telegram_service.send_solve(
                user_id=cmd.user_id,
                time=datetime.now(tz=pytz.timezone("Europe/Moscow")).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                task_number=cmd.task_unique_number,
            )
            return CorrectAnswer()

        return IncorrectAnswer()

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[AnswerModel]:
        result = await self.repository.get_all(skip=skip, limit=limit)
        return [AnswerModel.from_orm(row) for row in result]

    async def get(self, cmd: GetAnswerCommand) -> AnswerModel:
        result = await self.repository.get(cmd=cmd)
        return AnswerModel.from_orm(result)

    async def delete(self, cmd: DeleteAnswerCommand) -> Success:
        await self.repository.delete(cmd=cmd)
        return Success()

    async def update(self, cmd: UpdateAnswerCommand) -> Success:
        raise NotImplementedError
