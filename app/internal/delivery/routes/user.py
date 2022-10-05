from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header, HTTPException, status
from pydantic import PositiveInt

from app.config import config
from app.core.utils import check_vk_sign
from app.internal.deps import Application
from app.internal.schemes import (
    CreateUserCommand,
    DeleteUserCommand,
    EmptyResult,
    GetUserCommand,
    Success,
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
    secret: str,
    skip: int = 0,
    limit: int = 100,
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    if secret != config.BACKEND_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
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
    vk_params: str = Header(...),
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    if not check_vk_sign(vk_params):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Bad sign")
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
    secret: str,
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    if secret != config.BACKEND_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return await users_service.get(cmd=GetUserCommand(id=id))


# @router.put(
#     "/{id}",
#     response_model=Success,
#     status_code=status.HTTP_200_OK,
#     description="Update user by id",
#     responses={
#         **EmptyResult().build_docs(),
#     },
# )
# @inject
# async def update_user(
#     id: PositiveInt,
#     secret: str,
#     body: UpdateUserBody = Body(...),
#     users_service: UserService = Depends(Provide[Application.services.users_service]),
# ):
#     if secret != config.BACKEND_SECRET_KEY:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
#         )
#     return await users_service.update(cmd=UpdateUserCommand(id=id, **body.dict()))


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
    secret: str,
    users_service: UserService = Depends(Provide[Application.services.users_service]),
):
    if secret != config.BACKEND_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return await users_service.delete(cmd=DeleteUserCommand(id=id))
