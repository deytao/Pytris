import curses

from curses import wrapper as run_cursed
from model import shapes    # application's module


SPEED = 500


def print_lines(lines, window, minrow=1, mincol=1):
    for i, line in enumerate(lines):
        window.addstr(minrow + i, mincol, line)
    window.refresh()


class Controler(object):
    
    def __init__(self, shapes_window):
        self.shapes_window = shapes_window
        self.current_shape = shapes.Shape.get()

    def rotate(self):
        """ rotate current shape clockwise """
        shape = self.current_shape
        shape.state = shape.state + 1
        print_lines(shape.current_state, self.shapes_window, shape.line, shape.column)

    def left(self):
        """ move current shape to the left """
        shape = self.current_shape
        shape.move(-(shape.width), 1)
        print_lines(shape.current_state, self.shapes_window, shape.line, shape.column)

    def down(self):
        """ move current shape to the bottom """
        shape = self.current_shape
        shape.move(0, 1)
        print_lines(shape.current_state, self.shapes_window, shape.line, shape.column)

    def right(self):
        """ move current shape to the right """
        shape = self.current_shape
        shape.move(shape.width, 1)
        print_lines(shape.current_state, self.shapes_window, shape.line, shape.column)


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
        'w': controler.rotate,
        'a': controler.left,
        's': controler.down,
        'd': controler.right,
    }
    shapes_window.timeout(SPEED)
    while True:
        keystroke = shapes_window.getch()
        if keystroke == curses.ERR:
            keystroke = ord('s')
        try:
            action = action_map[chr(keystroke)]
        except (KeyError, ValueError):
            continue
        try:
            shapes_window.clear()
            shapes_window.border()
            action()
        except curses.error:
            pass


def main():
    run_cursed(run)
