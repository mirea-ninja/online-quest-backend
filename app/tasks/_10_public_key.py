from app.internal.schemes import TaskModel

FLAG = "ninja{1t_wa5_hard3r_than_0th3r5_48007ac5}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=10,
        question="Вот и настало заключительно испытание. Сегодня нам было передано послание из будущего, к сожалению, нынешние панды-мастера не в силах разгадать его. Мы думаем, что новые ученики смогут решить данную проблему. Я уверен, ты с этим легко справишься. Желаю удачи!",
        text="",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
