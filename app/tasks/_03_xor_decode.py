"""Дана исходная фраза(ключ) и строка, с помощью которой производится шифрование. Далее с помощью XOR (
https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%8E%D1%89%D0%B5%D0%B5_%C2%AB%D0%B8%D0%BB
%D0%B8%C2%BB) мы шифруем фразу и получаем массив чисел. Чтобы расшифровать полученный массив, нужно подобрать ключ,
который будет дан как подсказка или его можно будет получить через другой шифр(азбука морзе и тд)

Пример:
Исходная фраза(ответ): mirea_ninja_osa9du
Ключ шифрования: IIT
"""
from app.internal.schemes import TaskModel

FLAG = "ninja{u_r_n0w_g00d_at_x0r_b77e5f57}"
KEY = "IIT"


def get_flag() -> str:
    return FLAG


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=3,
        question="Для того, чтобы попасть в деревню панд IIT, необходимо напрячь извилины, сможешь ли ты разгадать шифр ?",
        text="[494855, 494851, 494872, 494863, 494859, 494901, 494852, 494851, 494852, 494848, 494859, 494901, "
        "494853, 494873, 494859, 494931, 494862, 494879]",
        media_links=[],
    )


def xor_encode(text: str, key: str) -> list[int]:
    key = int(key.encode().hex(), 16)
    return [ord(i) ^ key for i in text]


def check_solution(user_answer: str) -> bool:
    return user_answer == get_flag()
