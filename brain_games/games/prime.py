import random


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def show_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def solution():
    question = random.randint(1, 999)
    answer = ('no', 'yes')[is_prime(question)]
    return question, answer
