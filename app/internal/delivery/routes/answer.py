from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, status, HTTPException
from pydantic import PositiveInt

from app.internal.deps import Application
from app.internal.schemes import (
    AnswerModel,
    CreateAnswerCommand,
    DeleteAnswerCommand,
    EmptyResult,
    GetAnswerCommand,
    Success,
    UpdateAnswerBody,
    UpdateAnswerCommand, AnswerInRequest,
)
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
    skip: int = 0,
    limit: int = 100,
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    return await answers_service.get_all(skip=skip, limit=limit)


@router.post(
    "",
    response_model=AnswerModel,
    status_code=status.HTTP_201_CREATED,
    description="Create answer",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def create_answer(
    cmd: AnswerInRequest,
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    if not 1 <= cmd.task_unique_number <= 10:
        raise HTTPException(status_code=400, detail="Task number must be between 1 and 10")

    return await answers_service.create(cmd=cmd)


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
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    return await answers_service.get(cmd=GetAnswerCommand(id=id))


@router.put(
    "/{id}",
    response_model=Success,
    status_code=status.HTTP_200_OK,
    description="Update answer by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def update_answer(
    id: PositiveInt,
    body: UpdateAnswerBody = Body(...),
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    return await answers_service.update(cmd=UpdateAnswerCommand(id=id, **body.dict()))


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
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    return await answers_service.delete(cmd=DeleteAnswerCommand(id=id))


@router.post(
    "/{id}/answer",
    response_model=AnswerModel,
    status_code=status.HTTP_201_CREATED,
    description="Answer answer",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def answer_answer(
    id: PositiveInt,
    cmd: CreateAnswerCommand,
    answers_service: AnswerService = Depends(
        Provide[Application.services.answers_service]
    ),
):
    # TODO: add answer logic
    return await answers_service.create(cmd=cmd)
