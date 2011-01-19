
from collections import deque


class Shape(object):
    column = 1
    line = 0
    state = []
    states = ()
    width = 0
    height = 0

    def move(self, hspan, vspan):
        self.column += hspan
        self.line += vspan


class I(Shape):
    widht = 1
    height = 4
    states = deque((
        [
            ' _ ',
            '|_|',
            '|_|',
            '|_|',
            '|_|',
        ],
        [
            ' _ _ _ _',
            '|_|_|_|_|',
        ],
    ))


class J(Shape):
    widht = 1
    height = 4
    states = deque((
        [
            '   _ ',
            '  |_|',
            ' _|_|',
            '|_|_|',
        ],
        [
            ' _ ',
            '|_|_ _',
            '|_|_|_|',
        ],
        [
            ' _ _',
            '|_|_|',
            '|_|',
            '|_|',
        ],
        [
            ' _ _ _',
            '|_|_|_|',
            '    |_|',
        ],
    ))


class L(Shape):
    widht = 1
    height = 4
    states = deque((
        [
            ' _ ',
            '|_|',
            '|_|_',
            '|_|_|',
        ],
        [
            ' _ _ _',
            '|_|_|_|',
            '|_|',
        ],
        [
            ' _ _ ',
            '|_|_|',
            '  |_|',
            '  |_|',
        ],
        [
            '     _ ',
            ' _ _|_|',
            '|_|_|_|',
        ],
    ))


class S(Shape):
    widht = 1
    height = 4
    states = deque((
        [
            '   _ _',
            ' _|_|_|',
            '|_|_|',
        ],
        [
            ' _ ',
            '|_|_',
            '|_|_|',
            '  |_|',
        ],
    ))


class Square(Shape):
    widht = 1
    height = 4
    states = deque((
        [
            ' _ _ ',
            '|_|_|',
            '|_|_|',
        ],
    ))


class T(Shape):
    widht = 1
    height = 4
    states = deque((
        [
            '   _ ',
            ' _|_|_',
            '|_|_|_|',
        ],
        [
            ' _ ',
            '|_|_',
            '|_|_|',
            '|_|',
        ],
        [
            ' _ _ _',
            '|_|_|_|',
            '  |_|  ',
        ],
        [
            '   _ ',
            ' _|_|',
            '|_|_|',
            '  |_|',
        ],
    ))


class Z(Shape):
    widht = 1
    height = 4
    states = deque((
        [
            ' _ _',
            '|_|_|_',
            '  |_|_|',
        ],
        [
            '   _ ',
            ' _|_|',
            '|_|_|',
            '|_|',
        ],
    ))

