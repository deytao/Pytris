#!/usr/bin/env python

from __future__ import with_statement

import curses

from curses.wrapper import wrapper as run_cursed


def print_lines(lines, window, minrow=1, mincol=1):
    for i, line in enumerate(lines):
        window.addstr(minrow + i, mincol, line)
    window.refresh()


class Controler(object):
    
    def __init__(self, game_window):
        self.game_window = game_window
        #self.current_shape = None

    def right(self):
        #XXX move current shape to left
        print_lines(['To the rigth!'], self.game_window, 30, 10)

    def left(self):
        #XXX move current shape to left
        print_lines(['To the left!'], self.game_window, 30, 10)

    def down(self):
        #XXX move current shape to left
        print_lines(['Faaaaaalling!'], self.game_window, 30, 10)


def run(main_window):
    print_lines([
        'Welcome to Pytris',
        '',
        ' _          |_| ',
        '|_|    _ _  |_|  ___       _',
        '|_|_  |_|_| |_| |_|_|_   _|_|_',
        '|_|_| |_|_| |_|   |_|_| |_|_|_|',
    ], main_window)
    game_window = curses.newwin(50, 40, 1, 40)
    game_window.border()
    game_window.refresh()
    controler = Controler(game_window)
    action_map = {
        'q': exit,
        'o': controler.right,
        'p': controler.left,
        'l': controler.down,
    }
    while True:
        keystroke = main_window.getch()  # blocking call
        chrstroke = chr(keystroke)
        if chrstroke in action_map:
            action = action_map[chr(keystroke)]
            action()


def main():
    run_cursed(run)


if __name__ == '__main__':
    main()

