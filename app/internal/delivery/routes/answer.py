from typing import List
from typing import Union

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Header
from fastapi import HTTPException
from fastapi import status
from pydantic import PositiveInt

from app.config import config
from app.core.utils import check_vk_sign
from app.internal.deps import Application
from app.internal.schemes import AnswerInRequest
from app.internal.schemes import AnswerInRequestBody
from app.internal.schemes import AnswerModel
from app.internal.schemes import DeleteAnswerCommand
from app.internal.schemes import EmptyResult
from app.internal.schemes import GetAnswerCommand
from app.internal.schemes import Success
from app.internal.schemes.answer_status import AnswerAlreadySent
from app.internal.schemes.answer_status import CorrectAnswer
from app.internal.schemes.answer_status import IncorrectAnswer
from app.internal.schemes.answer_status import TooManyAnswerRequests
from app.internal.service import AnswerService

router = APIRouter(
    tags=["Answers"],
    prefix="/answers",
)


@router.get(
    "",
    response_model=List[AnswerModel],
    status_code=status.HTTP_200_OK,
    description="Get all answers",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def get_all_answers(
    secret: str,
    skip: int = 0,
    limit: int = 100,
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    if secret != config.BACKEND_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return await answers_service.get_all(skip=skip, limit=limit)


@router.post(
    "",
    response_model=Union[
        AnswerAlreadySent, TooManyAnswerRequests, CorrectAnswer, IncorrectAnswer
    ],
    status_code=status.HTTP_201_CREATED,
    description="Create answer",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def create_answer(
    cmd: AnswerInRequestBody,
    vk_params: str = Header(...),
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    if not check_vk_sign(vk_params):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Bad sign")

    if not 1 <= cmd.task_unique_number <= 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task number must be between 1 and 10",
        )

    return await answers_service.create(
        cmd=AnswerInRequest(vk_params=vk_params, **cmd.dict())
    )


@router.get(
    "/{id}",
    response_model=AnswerModel,
    status_code=status.HTTP_200_OK,
    description="Get answer by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def get_answer(
    id: PositiveInt,
    secret: str,
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    if secret != config.BACKEND_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return await answers_service.get(cmd=GetAnswerCommand(id=id))


# @router.put(
#     "/{id}",
#     response_model=Success,
#     status_code=status.HTTP_200_OK,
#     description="Update answer by id",
#     responses={
#         **EmptyResult().build_docs(),
#     },
# )
# @inject
# async def update_answer(
#     id: PositiveInt,
#     secret: str,
#     body: UpdateAnswerBody = Body(...),
#     answers_service: AnswerService = Depends(
#         Provide[Application.services.answers_service]
#     ),
# ):
#     if secret != config.BACKEND_SECRET_KEY:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
#         )
#     return await answers_service.update(cmd=UpdateAnswerCommand(id=id, **body.dict()))


@router.delete(
    "/{id}",
    response_model=Success,
    status_code=status.HTTP_200_OK,
    description="Delete answer by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def delete_answer(
    id: PositiveInt,
    secret: str,
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    if secret != config.BACKEND_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return await answers_service.delete(cmd=DeleteAnswerCommand(id=id))
