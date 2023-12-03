import random


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def show_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def solution():
    question = random.randint(1, 999)
    answer = ('no', 'yes')[is_even(question)]
    return question, answer
