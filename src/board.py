from __future__ import print_function
from random import randint

from .utils import clear_screen
from . import colors


class Board(object):
    def __init__(self, size_x, size_y, color_range):
        self.size_x = size_x
        self.size_y = size_y
        self.area = size_x * size_y
        self.board = [[randint(1, color_range) for _ in range(size_x)] for _ in range(size_y)]

    def get(self, cell):
        x, y = cell
        return self.board[y][x]

    def illustrate(self, players):
        clear_screen()

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):

                for player in players:
                    if (x, y) in player.domain:
                        print(colors.color_text(colors.keys[player.color], player.symbol), end=' ')
                        break
                else:
                    print(colors.color_text(colors.keys[cell], cell), end=' ')

            print()
        print()
