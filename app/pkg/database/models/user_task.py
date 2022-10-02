from sqlalchemy import Column, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from app.pkg.database import Base


class UserTask(Base):
    __tablename__ = "user_task"
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    task_id = Column(ForeignKey("task.id"), primary_key=True)
    completed_at = Column(DateTime, server_default=func.now())
    task = relationship("Task", back_populates="users")
    user = relationship("User", back_populates="tasks")
