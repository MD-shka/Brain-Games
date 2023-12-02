#!/usr/bin/env python3
import sys
from brain_games import engine
from brain_games.games import even


def brain_even():
    engine.game_engine(even)


if __name__ == '__main__':
    if sys.argv[0] == 'brain-even':
        brain_even()
