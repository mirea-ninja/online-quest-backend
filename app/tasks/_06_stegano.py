from app.internal.schemes import TaskModel

FLAG = "ninja{st3gan0_by_n1nja_9262a3c0}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=6,
        question="Поздравляю, юный ученик, тебе удалось разгадать половину моих загадок. Но наши панды не слишком "
                 "разговорчивы, просто так они не поведают о своих секретах. Тебе предстоит задобрить жителей "
                 "деревни. Посмотрим, сможешь ли ты это сделать.",
        text="",
        media_links=["/static/_06_source_f74e939af921ca26.png"],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
