from mj_env.tile import Tile
from mj_checker.mahjong import xiangtingshu_output
import textwrap


class CheckerAdapter(object):

    __char_to_letter = {
        "万":"m",
        "筒":"p",
        "条":"s",
        "字":"z"
    }
    __letter_to_char = {
        "m":"万",
        "p":"筒",
        "s":"条",
        "z":"字"
    }

    @staticmethod
    def tile_to_string(tile):
        return str(tile.number) + CheckerAdapter.__char_to_letter[tile.family]

    @staticmethod
    def string_to_tile(s):
        return Tile(CheckerAdapter.__letter_to_char[s[1]], int(s[0]))  # todo: to fix lost id information after the transform

    @staticmethod
    def card_to_tile(card):
        return Tile(CheckerAdapter.__letter_to_char[card.get_suit()], card.get_rank())

    @staticmethod
    def transform_to_string(tiles):
        return [CheckerAdapter.tile_to_string(x) for x in tiles]

    @staticmethod
    def transform_to_tiles(tile_string):
        tile_list = textwrap.wrap(tile_string, 2)
        return [CheckerAdapter.string_to_tile(x) for x in tile_list]

    @staticmethod
    def get_xiangtingshu(tile_string):
        best_cards = xiangtingshu_output(tile_string)
        return [(CheckerAdapter.card_to_tile(bc[0]), bc[1], bc[2], [CheckerAdapter.card_to_tile(c) for c in bc[3]]) for bc in best_cards]