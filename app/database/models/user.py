from sqlalchemy import BigInteger, Column, DateTime, Integer, func
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    vk_user_id = Column(
        Integer, nullable=False, unique=True
    )  # https://dev.vk.com/mini-apps/development/launch-params#vk_user_id
    answers = relationship("Answer", back_populates="user")
    created_at = Column(DateTime, default=func.now())
