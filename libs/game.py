import curses

from copy import copy
from curses import wrapper as run_cursed
from model import shapes    # application's module


SPEED = 500


def print_lines(lines, window, minrow=1, mincol=1):
    for i, line in enumerate(lines):
        window.addstr(minrow + i, mincol, line)


class Playfield(object):
    """
        Shapes container
    """

    def __init__(self, window, width, height, x=0, y=0):
        self.window = window.subwin(height * 3, width * 3, y, x)
        self.base_matrix = {(x, y): 0 for x in range(width) for y in range(height)}
        self.shape = None
        self.matrix = None

    def set_shape(self, shape):
        self.shape = shape

    def _merge(self):
        self.matrix = copy(self.base_matrix)
        if not self.shape:
            return
        for point, state in self.shape.current_state.items():
            x, y = point
            new_point = (x + self.shape.xcoord, y + self.shape.ycoord)
            self.matrix[new_point] = state

    def print(self):
        self._merge()
        self.window.clear()
        self.window.border()
        for point, state in self.matrix.items():
            if not state:
                continue
            x, y = point
            x = x + (x - 1)
            self.window.addstr(y - 1, x, '_')
            self.window.addstr(y, x - 1, '|')
            self.window.addstr(y, x, '_')
            self.window.addstr(y, x + 1, '|')
        self.window.refresh()


class Controler(object):
    """
        Gamepad
    """

    def __init__(self, window):
        self.window = window
        self.current_shape = shapes.Shape.get()

    def rotate(self):
        """ rotate current shape clockwise """
        shape = self.current_shape
        shape.state = shape.state + 1
        return shape

    def left(self):
        """ move current shape to the left """
        shape = self.current_shape
        shape.move(-1, 1)
        return shape

    def down(self):
        """ move current shape to the bottom """
        shape = self.current_shape
        shape.move(0, 1)
        return shape

    def right(self):
        """ move current shape to the right """
        shape = self.current_shape
        shape.move(1, 1)
        return shape


def run(main_window):
    curses.curs_set(0)
    side = Playfield(main_window, 17, 8)
    print_lines([
        'Welcome to Pytris',
        '             _',
        ' _          |_| ',
        '|_|    _ _  |_|  ___       _',
        '|_|_  |_|_| |_| |_|_|_   _|_|_',
        '|_|_| |_|_| |_|   |_|_| |_|_|_|',
        ], side.window)
    side.window.refresh()
    playfield = Playfield(main_window, 17, 13, x=25)
    playfield.print()
    controler = Controler(playfield.window)
    action_map = {
        'q': exit,
        'w': controler.rotate,
        'a': controler.left,
        's': controler.down,
        'd': controler.right,
    }
    playfield.window.timeout(SPEED)
    while True:
        keystroke = playfield.window.getch()
        if keystroke == curses.ERR:
            keystroke = ord('s')
        try:
            action = action_map[chr(keystroke)]
        except (KeyError, ValueError):
            continue
        try:
            shape = action()
            playfield.set_shape(shape)
            playfield.print()
        except curses.error:
            pass


def main():
    run_cursed(run)
