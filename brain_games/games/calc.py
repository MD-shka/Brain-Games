import random
import operator


operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def show_rules():
    return 'What is the result of the expression?'


def make_question():
    return (f'{random.randint(1, 999)} '
            f'{random.choice(("+", "-", "*"))} '
            f'{random.randint(1, 999)}')


def check_answer(expression):
    expression = expression.split()
    return str(operators[expression[1]](int(expression[0]), int(expression[2])))
