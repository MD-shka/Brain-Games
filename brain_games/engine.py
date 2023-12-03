from brain_games import cli


def game_engine(game):
    player = cli.welcome_user()
    player_answer = ''
    answer = ''
    result = (f'"{player_answer}" is wrong answer ;(. Correct answer was '
              f'"{answer}".\nLet\'s try again, {player}!',
              f'Congratulations, {player}!')
    for i in range(3):
        if i == 0:
            print(game.show_rules())
        question, answer = game.solution()
        print(f'Question: {question}')
        player_answer = input('Your answer: ')
        if player_answer != answer:
            break
        print('Correct!')
    print(result[player_answer == answer])
