#!/usr/bin/env python3
"""
mkproject.py

[not so] simple script to scaffold small programming projects.

Port of 'mkproject' (Bash).

"""


from enum import Enum


class Style(Enum):
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


class Colour(Enum):
    COLOUR_0 = 0
    COLOUR_1 = 1
    COLOUR_2 = 2
    COLOUR_3 = 3
    COLOUR_4 = 4
    COLOUR_5 = 5
    COLOUR_6 = 6
    COLOUR_7 = 7
    COLOUR_8 = 8
    COLOUR_DEFAULT = 9


def ansify(codes: list[int]) -> str:
    elems = ["\x1b["]
    for c in codes:
        elems.append(str(c))
        elems.append(";")
    elems.pop()
    elems.append("m")

    return "".join(elems)
