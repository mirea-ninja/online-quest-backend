FLAG = "ninja{back3nd_1s_th3_b35t_8a0e4d3f}"


def get_flag() -> str:
    return FLAG


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
