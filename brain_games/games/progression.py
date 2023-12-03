import random


def show_rules():
    return 'What number is missing in the progression?'


def solution():
    start = random.randint(1, 100)
    step = random.randint(2, 99)
    nums = []

    for _ in range(random.randint(5, 10)):
        nums.append(start + step)
        start = nums[-1]
    answer = str(random.choice(nums))
    question = (' '.join(map(str, nums))).replace(answer, '..')
    return question, answer
