#!/usr/bin/env python

import os
import curses


shapes = []


def create_infosarea(area):
    subwin = area.subwin(100, 40, 1, 1)
    subwin.addstr(1, 1, 'Welcome to Pytris')
    subwin.addstr(2, 1, '             _  ')
    subwin.addstr(3, 1, ' _          |_| ')
    subwin.addstr(4, 1, '|_|    _ _  |_|  ___       _')
    subwin.addstr(5, 1, '|_|_  |_|_| |_| |_|_|_   _|_|_')
    subwin.addstr(6, 1, '|_|_| |_|_| |_|   |_|_| |_|_|_|')
    subwin.refresh()
    return subwin


def create_shapesarea(area):
    subwin = area.subwin(100, 16, 1, 40)
    return subwin


def main():
    try:
        mainarea = curses.initscr()
        mainarea.keypad(1)
        mainarea.refresh()
        curses.noecho()
        curses.cbreak()
        infosarea = create_infosarea(mainarea)
        shapesarea = create_shapesarea(mainarea)
        shapesarea.timeout(500)
        while True:
            shapesarea.border(0)
            shapesarea.refresh()
            c = shapesarea.getch()
            shapesarea.clear()
            if c == ord('q'):
                break
            elif c == ord('o'):
                shapesarea.addstr(30, 30, 'To the right !')
            elif c == ord('p'):
                shapesarea.addstr(30, 30, 'To the left !')
            elif c == ord('l'):
                shapesarea.addstr(30, 30, 'Faaaaaalling !')
            shapesarea.refresh()
    except Exception as inst:
        raise
    finally:
        mainarea.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()


if __name__ == '__main__':
    main()

