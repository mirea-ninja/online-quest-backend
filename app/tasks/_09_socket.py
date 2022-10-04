FLAG = "ninja{s0ck3t_i0_ef1a4dfc}"


def get_flag() -> str:
    return FLAG


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
