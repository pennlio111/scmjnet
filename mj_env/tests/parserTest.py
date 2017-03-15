from mj_env.parser import Parser, TileStructure
from mj_env.tile import Tile
import unittest


class TestParserMethods(unittest.TestCase):

    def test_parse_triplet(self):
        # win_tile1 = [
        #     Tile("万", 1),
        #     Tile("万", 1),
        #     Tile("万", 3),
        #     Tile("万", 4),
        #     Tile("万", 5),
        #     Tile("条", 7),
        #     Tile("条", 8),
        #     Tile("条", 9),
        #     Tile("条", 2),
        #     Tile("条", 2),
        #     Tile("条", 2),
        #     Tile("筒", 1),
        #     Tile("筒", 1),
        #     Tile("筒", 1)
        #     ]
        #
        # parser = Parser()
        # ts = TileStructure()
        # parser.parse_triplets(ts, win_tile1, [1]*len(win_tile1))
        # self.assertEquals(ts.triplets, [[2,3,4],[5,6,7]])

        # win_tile2 = [
        #     Tile("万", 1),
        #     Tile("万", 1),
        #     Tile("万", 2),
        #     Tile("万", 2),
        #     Tile("万", 3),
        #     Tile("万", 3)
        #     ]
        #
        # parser = Parser()
        # ts = TileStructure()
        # parser.parse_triplets(ts, win_tile2, [1]*len(win_tile2))
        # self.assertEquals(ts.triplets, [[0,2,4],[1,3,5]])


        # win_tile3 = [
        #     Tile("万", 1, 0),
        #     Tile("万", 1, 1),
        #     Tile("万", 1, 2),
        #     Tile("万", 2, 0),
        #     Tile("万", 2, 1),
        #     Tile("万", 2, 1),
        #     Tile("万", 4, 0),
        #     Tile("万", 4, 1),
        #     Tile("条", 2, 0),
        #     Tile("条", 2, 1),
        #     Tile("条", 2, 2),
        #     Tile("筒", 1, 0),
        #     Tile("筒", 1, 2),
        #     Tile("筒", 1, 1)
        #     ]

        # no_win_tile1 = [
        #     Tile("万", 1, 0),
        #     Tile("万", 1, 1),
        #     Tile("万", 1, 2),
        #     Tile("万", 2, 0),
        #     Tile("万", 2, 1),
        #     Tile("万", 2, 1),
        #     Tile("万", 4, 0),
        #     Tile("万", 4, 1),
        #     Tile("条", 2, 0),
        #     Tile("条", 2, 1),
        #     Tile("条", 2, 2),
        #     Tile("筒", 1, 0),
        #     Tile("筒", 1, 2),
        #     Tile("筒", 2, 1)
        # ]


        no_win_tile2 = [
            Tile("万", 1),
            Tile("万", 1),
            Tile("万", 1),
            Tile("万", 2),
            Tile("万", 2),
            Tile("万", 5),
            Tile("万", 5),
            Tile("条", 2),
            Tile("条", 2),
            Tile("条", 4),
            Tile("条", 4),
            Tile("筒", 1),
            Tile("筒", 2),
            Tile("筒", 3)
        ]

        parser = Parser()
        ts = TileStructure()
        parser.parse_triplets(ts, no_win_tile2, [1]*len(no_win_tile2))
        self.assertEquals(ts.triplets, [[11,12,13]])
