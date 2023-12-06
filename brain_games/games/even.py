from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


limit_nums = (1, 999)


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = randint(*limit_nums)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
