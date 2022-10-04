FLAG = "ninja{48.785,132.932}"


def get_flag() -> str:
    return FLAG


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
