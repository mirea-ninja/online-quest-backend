from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.orm import relationship

from app.pkg.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    vk_user_id = Column(
        Integer, nullable=False
    )  # https://dev.vk.com/mini-apps/development/launch-params#vk_user_id
