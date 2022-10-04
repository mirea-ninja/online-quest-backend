from . import xor_decode


def check_solution(task_number: int, user_answer: str) -> bool:
    """Проверка ответа пользователя на задание."""
    return {
        1: lambda: xor_decode.check_solution(user_answer),
        #...
    }.get(task_number, lambda: False)()