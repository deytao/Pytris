#!/usr/bin/env python

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


def draw_game_area(std):
    curses.noecho()
    curses.cbreak()
    std.keypad(1)

    std.addstr(12, 25, 'Here we go !')
    std.refresh()
    std.getch()


def close_game_area(std):
    curses.nocbreak()
    std.keypad(0)
    curses.echo()
    curses.endwin()


def main():
    print('Welcome in Pytris')
    print('             _  ')
    print(' _          |_| ')
    print('|_|    _ _  |_|  ___       _')
    print('|_|_  |_|_| |_| |_|_|_   _|_|_')
    print('|_|_| |_|_| |_|   |_|_| |_|_|_|')

    stdscr = curses.initscr()
    
    draw_game_area(stdscr)
    close_game_area(stdscr)


if __name__ == '__main__':
    main()

