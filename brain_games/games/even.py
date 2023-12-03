import random


def show_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def solution():
    question = random.randint(1, 999)
    answer = 'no'
    if question % 2 == 0:
        answer = 'yes'
    return question, answer
