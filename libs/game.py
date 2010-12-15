
import curses
import random

from curses import wrapper as run_cursed
from model import shapes    # application's module


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
        '             _',
        ' _          |_| ',
        '|_|    _ _  |_|  ___       _',
        '|_|_  |_|_| |_| |_|_|_   _|_|_',
        '|_|_| |_|_| |_|   |_|_| |_|_|_|',
    ], game_window)
    shapes_window = main_window.subwin(50, 32, 0, 26)
    shapes_window.timeout(500)
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
    while True:
        keystroke = shapes_window.getch()  # blocking call, returning -1 after timeout delay
        shapes_window.clear()
        shapes_window.border(0)
        try:
            if keystroke == -1:
                action = action_map['j']
            else:
                action = action_map[chr(keystroke)]
        except KeyError:
            pass
        else:
            action()


def main():
    run_cursed(run)

