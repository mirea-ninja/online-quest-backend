from app.internal.schemes import TaskModel

FLAG = "ninja{back3nd_1s_th3_b35t_8a0e4d3f}"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=7,
        question="Ты становIшься все опытней, мой друг, н0 тебе предстоит пройти еще несколько испытаний. Я вижу, что мысли твои подобны кругам на vоде. В волнении исчезает ясность но если ты дашь волнам успокоиться, ответ станет очевидным. Сосредоточь свой ра3ум и найди то, _ что ищешь. Клан панд деревни IIT наблюдает за тобой.",
        text="[494855, 494851, 494872, 494863, 494859, 494901, 494852, 494851, 494852, 494848, 494859, 494901, "
        "494853, 494873, 494859, 494931, 494862, 494879]",
        media_links=[],
    )


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
