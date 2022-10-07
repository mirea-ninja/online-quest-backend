from app.internal.schemes import TaskModel


FLAGS = ["ninja{48.785,132.932}", "ninja{48.785183,132.932175}", "ninja{48.78518,132.93217}", "ninja{48.7851,132.9321}", "ninja{48.78,132.93}"] 


def get_flag() -> str:
    return FLAGS


def get_task() -> TaskModel:
    return TaskModel(
        task_unique_number=2,
        question="Поздравляю, ты преодолел своё первое испытание, но путь предстоит длинный, так что не стоит расслабляться. Настоящий мастер должен уметь хорошо ориентироваться на местности, где бы он не находился. Тебе предстоит найти правильный ориентир и понять, куда же ты попал!",
        text="",
        media_links=["/static/_02_source_80b097662186d53c.png"],
    )


def check_solution(user_answer: str) -> bool:
    user_answer = user_answer.lower().replace(' ', '')
    

    try:
        if '{' in user_answer and '}' in user_answer:
            tmp_ans = user_answer.split('{')[1].split('}')[0]
            by_nums = tmp_ans.split(',')
            first_num = float(by_nums[0])
            second_num = float(by_nums[1])

            if abs(first_num - 48.785183) <= 0.001 and abs(second_num - 132.932175) <= 0.001:
                return True
                
    except Exception as ex:
        pass

    return user_answer in get_flag()
