FLAG = "ninja{y0u_ar3_a1m0st_th3r3}_3295dccd9836"


def get_flag() -> str:
    return FLAG


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
