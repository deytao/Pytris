#!/usr/bin/env python

import curses


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

