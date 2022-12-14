from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Answer(Base):
    __tablename__ = "answer"

    id = Column(BigInteger, primary_key=True)
    user = relationship("User", back_populates="answers", lazy="joined")
    user_id = Column(ForeignKey("user.id"))
    task_unique_number = Column(Integer, nullable=False)
    sent_at = Column(DateTime(True), default=func.now())
    is_correct = Column(Boolean, nullable=False)
    answer = Column(String, nullable=False)  # текст ответа пользователя
