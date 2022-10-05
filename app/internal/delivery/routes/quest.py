from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Response
from fastapi import status

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
