class TileStructure(object):
    def __init__(self):
        self.tiles = 0
        # match priority:
        #  triplets > triples  > pairs > twins > singles  # todo: add quarters in the future
        self.singles = []
        self.pairs = []
        self.triples = []
        #
        self.brothers = []
        self.triplets = []

    def __repr__(self):
        return [str(x) for x in self.triplets]


class Parser(object):

    def parse(self, hand_tile):
        ts = TileStructure()
        private_tiles = hand_tile.get_private_tiles()
        un_selected = [1] * len(private_tiles)
        self.parse_triplets(ts, private_tiles, un_selected)
        # self.__parse_triples(private_tiles, un_selected)
        # self.__parse_pairs(private_tiles, un_selected)
        # self.__parse_brothers(private_tiles, un_selected)
        # self.__parse_singles(private_tiles, un_selected)
        return ts

    def parse_triplets(self, ts, tiles, un_selected):
        """
        greedy match triplets in tiles
        :param tiles:
        :param un_selected:
        :return:
        """
        k = self.__next_unselected(un_selected)
        found = False
        while 0 <= k < len(tiles) and sum(un_selected) >= 3:
            path = [(tiles[k], k)]
            i = k + 1
            while i < len(tiles):
                if not un_selected[i] or tiles[i] == path[-1][0]:
                    i += 1
                elif tiles[i].family == path[-1][0].family and tiles[i].number == path[-1][0].number+1:
                    path.append((tiles[i], i))
                    if len(path) == 3:
                        indices = [x[1] for x in path]
                        ts.triplets.append(indices) # only append the index
                        for i in indices:
                            un_selected[i] = 0 # mark as selected
                        k = self.__next_unselected(un_selected)  # k is the new start point
                        found = True  # flag for found
                        break
                    else:
                        i += 1
                else: # impossible to find one, increase k
                    break
            if not found:
                k += 1
        return

    def __next_unselected(self, un_selected):
        for i in range(len(un_selected)):
            if un_selected[i]:
                return i
        return -1









