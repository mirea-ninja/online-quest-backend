from datetime import datetime, timedelta
from app.tasks import check_solution
from typing import List, Any, Union

from app.internal.repository import AnswerRepository
from app.internal.schemes import (
    AnswerModel,
    CreateAnswerCommand,

    AnswerInRequest,
    DeleteAnswerCommand,
    GetAnswerCommand,
    Success,
    UpdateAnswerCommand,
)

from app.internal.schemes.answer_status import CorrectAnswer, IncorrectAnswer, AnswerAlreadySent, TooManyAnswerRequests

from .base import BaseService


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

    def __init__(self, repository: AnswerRepository) -> None:
        super().__init__()
        self.repository = repository

    async def create(self, cmd: AnswerInRequest) -> Union[
        AnswerAlreadySent, TooManyAnswerRequests, CorrectAnswer, IncorrectAnswer]:
        all_user_answers = await self.repository.get_user_answers(cmd.user_id)

        if all_user_answers:
            if any(answer.task_unique_number == cmd.task_unique_number and answer.answer == answer.answer for answer in
                   all_user_answers):
                return AnswerAlreadySent()
            # Пользователь может отправлять только один ответ раз в 3 секунды
            elif any(
                    answer.task_unique_number == cmd.task_unique_number and answer.sent_at > datetime.now() - timedelta(
                            seconds=3) for answer in all_user_answers):
                return TooManyAnswerRequests()

        # Проверка ответа
        result = check_solution(cmd.task_unique_number, cmd.answer)

        await self.repository.create(cmd=CreateAnswerCommand(
            user_id=cmd.user_id,
            task_unique_number=cmd.task_unique_number,
            answer=cmd.answer,
            is_correct=result,
        ))

        return CorrectAnswer() if result else IncorrectAnswer()

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
