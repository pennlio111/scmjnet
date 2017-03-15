from mj_env.strategy import RandomStrategy
from .checker import Checker
import logging

DEFAULT_WIN_PRIVATE_TILE_SIZE = 14


class Player(object):
    def __init__(self, name, id, strategy=RandomStrategy(), dealer=False, money=0):
        self.name = name
        self.id = id
        self.__hand_tile = HandTile()
        self.__discarded_tiles = []
        self.__dealer = dealer
        self.__money = money
        self.__strategy = strategy
        self.__xiajiao = False

    def set_dealer(self):
        self.__dealer = True

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def draw(self, table, cnt, from_top=True):
        tile_deque = table.drawn_from_top(cnt) if from_top else table.drawn_from_bottom(cnt)
        # update handTile
        while tile_deque:
            tile = tile_deque.popleft() 
            self.__hand_tile.append_private_tile(tile)
            self.__hand_tile.set_last(tile)
        return

    def is_dealer(self):
        return self.__dealer

    def discard_tile(self, table):
        """打牌"""
        if self.get_xiajiao():
            pass
        tile_index = self.__strategy.pick_a_tile(table, self.__hand_tile)
        if tile_index < 0 or tile_index >= len(self.__hand_tile.get_private_tiles()):
            logging.Logger.exception("invalid tile index to discard")
        else:
            tile = self.__hand_tile.discard(tile_index)
            self.__discarded_tiles.append(tile)
        return tile

    def get_hand_tile(self):
        return self.__hand_tile

    def check_win(self):
        "胡牌"
        return Checker.check_win(self.__hand_tile)

    def set_xiajiao(self, is_xiajiao):
        self.__xiajiao = is_xiajiao

    def get_xiajiao(self):
        return self.__xiajiao

    def check_if_i_have_a_jiao(self):
        if Checker.check_jiao(self.__hand_tile):
            self.set_xiajiao(True)
        else:
            self.set_xiajiao(False)

    def sort_private_tiles(self):
        self.__hand_tile.sort_private_tiles()


class HandTile(object):
    def __init__(self):
        self.__public = []
        self.__private = []
        self.__last = None
        self.__private_tile_size_to_win = DEFAULT_WIN_PRIVATE_TILE_SIZE

    def discard(self, i):
        return self.__private.pop(i)

    def sort_private_tiles(self):
        self.__sort_tiles(self.__private)

    def sort_public_tiles(self):
        self.__sort_tiles(self.__public)

    def __sort_tiles(self, tiles):
        tiles.sort(key=lambda x: x.id)
        tiles.sort(key=lambda x: x.number)
        tiles.sort(key=lambda x: x.family)

    def append_public_tile(self, tile):
        self.__public.append(tile)

    def append_private_tile(self, tile):
        self.__private.append(tile)

    def get_private_tiles(self):
        return self.__private

    def get_public_tiles(self):
        return self.__public

    def get_all_tiles(self):
        return self.__public + self.__private
    
    def set_last(self, last):
        self.__last = last
    
    def get_last(self):
        return self.__last

    def find_in_private_tile(self, target_tile):
        return [i for i in range(len(self.__private)) if self.__private[i] == target_tile]

    def __repr__(self):
        split_line = "-"*10
        return self.__private.__repr__() + "\n" + self.__public.__repr__() + "\n" + split_line

    def decease_by_one(self):  # todo: needed by gang or peng
        self.__private_tile_size_to_win -= 1

    def increase_by_one(self):
        self.__private_tile_size_to_win += 1

    def get_private_tile_size_to_win(self):
        return self.__private_tile_size_to_win



