FLAG = "ninja{w0w_1ts_r3g3xp_0d919e84}"


def get_flag() -> str:
    return FLAG


def get_task() -> dict:
    return {
        "task": "Найдите флаг в этом файле.",
    }


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
