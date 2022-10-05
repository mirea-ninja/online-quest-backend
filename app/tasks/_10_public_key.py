from app.internal.schemes import TaskModel

FLAG = "ninja{1t_wa5_hard3r_than_0th3r5_48007ac5}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=10,
        question="Для того, чтобы попасть в деревню панд IIT, необходимо напрячь извилины, сможешь ли ты разгадать шифр ?",
        text="[494855, 494851, 494872, 494863, 494859, 494901, 494852, 494851, 494852, 494848, 494859, 494901, "
        "494853, 494873, 494859, 494931, 494862, 494879]",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()