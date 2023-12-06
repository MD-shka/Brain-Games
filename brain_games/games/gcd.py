from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


limit_nums = (1, 999)


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_question_and_answer():
    num_1 = randint(*limit_nums)
    num_2 = randint(*limit_nums)
    question = f'{num_1} {num_2}'
    answer = str(get_gcd(num_1, num_2))
    return question, answer
