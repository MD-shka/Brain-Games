#!/usr/bin/env python3
import sys
import os
from typing import Dict
from brain_games import engine
from brain_games.games import even, calc, gcd, progression, prime


game_names: Dict[str, callable] = {
    'brain-even': even,
    'brain-calc': calc,
    'brain-gcd': gcd,
    'brain-progression': progression,
    'brain-prime': prime,
}


def main():
    game_name = game_names.get(os.path.basename(sys.argv[0]))
    engine.game_engine(game_name)


if __name__ == '__main__':
    main()
