from app.internal.schemes import TaskModel

FLAG = "ninja{w0w_1ts_r3g3xp_0d919e84}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=1,
        question="Настоящий мастер должен быть смекалистым, чтобы вести свой клан вперед. Сейчас мы проверим насколько твои движения быстры, а ум ясен. Сможешь ли ты отыскать то, что мы спрятали в тексте",
        text=open("./app/tasks/_01_source.txt", "r", encoding="utf-8").read(),
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
