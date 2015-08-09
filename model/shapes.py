import random

class Shape(object):
    xcoord = 1
    ycoord = 1
    states = ()
    _state = 0

    def move(self, hspan, vspan):
        self.xcoord += hspan
        self.ycoord += vspan

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
        {
            (0, 0): 1,
            (0, 1): 1,
            (0, 2): 1,
            (0, 3): 1,
        },
        {
            (1, 0): 1,
            (2, 0): 1,
            (3, 0): 1,
            (4, 0): 1,
        },
    )


class J(Shape):
    states = (
        {
            (1, 0): 1,
            (1, 1): 1,
            (0, 2): 1,
            (1, 2): 1,
        },
        {
            (0, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
            (2, 1): 1,
        },
        {
            (0, 0): 1,
            (1, 0): 1,
            (0, 1): 1,
            (0, 2): 1,
        },
        {
            (0, 0): 1,
            (0, 1): 1,
            (0, 2): 1,
            (1, 2): 1,
        },
    )


class L(Shape):
    states = (
        {
            (0, 0): 1,
            (0, 1): 1,
            (0, 2): 1,
            (1, 1): 1,
        },
        {
            (0, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
            (0, 1): 1,
        },
        {
            (0, 0): 1,
            (1, 0): 1,
            (1, 1): 1,
            (1, 2): 1,
        },
        {
            (0, 2): 1,
            (1, 0): 1,
            (1, 1): 1,
            (1, 2): 1,
        },
    )


class S(Shape):
    states = (
        {
            (1, 0): 1,
            (2, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
        },
        {
            (0, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
            (1, 2): 1,
        },
    )


class Square(Shape):
    states = (
        {
            (0, 0): 1,
            (1, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
        },
    )


class T(Shape):
    states = (
        {
            (1, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
            (2, 1): 1,
        },
        {
            (0, 0): 1,
            (0, 1): 1,
            (0, 2): 1,
            (1, 1): 1,
        },
        {
            (0, 0): 1,
            (0, 1): 1,
            (0, 2): 1,
            (1, 1): 1,
        },
        {
            (1, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
            (1, 2): 1,
        },
    )


class Z(Shape):
    states = (
        {
            (0, 0): 1,
            (1, 0): 1,
            (1, 1): 1,
            (2, 1): 1,
        },
        {
            (1, 0): 1,
            (0, 1): 1,
            (1, 1): 1,
            (1, 2): 1,
        },
    )
