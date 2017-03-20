from mj_env.checkerAdapter import CheckerAdapter
from mj_env.tile import Tile

win_tile1 = [
    Tile("万", 1, 0),
    Tile("万", 1, 1),
    Tile("万", 3, 0),
    Tile("万", 4, 0),
    Tile("万", 5, 0),
    Tile("条", 7, 0),
    Tile("条", 8, 0),
    Tile("条", 9, 0),
    Tile("条", 2, 0),
    Tile("条", 2, 1),
    Tile("条", 2, 2),
    Tile("筒", 1, 0),
    Tile("筒", 1, 1),
    Tile("筒", 1, 2)
]

wts = CheckerAdapter.transform_to_string(win_tile1)
wts = "".join(wts)
print(CheckerAdapter.get_xiangtingshu(wts))