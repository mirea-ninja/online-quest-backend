from pydantic import BaseModel, PositiveInt

__all__ = [
    "CampusModel",
    "CreateCampusCommand",
    "GetCampusCommand",
    "UpdateCampusBody",
    "UpdateCampusCommand",
    "DeleteCampusCommand",
]


class CampusModel(BaseModel):
    id: PositiveInt
    campus: str

    class Config:
        orm_mode = True


class CreateCampusCommand(BaseModel):
    campus: str


class GetCampusCommand(BaseModel):
    id: PositiveInt


class UpdateCampusBody(BaseModel):
    campus: str


class UpdateCampusCommand(UpdateCampusBody):
    id: PositiveInt


class DeleteCampusCommand(BaseModel):
    id: PositiveInt
