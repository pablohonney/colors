from __future__ import print_function

from itertools import cycle

import config
from . import colors
from .board import Board
from .player import BaseAIPlayer
from .positioning import Positions


class Game(object):
    COLOR_RANGE = len(colors.keys) - 1

    def __init__(self, size_x, size_y, player_1_cls, player_2_cls):

        self.board = Board(size_x, size_y, self.COLOR_RANGE)
        self.player_1 = player_1_cls(config.PLAYER_1_CHAR, self, Positions.BOTTOM_LEFT)
        self.player_2 = player_2_cls(config.PLAYER_2_CHAR, self, Positions.TOP_RIGHT)
        self.players = [self.player_1, self.player_2]

        self.player_1.init()
        self.player_2.init()
        self.winner = None

    def loop(self):

        self.illustrate()

        for player in cycle(self.players):

            # assert no condominium
            assert not self.player_1.domain.intersection(self.player_2.domain)

            if player.is_stuck():
                if player.other_player.is_stuck():
                    self.winner = None
                    return

                self.winner = player.other_player
                return

            next_color = player.next_color()
            if next_color == -1:
                self.winner = player.other_player
                return

            player.conquer(next_color)
            self.illustrate()

            if player.is_victorious():
                self.winner = player
                return

    @staticmethod
    def get_victory_msg(player):
        if isinstance(player, BaseAIPlayer):
            return colors.warn('%s WINS !' % player.symbol)
        else:
            return colors.success('%s WINS !' % player.symbol)

    def illustrate(self):
        self.board.illustrate(self.players)

    def start(self):
        self.loop()
        if self.winner:
            print(self.get_victory_msg(self.winner))
        else:
            print('No winner (')
