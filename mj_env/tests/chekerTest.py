from mj_env.checker import Checker
from mj_env.player import HandTile
from mj_env.tile import Tile
import unittest


class TestCheckerMethods(unittest.TestCase):

    def test_check_hu(self):
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

        self.assertTrue(Checker.check_hu(HandTile(win_tile1)))
        self.assertTrue(Checker.check_hu(HandTile(win_tile2)))
        self.assertTrue(Checker.check_hu(HandTile(win_tile3)))
        self.assertFalse(Checker.check_hu(HandTile(no_win_tile1)))
        self.assertFalse(Checker.check_hu(HandTile(no_win_tile2)))