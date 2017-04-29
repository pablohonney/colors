from colors.src.player import DummyAIPlayer, SmartAIPlayer
from colors.src.board import Board
from colors.src.game import Game
import colors.src.config as config

Board.illustrate = lambda *x: None

Player_1 = DummyAIPlayer
Player_2 = SmartAIPlayer

outcomes = []
for sizes in range(3, 40, 1):
    for _ in range(2):
        game = Game(sizes, sizes, Player_1, Player_2)
        game.loop()
        outcomes.append(game.winner)

winners = [winner.symbol for winner in outcomes if winner]


def get_percent(a):
    return a*100/len(outcomes)

print '{:15}: {}\n{:15}: {}\n{:15}: {}'.format(
    Player_1.__name__,
    get_percent(winners.count(config.PLAYER_1_CHAR)),
    'Draws',
    get_percent(len(outcomes) - len(winners)),
    Player_2.__name__,
    get_percent(winners.count(config.PLAYER_2_CHAR)),
)
