FLAG = "ninja{st3gan0_by_n1nja_9262a3c0}"


def get_flag() -> str:
    return FLAG


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
