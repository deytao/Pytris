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


def draw_game_area(std):
    curses.noecho()
    curses.cbreak()

    std.keypad(1)
    std.border(0)
    std.addstr(1, 1, 'Welcome to Pytris')
    std.addstr(2, 1, '             _  ')
    std.addstr(3, 1, ' _          |_| ')
    std.addstr(4, 1, '|_|    _ _  |_|  ___       _')
    std.addstr(5, 1, '|_|_  |_|_| |_| |_|_|_   _|_|_')
    std.addstr(6, 1, '|_|_| |_|_| |_|   |_|_| |_|_|_|')
    std.refresh()


def close_game_area(std):
    curses.nocbreak()
    std.keypad(0)
    curses.echo()
    curses.endwin()


def main():

    stdscr = curses.initscr()
    
    draw_game_area(stdscr)

    c = 0
    while 1:
        c = stdscr.getch() 
        if c == ord('q'):
            break
        elif c == ord('g'):
            stdscr.addstr(30, 30, 'Here we go !')
            stdscr.refresh()
        elif c == ord('j'):
            stdscr.addstr(30, 30, 'Oh No !')
            stdscr.refresh()

    close_game_area(stdscr)


if __name__ == '__main__':
    main()

