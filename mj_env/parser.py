class TileStructure(object):
    def __init__(self):
        self.tiles = 0
        # match priority:
        #  triplets > triples  > pairs > twins > singles  # todo: add quarters in the future
        self.singles = []
        self.pairs = []
        self.triples = []
        #
        self.twins = []
        self.triplets = []


class Parser(object):
    def parse(self, hand_tile):
        ts = TileStructure()


