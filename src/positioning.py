class Movements(object):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    @classmethod
    def keys(cls):
        return [cls.UP, cls.RIGHT, cls.DOWN, cls.LEFT]


class Positions(object):
    TOP_RIGHT = 1
    BOTTOM_RIGHT = 2
    BOTTOM_LEFT = 3
    TOP_LEFT = 4


def resolve_real_position(size_x, size_y, rel_pos):
    size_x -= 1
    size_y -= 1

    position = {
        Positions.TOP_RIGHT: (size_x, 0),
        Positions.BOTTOM_RIGHT: (size_x, size_y),
        Positions.BOTTOM_LEFT: (0, size_y),
        Positions.TOP_LEFT: (0, 0),
    }[rel_pos]

    return position
