import curses

import copy
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
        self.fixed_matrix = {(lng, lat): '#' for lng in range(width) for lat in range(height - 1, height)}

    def intersects(self, shape):
        if not shape:
            return False
        return set(self.fixed_matrix.keys()) & set(shape.matrix.keys())

    def print_point(self, point, char):
        lng, lat = point
        self.window.addstr(lat, lng, char)

    def print_(self, shape):
        matrix = {}
        matrix.update(self.fixed_matrix)
        matrix.update(shape.matrix)
        self.window.clear()
        self.window.border()
        for point, state in sorted(matrix.items()):
            if not state:
                continue
            self.print_point(point, state)
        self.window.refresh()


class Controler(object):
    """
        Gamepad
    """

    def __init__(self, window):
        self.window = window

    def rotate(self, playfield, shape):
        """ rotate current shape clockwise """
        duped = copy.deepcopy(shape)
        shape.state = shape.state + 1
        if playfield.intersects(shape):
            playfield.fixed_matrix.update({k: '%' for k in duped.matrix})
            shape = shapes.Shape.get()
        return shape

    def left(self, playfield, shape):
        """ move current shape to the left """
        duped = copy.deepcopy(shape)
        shape.move(-1, 1)
        if playfield.intersects(shape):
            playfield.fixed_matrix.update({k: '%' for k in duped.matrix})
            shape = shapes.Shape.get()
        return shape

    def down(self, playfield, shape):
        """ move current shape to the bottom """
        duped = copy.deepcopy(shape)
        shape.move(0, 1)
        if playfield.intersects(shape):
            playfield.fixed_matrix.update({k: '%' for k in duped.matrix})
            shape = shapes.Shape.get()
        return shape

    def right(self, playfield, shape):
        """ move current shape to the right """
        duped = copy.deepcopy(shape)
        shape.move(1, 1)
        if playfield.intersects(shape):
            playfield.fixed_matrix.update({k: '%' for k in duped.matrix})
            shape = shapes.Shape.get()
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
    shape = shapes.Shape.get()
    playfield = Playfield(main_window, 50, 40, lng=25)
    try:
        playfield.print_(shape)
    except curses.error:
        pass
    controler = Controler(playfield.window)
    action_map = {
        'q': lambda pf, s: exit(0),
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
            shape = action(playfield, shape)
            playfield.print_(shape)
        except ShapeLanded:
            shape = shapes.Shape.get()
        except curses.error:
            pass


def main():
    run_cursed(run)
