#!/usr/bin/env python3
"""
mkproject.py

[not so] simple script to scaffold small programming projects.

Port of 'mkproject' (Bash).

"""


NORMAL = 0
BOLD = 1
DIM = 2
ITALIC = 3
UNDERLINE = 4
BLINK = 5
_ = 6
REVERSE = 7
HIDDEN = 8
STRIKETHROUGH = 9


COLOUR_0 = BLACK = 30
COLOUR_1 = RED = 31
COLOUR_2 = green =  32
COLOUR_3 = yellow =  33
COLOUR_4 = blue = 34
COLOUR_5 = pink =  35
COLOUR_6 = cyan =  36
COLOUR_7 = grey = 37
COLOUR_8 = white =  38
COLOUR_DEFAULT = default_fg =39


def ansify(codes: list[int]) -> str:
    elems = ["\x1b["]
    for c in codes:
        elems.append(str(c))
        elems.append(";")
    elems.pop()
    elems.append("m")

    return "".join(elems)
