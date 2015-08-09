import random

class Shape(object):
    lng = 0
    lat = 0
    states = ()
    _state = 0

    def move(self, hspan, vspan):
        self.lng += hspan
        self.lat += vspan

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
    def matrix(self):
        matrix = {}
        for point, state in self.current_state.items():
            lng, lat = point
            new_point = (lng + self.lng, lat + self.lat)
            matrix[new_point] = state
        return matrix

    @staticmethod
    def get():
        shape = random.choice([I, J, L, Z, Square])
        return shape()


class I(Shape):
    states = (
        {
            (1, 1): 1,
            (1, 2): 1,
            (1, 3): 1,
            (1, 4): 1,
        },
        {
            (2, 1): 1,
            (3, 1): 1,
            (4, 1): 1,
            (5, 1): 1,
        },
    )


class J(Shape):
    states = (
        {
            (2, 1): 1,
            (2, 2): 1,
            (2, 3): 1,
            (1, 3): 1,
        },
        {
            (1, 1): 1,
            (1, 2): 1,
            (2, 2): 1,
            (3, 2): 1,
        },
        {
            (1, 1): 1,
            (2, 1): 1,
            (1, 2): 1,
            (1, 3): 1,
        },
        {
            (1, 1): 1,
            (2, 1): 1,
            (3, 1): 1,
            (3, 2): 1,
        },
    )


class L(Shape):
    states = (
        {
            (1, 1): 1,
            (1, 2): 1,
            (1, 3): 1,
            (2, 3): 1,
        },
        {
            (1, 1): 1,
            (2, 1): 1,
            (3, 1): 1,
            (1, 2): 1,
        },
        {
            (1, 1): 1,
            (2, 1): 1,
            (2, 2): 1,
            (2, 3): 1,
        },
        {
            (3, 1): 1,
            (1, 2): 1,
            (2, 2): 1,
            (3, 2): 1,
        },
    )


class S(Shape):
    states = (
        {
            (2, 1): 1,
            (3, 1): 1,
            (1, 2): 1,
            (2, 2): 1,
        },
        {
            (1, 1): 1,
            (1, 2): 1,
            (2, 2): 1,
            (2, 3): 1,
        },
    )


class Square(Shape):
    states = (
        {
            (1, 1): 1,
            (2, 1): 1,
            (1, 2): 1,
            (2, 2): 1,
        },
    )


class T(Shape):
    states = (
        {
            (2, 1): 1,
            (1, 2): 1,
            (2, 2): 1,
            (3, 2): 1,
        },
        {
            (1, 1): 1,
            (1, 2): 1,
            (1, 3): 1,
            (2, 2): 1,
        },
        {
            (2, 2): 1,
            (1, 1): 1,
            (2, 1): 1,
            (3, 1): 1,
        },
        {
            (1, 2): 1,
            (2, 1): 1,
            (2, 2): 1,
            (2, 3): 1,
        },
    )


class Z(Shape):
    states = (
        {
            (1, 1): 1,
            (2, 1): 1,
            (2, 2): 1,
            (3, 2): 1,
        },
        {
            (2, 1): 1,
            (1, 2): 1,
            (2, 2): 1,
            (1, 3): 1,
        },
    )
