
class Shape(object):
    column = 0
    line = 0
    states = {}
    width = 0
    height = 0

    def __init__(self):
        return self

    def move(self, moves):
        self.column += moves.horizontal
        self.line += moves.vertical


class I(Shape):
    widht = 1
    height = 4
    states = {
        1: [
            ' _ ',
            '|_|',
            '|_|',
            '|_|',
            '|_|',
        ],
        2: [
            ' _ _ _ _',
            '|_|_|_|_|',
        ],
    }

    def __init__(self):
        return self


class J(Shape):
    widht = 1
    height = 4
    states = {
        1: [
            '   _ ',
            '  |_|',
            ' _|_|',
            '|_|_|',
        ],
        2: [
            ' _ ',
            '|_|_ _',
            '|_|_|_|',
        ],
        3: [
            ' _ _',
            '|_|_|',
            '|_|',
            '|_|',
        ],
        4: [
            ' _ _ _',
            '|_|_|_|',
            '    |_|',
        ],
    }

    def __init__(self):
        return self


class L(Shape):
    widht = 1
    height = 4
    states = {
        1: [
            ' _ ',
            '|_|',
            '|_|_',
            '|_|_|',
        ],
        2: [
            ' _ _ _',
            '|_|_|_|',
            '|_|',
        ],
        3: [
            ' _ _ ',
            '|_|_|',
            '  |_|',
            '  |_|',
        ],
        4: [
            '     _ ',
            ' _ _|_|',
            '|_|_|_|',
        ],
    }

    def __init__(self):
        return self


class S(Shape):
    widht = 1
    height = 4
    states = {
        1: [
            '   _ _',
            ' _|_|_|',
            '|_|_|',
        ],
        2: [
            ' _ ',
            '|_|_',
            '|_|_|',
            '  |_|',
        ],
    }

    def __init__(self):
        return self


class Square(Shape):
    widht = 1
    height = 4
    states = {
        1: [
            ' _ _ ',
            '|_|_|',
            '|_|_|',
        ],
    }

    def __init__(self):
        return self


class T(Shape):
    widht = 1
    height = 4
    states = {
        1: [
            '   _ ',
            ' _|_|_',
            '|_|_|_|',
        ],
        2: [
            ' _ ',
            '|_|_',
            '|_|_|',
            '|_|',
        ],
        3: [
            ' _ _ _',
            '|_|_|_|',
            '  |_|  ',
        ],
        4: [
            '   _ ',
            ' _|_|',
            '|_|_|',
            '  |_|',
        ],
    }

    def __init__(self):
        return self


class Z(Shape):
    widht = 1
    height = 4
    states = {
        1: [
            ' _ _',
            '|_|_|_',
            '  |_|_|',
        ],
        2: [
            '   _ ',
            ' _|_|',
            '|_|_|',
            '|_|',
        ],
    }

    def __init__(self):
        return self

