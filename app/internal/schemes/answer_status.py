from pydantic import BaseModel


class CorrectAnswer(BaseModel):
    message: str = "correct answer"


class IncorrectAnswer(BaseModel):
    message: str = "incorrect answer"


class AnswerAlreadySent(BaseModel):
    message: str = "answer already sent"


class TooManyAnswerRequests(BaseModel):
    message: str = "too many answer requests. try again later"
