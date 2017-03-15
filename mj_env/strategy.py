from abc import ABCMeta, abstractmethod
from random import randint
from .checker import Checker
INIT_TILE_SIZE = 13

class Strategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def pick_a_tile(self, table, hand_tile):
        pass


class RandomStrategy(Strategy):

    def __init__(self):
        super()

    def pick_a_tile(self, table, hand_tile):
        return randint(0, INIT_TILE_SIZE)  # from 0 to 13 inclusive


class NNStrategy(Strategy):

    def __init__(self):
        super()

    def pick_a_tile(self, table, hand_tile):

        tiles = hand_tile.get_private_tiles()

        single_tiles = []
        for i in range(len(tiles)):
            if not self.__has_more_than_one_this_tile(i, tiles) and not self.__has_a_neighbor_tile(i, tiles):
                single_tiles.append(i)

        if single_tiles:
            return single_tiles.pop()
        else:
            return randint(0, hand_tile.get_private_tile_size_to_win() - 1)


    def __has_more_than_one_this_tile(self, i, tiles):
        the_same_ones = [x for x in tiles if x == tiles[i]]
        return len(the_same_ones) > 1 # exclude itself

    def __has_a_neighbor_tile(self, i, tiles):
        adj_tiles = [x for x in tiles if x.family == tiles[i].family and abs(x.number - tiles[i].number) == 1]
        return len(adj_tiles) > 0 # exclude itself