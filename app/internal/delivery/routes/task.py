from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, status
from pydantic import PositiveInt

from app.internal.deps import Application
from app.internal.schemes import (
    CreateTaskCommand,
    DeleteTaskCommand,
    EmptyResult,
    GetTaskCommand,
    Success,
    TaskModel,
    UpdateTaskBody,
    UpdateTaskCommand,
)
from app.internal.service import TaskService

router = APIRouter(
    tags=["Tasks"],
    prefix="/tasks",
)


@router.get(
    "",
    response_model=List[TaskModel],
    status_code=status.HTTP_200_OK,
    description="Get all tasks",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def get_all_tasks(
    skip: int = 0,
    limit: int = 100,
    tasks_service: TaskService = Depends(Provide[Application.services.tasks_service]),
):
    return await tasks_service.get_all(skip=skip, limit=limit)


@router.post(
    "",
    response_model=TaskModel,
    status_code=status.HTTP_201_CREATED,
    description="Create task",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def create_task(
    cmd: CreateTaskCommand,
    tasks_service: TaskService = Depends(Provide[Application.services.tasks_service]),
):
    return await tasks_service.create(cmd=cmd)


@router.get(
    "/{id}",
    response_model=TaskModel,
    status_code=status.HTTP_200_OK,
    description="Get task by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def get_task(
    id: PositiveInt,
    tasks_service: TaskService = Depends(Provide[Application.services.tasks_service]),
):
    return await tasks_service.get(cmd=GetTaskCommand(id=id))


@router.put(
    "/{id}",
    response_model=Success,
    status_code=status.HTTP_200_OK,
    description="Update task by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def update_task(
    id: PositiveInt,
    body: UpdateTaskBody = Body(...),
    tasks_service: TaskService = Depends(Provide[Application.services.tasks_service]),
):
    return await tasks_service.update(cmd=UpdateTaskCommand(id=id, **body.dict()))


@router.delete(
    "/{id}",
    response_model=Success,
    status_code=status.HTTP_200_OK,
    description="Delete task by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def delete_task(
    id: PositiveInt,
    tasks_service: TaskService = Depends(Provide[Application.services.tasks_service]),
):
    return await tasks_service.delete(cmd=DeleteTaskCommand(id=id))
