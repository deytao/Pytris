#!/usr/bin/env python

import os
import curses

SHAPE_TYPE_SQUARE = 101
SHAPE_TYPE_BAR = 102
SHAPE_TYPE_L = 103
SHAPE_TYPE_Z = 104
SHAPE_TYPE_S = 105


class Shape():
    id = 0
    type = 0
    pos_x = 0
    pos_y = 0

    def __init__(self):
        return self

    def move(self):
        return self


class Square(Shape):
    id = 0
    type = SHAPE_TYPE_SQUARE

    def __int__(self):
        return self


class Bar(Shape):
    id = 0
    type = SHAPE_TYPE_BAR

    def __int__(self):
        return self


def draw_game_area(scr):
    shapescr = scr.subwin(0, 50)
    shapescr.border(0)
    shapescr.refresh()

    return shapescr


#def close_game_area(std):


shapes = []
def main():
    gamescr = curses.initscr()
    gamescr.keypad(1)
    gamescr.addstr(1, 1, 'Welcome to Pytris')
    gamescr.addstr(2, 1, '             _  ')
    gamescr.addstr(3, 1, ' _          |_| ')
    gamescr.addstr(4, 1, '|_|    _ _  |_|  ___       _')
    gamescr.addstr(5, 1, '|_|_  |_|_| |_| |_|_|_   _|_|_')
    gamescr.addstr(6, 1, '|_|_| |_|_| |_|   |_|_| |_|_|_|')
    gamescr.refresh()
    gamescr.timeout(500)

    curses.noecho()
    curses.cbreak()

    shapearea = draw_game_area(gamescr)
    shapearea.timeout(500)
    while True:
        c = shapearea.getch() 
        shapearea.clear()

        if c == ord('q'):
            break
        elif c == ord('o'):
            shapearea.addstr(30, 30, 'To the right !')
        elif c == ord('p'):
            shapearea.addstr(30, 30, 'To the left !')
        elif c == ord('l'):
            shapearea.addstr(30, 30, 'Faaaaaalling !')

        shapearea.refresh()

    gamescr.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    main()

