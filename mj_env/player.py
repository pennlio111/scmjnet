class Player(object):
    def __init__(self, name, id, dealer = False):
        self.name = name
        self.id = id
        self.__handTile = []
        self.__discardTiles = []
        self.__dealer = dealer

    def setDealer(self):
        self.__dealer = True

    def sortTile(self):
        self.__handTile.sort(key=lambda x: x.number)
        self.__handTile.sort(key=lambda x: x.family)

    def draw(self, table, cnt, fromTop = True):
        tiles = table.toBeDrawnTop(cnt) if fromTop else table.toBeDrawnBottom(cnt)
        # update handTile
        self.__handTile += tiles
        self.sortTile()
        return

    def isDealer(self):
        return self.__dealer

    def discard(self, i, table):
        if i < 0 or i >= len(self.__handTile):
            print("invalid tile index to discard")
        else:
            tile = self.__handTile.pop(i)
            self.__discardTiles.append(tile)
            table.takeDiscardTile(tile)
        return

    def getHandTile(self):
        return self.__handTile
