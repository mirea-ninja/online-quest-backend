from app.internal.schemes import TaskModel

FLAG = "ninja{48.785,132.932}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=2,
        question="Найдите флаг в этом файле. Флаг начинается с ninja{ и заканчивается }",
        text="...",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
