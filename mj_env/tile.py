class Tile(object):

    def __init__(self, family, number, id):
        self.family = family
        self.number = number
        self.id = id

    def __repr__(self):
        return "[" + str(self.number) + str(self.family) + "]"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.number == other.number and self.family == other.family


class MahjongSuite(object):
    def __init__(self):
        self.suit = []

    def all_suite(self):
        for family in ["条", "万", "筒"]:
            for number in range(1, 10):
                for id in range(4):
                    self.suit.append(Tile(family, number, id))
        return self.suit

