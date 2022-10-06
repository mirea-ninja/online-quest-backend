from app.internal.schemes import TaskModel

FLAG = "ninja{back3nd_1s_th3_b35t_8a0e4d3f}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=7,
        question="Ты становIшься все опытней, мой друг, н0 тебе предстоит пройти еще несколько испытаний. Я вижу, что мысли твои подобны кругам на vоде. В волнении исчезает ясность но если ты дашь волнам успокоиться, ответ станет очевидным. Сосредоточь свой ра3ум и найди то, _ что ищешь. Клан панд деревни IIT наблюдает за тобой.",
        text="",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
