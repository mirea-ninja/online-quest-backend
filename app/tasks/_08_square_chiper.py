from app.internal.schemes import TaskModel

FLAG = "ninja{y0u_ar3_a1m0st_th3r3_3295dccd9836}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=8,
        question="Для того, чтобы попасть в деревню панд IIT, необходимо напрячь извилины, сможешь ли ты разгадать шифр ?",
        text="a?А -> abcdefghijklmnopqrstuvwxy_1234567890{}\nc0d3 -> 32 23 32 24 11 71 51 66 43 52 11 36 55 52 11 53 31 66 41 42 52 42 22 55 36 55 52 55 54 65 61 14 13 13 14 65 64 55 62 72",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
