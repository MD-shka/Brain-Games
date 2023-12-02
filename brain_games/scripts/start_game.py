#!/usr/bin/env python3
import sys
from brain_games import engine
from brain_games.games import even, calc, gcd


def brain_even():
    engine.game_engine(even)


def brain_calc():
    engine.game_engine(calc)


def brain_gcd():
    engine.game_engine(gcd)


if __name__ == '__main__':
    if sys.argv[0] == 'brain-even':
        brain_even()

    elif sys.argv[0] == 'brain-calc':
        brain_calc()

    elif sys.argv[0] == 'brain-gcd':
        brain_gcd()
