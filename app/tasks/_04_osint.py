from app.internal.schemes import TaskModel

FLAG = "ninja{os1nt_1n_qu35t_b40936ae}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=4,
        question="Прекрасно, ты достойно прошел испытание. Мой ученик, запомни, без прошлого не может быть и "
                 "будущего. Мастеру просто необходимо знать историю своей деревни IIT. С 2015 года панды заботятся об "
                 "экологии, устраивая каждый год торжественную церемонию сбора бамбука для переработки, "
                 "а также выкладывая результаты сбора. Найди ответ в одной из записей",
        text="Введите ответ",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
