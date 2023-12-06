from random import randint


RULES = 'What number is missing in the progression?'
START_INDEX = 0

limit_nums = (1, 100)
limit_length = (5, 10)


def get_question_and_answer():
    start = randint(*limit_nums)
    step = randint(*limit_nums)
    length = randint(*limit_length)
    end_index = length - 1
    random_index = randint(START_INDEX, end_index)
    end = start + step * length
    progression = list(range(start, end, step))
    answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, answer
