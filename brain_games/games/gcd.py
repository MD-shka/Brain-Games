import random


def show_rules():
    return 'Find the greatest common divisor of given numbers.'


def make_question():
    return f'{random.randint(1, 999)} {random.randint(1, 999)}'


def check_answer(nums):
    a, b = nums.split(' ')
    a, b = int(a), int(b)
    while b != 0:
        a, b = b, a % b
    return str(a)
