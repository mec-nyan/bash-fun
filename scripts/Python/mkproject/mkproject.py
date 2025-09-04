#!/usr/bin/env python3
"""
mkproject.py

[not so] simple script to scaffold small programming projects.

Port of 'mkproject' (Bash).

"""

import random
import sys
import termios
import tty


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
COLOUR_2 = GREEN = 32
COLOUR_3 = YELLOW = 33
COLOUR_4 = BLUE = 34
COLOUR_5 = PINK = 35
COLOUR_6 = CYAN = 36
COLOUR_7 = GREY = 37
COLOUR_8 = WHITE = 38
COLOUR_DEFAULT = DEFAULT_FG = 39


def ansify(codes: list[int]) -> str:
    elems = ["\x1b["]
    for c in codes:
        elems.append(str(c))
        elems.append(";")
    elems.pop()
    elems.append("m")

    return "".join(elems)


def fruit_me() -> str:
    fruits = ["🍒" "🍑" "🍌" "🍎" "🍏" "🍇" "🍊" "🍍" "🥝" "🍉" "🍈" "🍋" "🍐" "🍓"
              ]
    return random.choice(fruits)


def log_me(message: str, level: str) -> None:
    match level:
        case "info":
            sys.stdout.write(
                f"{ansify([BLUE])} {ansify([ITALIC, GREEN])}{message}"
            )
        case "warning":
            sys.stdout.write(
                f"{ansify([YELLOW])} {ansify([ITALIC, RED])}{message}"
            )
    sys.stdout.write(f"{ansify([NORMAL])}\n")


def get_ch() -> str:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def ask_yes_or_no(prompt: str, message: str, default: str = "no") -> bool:
    fruit = fruit_me()

    sys.stdout.write(f"{fruit} {prompt} (y/n) (default: {default}) ")

    tries = 0

    while True:
        tries += 1

        answer = get_ch()

        if answer == "\n":
            sys.stdout.write(
                f"    {ansify([GREEN])}{message}{ansify([NORMAL])}")
            match default.lower():
                case "y" | "yes":
                    return True
                case "n" | "no":
                    return False
                case _:
                    return False
        elif answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            sys.stdout.write("\ny/n? ")

        if tries == 3:
            sys.stdout.write(f"{ansify([DIM, YELLOW])}Fuck it!"
                             f"Falling back to defaults.\n{ansify([NORMAL])}")
