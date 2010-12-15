
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
    window.refresh()


class Controler(object):
    
    def __init__(self, shapes_window):
        self.shapes_window = shapes_window

    def right(self):
        #XXX move current shape to left
        shape = self.current_shape
        shape.move(3, 0)
        print_lines(shape.states[0], self.shapes_window, shape.line, shape.column)

    def left(self):
        #XXX move current shape to left
        shape = self.current_shape
        shape.move(-3, 0)
        print_lines(shape.states[0], self.shapes_window, shape.line, shape.column)

    def down(self):
        #XXX move current shape to left
        shape = self.current_shape
        shape.move(0, 1)
        print_lines(shape.states[0], self.shapes_window, shape.line, shape.column)

    def rotate(self):
        #XXX move current shape to left
        shape = self.current_shape
        states = shape.states
        states.rotate(1)

def run(main_window):
    timeout = 500
    shapetypes = (
        shapes.I,
        shapes.J,
        shapes.L,
        shapes.S,
        shapes.T,
        shapes.Z,
    )
    curses.curs_set(0)
    game_window = main_window.subwin(50, 25, 0, 0)
    print_lines([
        'Welcome to Pytris',
    ], game_window)
    shapes_window = main_window.subwin(50, 32, 0, 26)
    shapes_window.border(0)
    shapes_window.refresh()
    controler = Controler(shapes_window)
    controler.current_shape = random.choice(shapetypes)()
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
            if keystroke == -1:
                action = action_map['j']
                timeout = 500
            else:
                action = action_map[chr(keystroke)]
        except KeyError:
            pass
        else:
            action()
        shapes_window.timeout(timeout)


def main():
    run_cursed(run)

