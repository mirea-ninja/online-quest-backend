from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class Answer(Base):
    """Таблица всех ответов пользователей."""
    __tablename__ = "answer"
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    task_unique_number = Column(Integer)  # Уникальный номер задачи (1-10)
    sent_at = Column(DateTime, default=func.now())
    is_correct = Column(Boolean, nullable=False)  # Правильный ли ответ
    user = relationship("User", back_populates="answers")
