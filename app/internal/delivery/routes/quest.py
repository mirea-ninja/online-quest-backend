from dependency_injector.wiring import inject
from fastapi import APIRouter, HTTPException, Response, status

from app.tasks import _07_post_request

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
async def get_data(key: str, response: Response):
    if key != "l0v3_IIT":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Ha-ha, you thought you could get data from me? No way!",
        )
    response.headers["X-NINJA-KEY"] = _07_post_request.get_flag()
    return {"message": "Happy Birthday IIT!"}
