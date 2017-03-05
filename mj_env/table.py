import numpy as np
import collections
from mj_env.tile import MahjongSuite

class MahjongTable(object):
    def __init__(self, players, dealerIndex):
        self.__tileWall = collections.deque([])
        self.__drawnTiles = []
        self.__poolTiles = []
        self.__tileSuite = MahjongSuite().allSuite()
        self.__players = players
        # set dealer
        self.__players[dealerIndex].setDealer()

    def getReady(self):
        # reset all parameters
        self.shuffleSuite()
        self.__drawnTiles = []
        self.__poolTiles = []
        print(len(self.__tileWall))

    def shuffleSuite(self):
        """
        shuffle the suite
        """
        self.__tileWall = collections.deque(np.random.permutation(self.__tileSuite))
        return

    def toBeDrawnTop(self, count):
        drawn = []
        if 0 < count <= len(self.__tileWall):
            while count > 0:
                tile = self.__tileWall.popleft()
                self.__drawnTiles.append(tile)
                drawn.append(tile)
                count -= 1
        return drawn

    def toBeDrawnBottom(self, count):
        """
        return draw tiles as a list from the top of the tileWall
        :param count:
        :return:
        """
        drawn = []
        if 0 < count <= len(self.__tileWall):
            while count > 0:
                tile = self.__tileWall.popl()
                self.__drawnTiles.append(tile)
                drawn.append(tile)
                count -= 1
        return drawn

    def takeDiscardTile(self, tile):
        self.__poolTiles.append(tile)
        return

    def showPool(self):
        print("Pool:")
        print(self.__poolTiles)

    def getBottomSize(self):
        return len(self.__tileWall)