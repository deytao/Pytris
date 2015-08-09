import curses

from copy import copy
from curses import wrapper as run_cursed
from model import shapes    # application's module


SPEED = 500


def print_lines(lines, window, minrow=1, mincol=1):
    for i, line in enumerate(lines):
        window.addstr(minrow + i, mincol, line)


class ShapeLanded(Exception):
    pass


class Playfield(object):
    """
        Shapes container
    """

    def __init__(self, window, width, height, lng=0, lat=0):
        self.window = window.subwin(height, width, lat, lng)
        self.base_matrix = {(lng, lat): 0 for lng in range(width) for lat in range(height)}
        self.fixed_matrix = {(lng, lat): 1 for lng in range(width) for lat in range(height - 1, height)}

    def intersects(self, shape):
        if not shape:
            return False
        return set(self.fixed_matrix.keys()) & set(shape.matrix.keys())

    def print_point(self, point):
        lng, lat = point
        lng = lng + (lng - 1)
        self.window.addstr(lat - 1, lng, '_')
        self.window.addstr(lat, lng - 1, '|')
        self.window.addstr(lat, lng, '_')
        self.window.addstr(lat, lng + 1, '|')

    def print(self, shape=None):
        matrix = copy(self.base_matrix)
        if self.intersects(shape):
            self.fixed_matrix.update(shape.matrix)
            raise ShapeLanded()
        else:
            matrix.update(shape.matrix if shape else {})
        matrix.update(self.fixed_matrix)
        self.window.clear()
        self.window.border()
        for point, state in matrix.items():
            if not state:
                continue
            try:
                self.print_point(point)
            except curses.error:
                continue
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
    side = Playfield(main_window, 50, 24)
    print_lines([
        'Welcome to Pytris',
        '             _',
        ' _          |_| ',
        '|_|    _ _  |_|  ___       _',
        '|_|_  |_|_| |_| |_|_|_   _|_|_',
        '|_|_| |_|_| |_|   |_|_| |_|_|_|',
        ], side.window)
    side.window.refresh()
    playfield = Playfield(main_window, 50, 40, lng=25)
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
            playfield.print(shape)
        except ShapeLanded:
            controler.current_shape = shapes.Shape.get()
        except curses.error:
            pass


def main():
    run_cursed(run)
