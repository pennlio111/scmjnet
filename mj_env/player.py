from .checker import Checker

class Player(object):
    def __init__(self, name, id, dealer = False, money = 0):
        self.name = name
        self.id = id
        self.__handTile = HandTile([])
        self.__discardTiles = []
        self.__dealer = dealer
        self.__money = money

    def setDealer(self):
        self.__dealer = True

    def draw(self, table, cnt, fromTop = True):
        tileDeque = table.toBeDrawnTop(cnt) if fromTop else table.toBeDrawnBottom(cnt)
        # update handTile
        while tileDeque:
            self.__handTile.appendInvisibleTile(tileDeque.popleft())
        self.__handTile.sortInvisibleTiles()
        return

    def isDealer(self):
        return self.__dealer

    def discard(self, i, table):
        """打牌"""
        if i < 0 or i >= len(self.__handTile.getInvisibleTiles()):
            print("invalid tile index to discard")
        else:
            tile = self.__handTile.discard(i)
            self.__discardTiles.append(tile)
            table.takeDiscardTile(tile)
        return

    def getHandTile(self):
        return self.__handTile

    def win(self):
        "胡牌"
        return True if Checker.checkHu(self.__handTile) else False


class HandTile(object):
    def __init__(self, tiles):
        self.__visibleTiles = tiles
        self.__invisibleTiles = []
        self.__tiles = self.__visibleTiles + self.__invisibleTiles

    def sortTiles(self):
        self.__tiles.sort(key=lambda x: x.number)
        self.__tiles.sort(key=lambda x: x.family)

    def discard(self, i):
        return self.__invisibleTiles.pop(i)

    def sortInvisibleTiles(self):
        self.__invisibleTiles.sort(key=lambda x: x.number)
        self.__invisibleTiles.sort(key=lambda x: x.family)

    def sortVisibleTiles(self):
        self.__visibleTiles.sort(key=lambda x: x.number)
        self.__visibleTiles.sort(key=lambda x: x.number)

    def appendVisibleTile(self, tile):
        self.__visibleTiles.append(tile)

    def appendInvisibleTile(self, tile):
        self.__invisibleTiles.append(tile)

    def getInvisibleTiles(self):
        return self.__invisibleTiles

    def getVisibleTiles(self):
        return self.__visibleTiles

    def __repr__(self):
        split_line = "-"*10
        return self.__invisibleTiles.__repr__() + "\n" + self.__visibleTiles.__repr__() + "\n" + split_line



