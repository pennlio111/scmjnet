import numpy as np
import collections
from mj_env.tile import MahjongSuite

class MahjongTable(object):
    def __init__(self, players):
        self.__tile_wall = collections.deque([])
        self.__drawn_tiles = []
        self.__players = players
        self.__pool_tiles = []
        self.__the_suite = MahjongSuite().all_suite()
        self.__dealer_index = -1 # no dealer

    def get_ready(self, dealer_index):
        # reset all parameters
        self.__shuffle_tile_suite()
        self.__drawn_tiles = []
        self.__pool_tiles = [collections.deque([]) for _ in range(len(self.__players))]
        self.__dealer_index = dealer_index
        self.__players[self.__dealer_index].set_dealer()
        print("====== Game START ========")

    def __shuffle_tile_suite(self):
        """
        shuffle the suite
        """
        self.__tile_wall = collections.deque(np.random.permutation(self.__the_suite))
        return

    def drawn_from_top(self, count):
        """
        return draw tiles as a list from the top of the tileWall
        :param count:
        :return: a deque
        """
        drawn = collections.deque([])
        if 0 < count <= len(self.__tile_wall):
            while count > 0:
                tile = self.__tile_wall.popleft()
                self.__drawn_tiles.append(tile)
                drawn.append(tile)
                count -= 1
        return drawn

    def drawn_from_bottom(self, count):
        """
        return draw tiles as a list from the bottom of the tileWall
        :param count:
        :return: a deque
        """
        drawn = collections.deque([])
        if 0 < count <= len(self.__tile_wall):
            while count > 0:
                tile = self.__tile_wall.popl()
                self.__drawn_tiles.append(tile)
                drawn.append(tile)
                count -= 1
        return drawn

    def take_the_discarded_tile(self, index, tile):
        self.__pool_tiles[index].append(tile)
        return

    def show_the_pool(self):
        print("Pool:")
        for i in range(len(self.__pool_tiles)):
            print(str(i))
            print([tile for tile in self.__pool_tiles[i]])

    def get_bottom_size(self):
        return len(self.__tile_wall)

    def has_next_tile(self):
        return len(self.__tile_wall) > 0