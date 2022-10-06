from app.internal.schemes import TaskModel

FLAG = "ninja{1t_wa5_hard3r_than_0th3r5_48007afpf6c5}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=10,
        question="Вот и настало заключительно испытание. Сегодня нам было передано послание из будущего, к сожалению, нынешние панды-мастера не в силах разгадать его. Мы думаем, что новые ученики смогут решить данную проблему. Я уверен, ты с этим легко справишься. Желаю удачи!",
        text="Answer: 7235950 8653973 22582420 46400007 30942811 18377826 9090748 1809330 24157907 26947293 26463809 19620468 27720117 24249324 18761476",
        media_links=["/static/_10_private_16b5541b2f683ec4.key", "static/_10_solver_d38a5d61a6b2fedf.py"],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
