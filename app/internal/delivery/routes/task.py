from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header, HTTPException, status
from pydantic import PositiveInt

from app.core.utils import check_vk_sign
from app.internal.deps import Application
from app.internal.schemes import EmptyResult, TaskInRequest, TaskModel
from app.internal.service import TaskService

router = APIRouter(
    tags=["Tasks"],
    prefix="/tasks",
)


@router.get(
    "/{user_id}",
    response_model=TaskModel,
    status_code=status.HTTP_200_OK,
    description="Get next task",
    responses={
        **EmptyResult().build_docs(),
    },
)
@inject
async def get_next_task(
    user_id: PositiveInt,
    vk_params: str = Header(...),
    tasks_service: TaskService = Depends(Provide[Application.services.tasks_service]),
):
    if not check_vk_sign(vk_params):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Bad sign")

    if await tasks_service.is_all_tasks_done(user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="All tasks done")

    return await tasks_service.get(
        cmd=TaskInRequest(user_id=user_id, vk_params=vk_params)
    )
