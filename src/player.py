from __future__ import print_function
from collections import Counter
from copy import deepcopy as copy

from utils import ask
from positioning import resolve_real_position
from positioning import Movements
import colors


class BasePlayer(object):
    def __init__(self, symbol, game, position):
        base_cell = resolve_real_position(game.board.size_x, game.board.size_y, position)
        self.symbol = symbol
        self.game = game

        self.queue = [base_cell]
        self.domain = set()
        self.frontier = set()

        self.other_player = None
        self.color = self.game.board.get(base_cell)

    def init(self):
        self.other_player = self.game.player_2 if self.game.player_1 is self else self.game.player_1
        self.conquer(self.color)

    @property
    def domain_area(self):
        return len(self.domain)

    def is_victorious(self):
        return self.domain_area > self.game.board.area / 2

    def is_stuck(self):
        return len(self.frontier) == 0

    def scout_around(self, cell):
        x, y = cell
        for delta_x, delta_y in Movements.keys():

            x_ = x + delta_x
            if self.game.board.size_x <= x_ or x_ < 0:
                continue

            y_ = y + delta_y
            if self.game.board.size_y <= y_ or y_ < 0:
                continue

            next_cell = (x_, y_)
            if next_cell in self.other_player.domain or next_cell in self.domain:
                continue

            self.queue.append(next_cell)

    def revise_frontier(self):
        for cell in list(self.frontier):
            if cell in self.other_player.domain:
                self.frontier.remove(cell)

    def conquer(self, color):
        self.color = color

        self.revise_frontier()
        self.queue.extend(self.frontier)
        self.frontier.clear()

        while self.queue:
            cell = self.queue.pop(0)
            cell_color = self.game.board.get(cell)

            if cell_color == self.color:
                if cell not in self.domain:
                    self.domain.add(cell)
                    self.scout_around(cell)

            else:  # cell_color not in self.other_player.domain:
                self.frontier.add(cell)


class HumanPlayer(BasePlayer):
    def next_color(self):
        picked_color = ask(
            '%s. pick up number: ' % self.symbol,
            lambda x: (int(x), 0 < int(x) <= self.game.COLOR_RANGE)
        )

        if picked_color == self.color:
            self.game.illustrate()
            print(colors.warn('You already own the color. Choose a different one.'))
            return self.next_color()

        return picked_color


class BaseAIPlayer(BasePlayer):
    def _rate_frontier(self):
        raise NotImplementedError

    def next_color(self):
        self.revise_frontier()

        try:
            return self._rate_frontier()[0]
        except IndexError:
            return -1


class DummyAIPlayer(BaseAIPlayer):
    def _rate_frontier(self):
        frontier_color_histogram = Counter(map(self.game.board.get, self.frontier))
        return [x for x, _ in frontier_color_histogram.most_common()]


class SmartAIPlayer(BaseAIPlayer):
    def _rate_frontier(self):
        domain_color_histogram = Counter()

        domain_ = copy(self.domain)
        frontier_ = copy(self.frontier)

        for color in set(map(self.game.board.get, self.frontier)):
            self.conquer(color)
            domain_color_histogram[color] = self.domain_area

            self.domain = copy(domain_)
            self.frontier = copy(frontier_)

        return [x for x, _ in domain_color_histogram.most_common()]
