from app.internal.schemes import TaskModel

FLAG = "ninja{x0r_1s_th3_b35t_1567b02d}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=5,
        question="Помни - настоящий мастер не просто качественно выполняет свои обязанности, но и уделяет особое внимание деталям. Стоит упустить всего одну мелочь – и вот, требуемого уровня мастерства уже не достичь. Будь предельно внимателен.",
        text="",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
