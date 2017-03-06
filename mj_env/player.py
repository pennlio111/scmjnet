from .checker import Checker

class Player(object):
    def __init__(self, name, id, dealer=False, money=0):
        self.name = name
        self.id = id
        self.__handTile = HandTile([])
        self.__discardTiles = []
        self.__dealer = dealer
        self.__money = money

    def set_dealer(self):
        self.__dealer = True

    def draw(self, table, cnt, fromTop=True):
        tile_deque = table.drawn_from_top(cnt) if fromTop else table.drawn_from_bottom(cnt)
        # update handTile
        while tile_deque:
            self.__handTile.appendInvisibleTile(tile_deque.popleft())
        self.__handTile.sortInvisibleTiles()
        return

    def is_dealer(self):
        return self.__dealer

    def discard(self, i, table):
        """打牌"""
        if i < 0 or i >= len(self.__handTile.getInvisibleTiles()):
            print("invalid tile index to discard")
        else:
            tile = self.__handTile.discard(i)
            self.__discardTiles.append(tile)
            table.take_the_discarded_tile(tile)
        return

    def getHandTile(self):
        return self.__handTile

    def win(self):
        "胡牌"
        return True if Checker.check_hu(self.__handTile) else False


class HandTile(object):
    def __init__(self, invisible_tiles, visible_tiles = []):
        self.__visible = visible_tiles
        self.__invisible = invisible_tiles

    def discard(self, i):
        return self.__invisible.pop(i)

    def sortInvisibleTiles(self):
        self.__sortTiles(self.__invisible)

    def sortVisibleTiles(self):
        self.__sortTiles(self.__visible)

    def __sortTiles(self, tiles):
        tiles.sort(key=lambda x: x.id)
        tiles.sort(key=lambda x: x.number)
        tiles.sort(key=lambda x: x.family)

    def appendVisibleTile(self, tile):
        self.__visible.append(tile)

    def appendInvisibleTile(self, tile):
        self.__invisible.append(tile)

    def getInvisibleTiles(self):
        return self.__invisible

    def getVisibleTiles(self):
        return self.__visible

    def get_all_tiles(self):
        return self.__visible + self.__invisible

    def __repr__(self):
        split_line = "-"*10
        return self.__invisible.__repr__() + "\n" + self.__visible.__repr__() + "\n" + split_line



