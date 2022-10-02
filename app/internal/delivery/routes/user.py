from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, status
from pydantic import PositiveInt

from app.internal.deps import Application
from app.internal.schemes import (
    CreateUserCommand,
    DeleteUserCommand,
    EmptyResult,
    GetUserCommand,
    Success,
    UpdateUserBody,
    UpdateUserCommand,
    UserModel,
)
from app.internal.service import UserService

router = APIRouter(
    tags=["Users"],
    prefix="/users",
)


@router.get(
    "",
    response_model=List[UserModel],
    status_code=status.HTTP_200_OK,
    description="Get all users",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def get_all_users(
    skip: int = 0,
    limit: int = 100,
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    return await users_service.get_all(skip=skip, limit=limit)


@router.post(
    "",
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED,
    description="Create user",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def create_user(
    cmd: CreateUserCommand,
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    return await users_service.create(cmd=cmd)


@router.get(
    "/{id}",
    response_model=UserModel,
    status_code=status.HTTP_200_OK,
    description="Get user by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def get_user(
    id: PositiveInt,
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    return await users_service.get(cmd=GetUserCommand(id=id))


@router.put(
    "/{id}",
    response_model=Success,
    status_code=status.HTTP_200_OK,
    description="Update user by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def update_user(
    id: PositiveInt,
    body: UpdateUserBody = Body(...),
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    return await users_service.update(cmd=UpdateUserCommand(id=id, **body.dict()))


@router.delete(
    "/{id}",
    response_model=Success,
    status_code=status.HTTP_200_OK,
    description="Delete user by id",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def delete_user(
    id: PositiveInt,
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    return await users_service.delete(cmd=DeleteUserCommand(id=id))
