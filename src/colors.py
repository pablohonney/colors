RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
VIOLET = '\033[95m'
WHITE = ''

BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CLEAR = '\033[0m'

keys = [RED, GREEN, YELLOW, BLUE, VIOLET, WHITE]


def color_text(color, text):
    return '%s%s%s' % (color, text, CLEAR)


def warn(text):
    return color_text(RED, text)


def success(text):
    return color_text(GREEN, text)
