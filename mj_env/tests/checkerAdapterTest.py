from mj_env.checkerAdapter import CheckerAdapter
from mj_env.tile import Tile
import unittest


class TestCheckerAdapterMethods(unittest.TestCase):

    def test_transform(self):
        win_tile1 = [
            Tile("万", 1, 0),
            Tile("万", 1, 1),
            Tile("万", 3, 0),
            Tile("万", 4, 0),
            Tile("万", 5, 0),
            Tile("条", 7, 0),
            Tile("条", 9, 0),
            Tile("条", 8, 0),
            Tile("条", 2, 0),
            Tile("条", 2, 1),
            Tile("条", 2, 2),
            Tile("筒", 1, 0),
            Tile("筒", 1, 2),
            Tile("筒", 1, 1)
            ]
        win_tile2 = [
            Tile("万", 1, 0),
            Tile("万", 1, 1),
            Tile("万", 2, 0),
            Tile("万", 2, 1),
            Tile("万", 3, 0),
            Tile("万", 3, 1),
            Tile("万", 4, 0),
            Tile("万", 4, 1),
            Tile("条", 2, 0),
            Tile("条", 2, 1),
            Tile("条", 2, 2),
            Tile("筒", 1, 0),
            Tile("筒", 1, 2),
            Tile("筒", 1, 1)
            ]

        win_tile3 = [
            Tile("万", 1, 0),
            Tile("万", 1, 1),
            Tile("万", 1, 2),
            Tile("万", 2, 0),
            Tile("万", 2, 1),
            Tile("万", 2, 1),
            Tile("万", 4, 0),
            Tile("万", 4, 1),
            Tile("条", 2, 0),
            Tile("条", 2, 1),
            Tile("条", 2, 2),
            Tile("筒", 1, 0),
            Tile("筒", 1, 2),
            Tile("筒", 1, 1)
            ]

        no_win_tile1 = [
            Tile("万", 1, 0),
            Tile("万", 1, 1),
            Tile("万", 1, 2),
            Tile("万", 2, 0),
            Tile("万", 2, 1),
            Tile("万", 2, 1),
            Tile("万", 4, 0),
            Tile("万", 4, 1),
            Tile("条", 2, 0),
            Tile("条", 2, 1),
            Tile("条", 2, 2),
            Tile("筒", 1, 0),
            Tile("筒", 1, 2),
            Tile("筒", 2, 1)
        ]

        no_win_tile2 = [
            Tile("万", 1, 0),
            Tile("万", 1, 1),
            Tile("万", 1, 2),
            Tile("万", 2, 0),
            Tile("万", 2, 0),
            Tile("万", 5, 0),
            Tile("万", 5, 1),
            Tile("条", 2, 1),
            Tile("条", 2, 2),
            Tile("条", 4, 0),
            Tile("条", 4, 1),
            Tile("筒", 1, 0),
            Tile("筒", 2, 0),
            Tile("筒", 3, 0)
        ]

        self.assertEquals(
            CheckerAdapter.transform_to_tiles("".join(CheckerAdapter.transform_to_string(win_tile1))), win_tile1)
        self.assertEquals(
            CheckerAdapter.transform_to_tiles("".join(CheckerAdapter.transform_to_string(win_tile2))), win_tile2)
        self.assertEquals(
            CheckerAdapter.transform_to_tiles("".join(CheckerAdapter.transform_to_string(win_tile3))), win_tile3)
        self.assertEquals(
            CheckerAdapter.transform_to_tiles("".join(CheckerAdapter.transform_to_string(no_win_tile1))), no_win_tile1)
        self.assertEquals(
            CheckerAdapter.transform_to_tiles("".join(CheckerAdapter.transform_to_string(no_win_tile2))), no_win_tile2)

    def test_xiangtingshu(self):
        win_tile1 = [
            Tile("万", 1, 0),
            Tile("万", 1, 1),
            Tile("万", 3, 0),
            Tile("万", 4, 0),
            Tile("万", 5, 0),
            Tile("条", 7, 0),
            Tile("条", 9, 0),
            Tile("条", 8, 0),
            Tile("条", 2, 0),
            Tile("条", 2, 1),
            Tile("条", 2, 2),
            Tile("筒", 1, 0),
            Tile("筒", 1, 2),
            Tile("筒", 1, 1)
        ]
        wts = CheckerAdapter.transform_to_string(win_tile1)
        print(CheckerAdapter.get_xiangtingshu(wts))