import random


def show_rules():
    return 'Find the greatest common divisor of given numbers.'


def solution():
    a, b = random.randint(1, 999), random.randint(1, 999)
    question = f'{a} {b}'
    while b != 0:
        a, b = b, a % b
    answer = str(a)
    return question, answer
