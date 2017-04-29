#!/usr/bin/env python

"""
COLORS

Pick up the color numbers and expand your domain into the wilderness.
The one who conquers more wins )

player {player_1}: you
player {player_2}: second player or computer

Usage:
    colors
    colors 2D_size
    colors x_size y_size

"""

from __future__ import print_function

import sys

import player
import config
import colors
from game import Game
from utils import ask
from utils import clear_screen

__doc__ = __doc__.format(
    player_1=config.PLAYER_1_CHAR,
    player_2=config.PLAYER_2_CHAR,
)


def get_board_dimensions():
    if len(sys.argv) == 2:
        x = y = sys.argv[1]
    elif len(sys.argv) == 3:
        x, y = sys.argv[1:]
    else:
        x = config.DEFAULT_X_SIZE
        y = config.DEFAULT_Y_SIZE

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print(colors.warn('Dimensions are numeric, stupid'))
        sys.exit(1)

    if x < 3 or y < 3:
        print(colors.warn('Dimensions should be 3+'))
        sys.exit(1)

    return x, y


def choose_players():
    player_1 = player.HumanPlayer

    ok_computer = ask('play with computer? y/n', lambda x: (x in 'yY', x in 'yYnN'))
    if ok_computer:
        level = ask('\nEasy? 1\nDifficult? 2\n', lambda x: (int(x), int(x) in [1, 2]))
        if level == 1:
            player_2 = player.DummyAIPlayer
        elif level == 2:
            player_2 = player.SmartAIPlayer
        else:
            raise ValueError("Wrong level")
    else:
        player_2 = player.HumanPlayer

    return player_1, player_2


def main():
    clear_screen()
    print(__doc__)

    size_x, size_y = get_board_dimensions()

    try:
        player_1, player_2 = choose_players()

        while True:
            game = Game(size_x, size_y, player_1, player_2)
            game.start()

            play_again = ask('\nPlay again? y/n', lambda x: (x in 'yY', x in 'yYnN'))
            if not play_again:
                break

    except KeyboardInterrupt:
        pass

    print('\n\nBye.. & have a good day.')


if __name__ == '__main__':
    main()
