#!/usr/bin/env python

import os
import curses


def create_game_area(scr):
    shapescr = scr.subwin(100, 16, 0, 40)
    return shapescr


#def close_game_area(std):


shapes = []
def main():
    try:
        gamearea = curses.initscr()
        gamearea.keypad(1)
        gamearea.addstr(1, 1, 'Welcome to Pytris')
        gamearea.addstr(2, 1, '             _  ')
        gamearea.addstr(3, 1, ' _          |_| ')
        gamearea.addstr(4, 1, '|_|    _ _  |_|  ___       _')
        gamearea.addstr(5, 1, '|_|_  |_|_| |_| |_|_|_   _|_|_')
        gamearea.addstr(6, 1, '|_|_| |_|_| |_|   |_|_| |_|_|_|')
        gamearea.refresh()

        curses.noecho()
        curses.cbreak()

        shapearea = create_game_area(gamearea)
        shapearea.timeout(500)
        while True:
            shapearea.border(0)
            shapearea.refresh()
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
        break
    except Exception:
        pass
    finally:
        gamearea.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()


if __name__ == '__main__':
    main()

