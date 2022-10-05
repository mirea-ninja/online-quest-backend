from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Header
from fastapi import HTTPException
from fastapi import status
from pydantic import PositiveInt

from app.core.utils import check_vk_sign
from app.internal.deps import Application
from app.internal.schemes import EmptyResult
from app.internal.schemes import TaskInRequest
from app.internal.schemes import TaskModel
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

    return await tasks_service.get(
        cmd=TaskInRequest(user_id=user_id, vk_params=vk_params)
    )
