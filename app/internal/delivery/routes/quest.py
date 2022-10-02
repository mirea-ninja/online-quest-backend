from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, status, Response

from app.internal.deps import Application

router = APIRouter(
    tags=["Quest"],
    prefix="/quest",
)



@router.get(
    "",
    status_code=status.HTTP_200_OK,
    description="Get data",
)
@inject
async def get_data(response: Response):
    response.headers["X-MIREA-NINJA-KEY"] = "ninja[d9shys]"
    return {"message": "Happy Birthday IIT!"}
