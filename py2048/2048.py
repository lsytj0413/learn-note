# coding=utf-8

import curses
from random import randrange, choice
from collections import defaultdict


actions = [
    'Up',
    'Left',
    'Down',
    'Right',
    'Restart',
    'Exit'
]

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
print letter_codes

action_dict = dict(zip(letter_codes, actions * 2))
print action_dict
