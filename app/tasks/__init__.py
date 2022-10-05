from ..internal.schemes import TaskModel
from . import _01_regexp
from . import _02_coordinates
from . import _03_xor_decode
from . import _04_osint
from . import _05_images_xor_decode
from . import _06_stegano
from . import _07_post_request
from . import _08_todo
from . import _09_socket
from . import _10_todo


def check_solution(task_number: int, user_answer: str) -> bool:
    """Проверка ответа пользователя на задание."""
    return {
        1: lambda: _01_regexp.check_solution(user_answer),
        2: lambda: _02_coordinates.check_solution(user_answer),
        3: lambda: _03_xor_decode.check_solution(user_answer),
        4: lambda: _04_osint.check_solution(user_answer),
        5: lambda: _05_images_xor_decode.check_solution(user_answer),
        6: lambda: _06_stegano.check_solution(user_answer),
        7: lambda: _07_post_request.check_solution(user_answer),
        8: lambda: _08_todo.check_solution(user_answer),
        9: lambda: _09_socket.check_solution(user_answer),
        10: lambda: _10_todo.check_solution(user_answer),
    }.get(task_number, lambda: False)()


def get_task(task_number: int) -> TaskModel:
    """Получение задания по его номеру."""
    return {
        1: lambda: _01_regexp.get_task(),
        2: lambda: _02_coordinates.get_task(),
        3: lambda: _03_xor_decode.get_task(),
        4: lambda: _04_osint.get_task(),
        5: lambda: _05_images_xor_decode.get_task(),
        6: lambda: _06_stegano.get_task(),
        7: lambda: _07_post_request.get_task(),
        8: lambda: _08_todo.get_task(),
        9: lambda: _09_socket.get_task(),
        10: lambda: _10_todo.get_task(),
    }.get(task_number)()
