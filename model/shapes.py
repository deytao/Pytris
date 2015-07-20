import random

class Shape(object):
    column = 0
    line = 0
    states = ()
    _state = 0

    def move(self, hspan, vspan):
        self.column += hspan
        self.line += vspan

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        try:
            self.states[value]
            self._state = value
        except IndexError:
            self._state = 0

    @property
    def current_state(self):
        return self.states[self.state]

    @property
    def width(self):
        return max([len(line) for line in self.current_state])

    @property
    def height(self):
        return len(self.current_state)

    @staticmethod
    def get():
        shape = random.choice([I, J, L, Z, Square])
        return shape()


class I(Shape):
    states = (
        (
            ' _ ',
            '|_|',
            '|_|',
            '|_|',
            '|_|',
        ),
        (
            ' _ _ _ _',
            '|_|_|_|_|',
        ),
    )


class J(Shape):
    states = (
        (
            '   _ ',
            '  |_|',
            ' _|_|',
            '|_|_|',
        ),
        (
            ' _ ',
            '|_|_ _',
            '|_|_|_|',
        ),
        (
            ' _ _',
            '|_|_|',
            '|_|',
            '|_|',
        ),
        (
            ' _ _ _',
            '|_|_|_|',
            '    |_|',
        ),
    )


class L(Shape):
    states = (
        (
            ' _ ',
            '|_|',
            '|_|_',
            '|_|_|',
        ),
        (
            ' _ _ _',
            '|_|_|_|',
            '|_|',
        ),
        (
            ' _ _ ',
            '|_|_|',
            '  |_|',
            '  |_|',
        ),
        (
            '     _ ',
            ' _ _|_|',
            '|_|_|_|',
        ),
    )


class S(Shape):
    states = (
        (
            '   _ _',
            ' _|_|_|',
            '|_|_|',
        ),
        (
            ' _ ',
            '|_|_',
            '|_|_|',
            '  |_|',
        ),
    )


class Square(Shape):
    states = (
        (
            ' _ _ ',
            '|_|_|',
            '|_|_|',
        ),
    )


class T(Shape):
    states = (
        (
            '   _ ',
            ' _|_|_',
            '|_|_|_|',
        ),
        (
            ' _ ',
            '|_|_',
            '|_|_|',
            '|_|',
        ),
        (
            ' _ _ _',
            '|_|_|_|',
            '  |_|  ',
        ),
        (
            '   _ ',
            ' _|_|',
            '|_|_|',
            '  |_|',
        ),
    )


class Z(Shape):
    states = (
        (
            ' _ _',
            '|_|_|_',
            '  |_|_|',
        ),
        (
            '   _ ',
            ' _|_|',
            '|_|_|',
            '|_|',
        ),
    )
