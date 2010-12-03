
class Shape(object):
    column = 0
    line = 0
    position = 0

    def __init__(self):
        return self

    def move(self, moves):
        self.column = self.column + moves.horizontal
        self.column = self.column + moves.vertical
