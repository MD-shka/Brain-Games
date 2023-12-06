from prompt import string
from brain_games.cli import welcome_user


ROUND = 3


def run_game(game):
    player = welcome_user()
    print(game.RULES)
    for i in range(ROUND):
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        player_answer = string('Your answer: ')
        if player_answer != answer:
            return print(f'"{player_answer}" is wrong answer ;(. '
                         f'Correct answer was "{answer}".\n'
                         f'Let\'s try again, {player}!')
        print('Correct!')
    return print(f'Congratulations, {player}!')
