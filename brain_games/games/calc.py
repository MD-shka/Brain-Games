import random
import operator


operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def show_rules():
    return 'What is the result of the expression?'


def solution():
    expression = (random.randint(1, 999),
                  random.choice(("+", "-", "*")),
                  random.randint(1, 999))
    question = ' '.join(map(str, expression))
    answer = str(operators[expression[1]](expression[0], expression[2]))
    return question, answer
