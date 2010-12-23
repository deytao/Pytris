
import curses
import random

from curses import wrapper as run_cursed
from time import time
from model import shapes  # application's module


def print_lines(lines, window, minrow=1, mincol=1):
    for i, line in enumerate(lines):
        try:
            window.addstr(minrow + i, mincol, line)
        except Exception:
            pass


class Controler(object):
    
    shape_types = (
        shapes.I,
        shapes.J,
        shapes.L,
        shapes.S,
        shapes.T,
        shapes.Z,
    )

    def __init__(self, shapes_window):
        self.shapes_window = shapes_window

    def right(self):
        #XXX move current shape to right
        shape = self.current_shape
        shape.move(3, 0)

    def left(self):
        #XXX move current shape to left
        shape = self.current_shape
        if (shape.column > 0):
            shape.move(-3, 0)

    def down(self):
        #XXX move current shape to down
        shape = self.current_shape
        shape.move(0, 1)

    def rotate(self):
        #XXX rotate current shape spinning deque states
        shape = self.current_shape
        states = shape.states
        states.rotate(1)

    def display(self, previous_ones):
        #XXX print current shape
        shape = self.current_shape
        previous_ones.append(shape)
        for i, displayed_shape in enumerate(previous_ones):
            print_lines(displayed_shape.states[0], self.shapes_window, displayed_shape.line, displayed_shape.column)

    def is_endoflines(self):
        window = self.shapes_window
        window_height, window_width = window.getmaxyx()
        shape = self.current_shape
        return (shape.line + len(shape.states[0]) >= window_height - 1)

    def renew_shape(self):
        self.current_shape = random.choice(self.shape_types)()


def run(main_window):
    timeout = 500
    previous_shapes = []
    curses.curs_set(0)
    game_window = main_window.subwin(50, 25, 0, 0)
    print_lines([
        'Welcome to Pytris',
    ], game_window)
    shapes_window = main_window.subwin(50, 32, 0, 26)
    shapes_window.border(0)
    shapes_window.refresh()
    controler = Controler(shapes_window)
    controler.renew_shape()
    action_map = {
        'q': exit,
        'l': controler.right,
        'h': controler.left,
        'j': controler.down,
        'k': controler.rotate,
    }
    shapes_window.timeout(timeout)
    while True:
        start_time = time()
        keystroke = shapes_window.getch()  # blocking call, returning -1 after timeout delay
        end_time = time()
        wait_time = (end_time - start_time) * 1000
        timeout -= wait_time
        shapes_window.clear()
        shapes_window.border(0)
        try:
            action = action_map[chr(keystroke)]
        except ValueError:
            controler.down()
            timeout = 500
        except KeyError:
            pass
        else:
            action()
        if (controler.is_endoflines()):
            previous_shapes.append(controler.current_shape)
            controler.renew_shape()
        controler.display(previous_shapes)
        shapes_window.timeout(int(timeout))
        shapes_window.refresh()


def main():
    run_cursed(run)

