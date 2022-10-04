FLAG = "ninja{os1nt_1n_qu35t_b40936ae}"


def get_flag() -> str:
    return FLAG


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
