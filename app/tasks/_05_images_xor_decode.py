FLAG = "ninja{x0r_1s_th3_b35t_1567b02d}"


def get_flag() -> str:
    return FLAG


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
