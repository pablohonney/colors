from __future__ import print_function
import platform
import os
import sys

from . import colors

if sys.version_info < (3, 0):
    input = raw_input


def clear_screen():
    os_ = platform.system()
    if os_ == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def ask(question, check_func=None):
    while True:
        try:
            answer = input(question)
            if check_func:
                answer, ok = check_func(answer)
                if not ok:
                    raise ValueError

            return answer
        except Exception:
            print(colors.warn('Invalid input. Try again'))
