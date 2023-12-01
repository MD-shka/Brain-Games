import random
from brain_games import cli


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def selection_result(player_answer, answer, name):
    if player_answer == answer:
        return f'Congratulations, {name}!'
    return (f'"{player_answer}" is wrong answer ;(. Correct answer'
            f' was "{answer}".\nLet\'s try again, {name}!')


def check_even():
    player = cli.welcome_user()
    player_answer = ''
    answer = ''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = random.randint(1, 999)
        print(f'Question: {num}')
        player_answer = input('Your answer: ').lower()
        answer = is_even(num)
        if player_answer != answer:
            break
        print('Correct!')
    print((selection_result(player_answer, answer, player)))


def main():
    check_even()


if __name__ == '__main__':
    main()
