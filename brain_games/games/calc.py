from random import randint, choice
from operator import add, sub, mul


OPERATORS = {'+': add, '-': sub, '*': mul}
RULES = 'What is the result of the expression?'


limit_nums = (1, 999)


def get_question_and_answer():
    num_1 = randint(*limit_nums)
    num_2 = randint(*limit_nums)
    op = choice(list(OPERATORS.keys()))
    question = ' '.join(map(str, (num_1, op, num_2)))
    answer = str(OPERATORS[op](num_1, num_2))
    return question, answer
