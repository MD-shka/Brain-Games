from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


limit_nums = (1, 999)


def is_prime(number):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


def get_question_and_answer():
    question = randint(*limit_nums)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
