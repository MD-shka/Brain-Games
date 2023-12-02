import random


def show_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    return random.randint(1, 999)


def check_answer(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'
