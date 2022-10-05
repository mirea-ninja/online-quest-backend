from app.internal.schemes import TaskModel

FLAG = "ninja{48.785,132.932}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=2,
        question="Поздравляю, ты преодолел своё первое испытание, но путь предстоит длинный, так что не стоит расслабляться. Настоящий мастер должен уметь хорошо ориентироваться на местности, где бы он не находился. Тебе предстоит найти правильный ориентир и понять, куда же ты попал!",
        text="",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
