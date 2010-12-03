#!/usr/bin/env python

import curses

from curses import wrapper as run_cursed


def print_lines(lines, window, minrow=1, mincol=1):
    for i, line in enumerate(lines):
        window.addstr(minrow + i, mincol, line)
    window.refresh()


class Controler(object):
    
    def __init__(self, shapes_window):
        self.shapes_window = shapes_window
        #self.current_shape = None

    def right(self):
        #XXX move current shape to left
        print_lines(['To the rigth!'], self.shapes_window, 30, 10)

    def left(self):
        #XXX move current shape to left
        print_lines(['To the left!'], self.shapes_window, 30, 10)

    def down(self):
        #XXX move current shape to left
        print_lines(['Faaaaaalling!'], self.shapes_window, 30, 10)


def run(main_window):
    curses.curs_set(0)
    game_window = main_window.subwin(50, 25, 0, 0)
    print_lines([
        'Welcome to Pytris',
        '             _',
        ' _          |_| ',
        '|_|    _ _  |_|  ___       _',
        '|_|_  |_|_| |_| |_|_|_   _|_|_',
        '|_|_| |_|_| |_|   |_|_| |_|_|_|',
    ], game_window)
    shapes_window = main_window.subwin(50, 32, 0, 26)
    shapes_window.border()
    shapes_window.refresh()
    controler = Controler(shapes_window)
    action_map = {
        'q': exit,
        'o': controler.right,
        'p': controler.left,
        'l': controler.down,
    }
    while True:
        keystroke = shapes_window.getch()  # blocking call
        try:
            action = action_map[chr(keystroke)]
        except KeyError:
            pass
        else:
            action()


def main():
    run_cursed(run)


if __name__ == '__main__':
    main()

