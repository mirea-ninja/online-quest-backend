from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import relationship

from app.pkg.database import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(BigInteger, primary_key=True)
    answer = Column(String, nullable=False)
    users = relationship("UserTask", back_populates="task")
