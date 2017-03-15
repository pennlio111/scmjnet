from mj_env.tile import MahjongSuite
import copy


class Checker(object):
    @staticmethod
    def check_win(hand_tile):
        hand_tile.sort_private_tiles()
        tile = hand_tile.get_private_tiles() #todo: 加入吃碰杠的情况
        for i in range(1, len(tile)):
            if tile[i-1] == tile[i]: # jiang
                left = Checker.__has_valid_units(tile[:i-1], [], [])
                right = Checker.__has_valid_units(tile[i+1:], [], [])
                if left and right and len(tile) == hand_tile.get_private_tile_size_to_win():
                    return True
        return False

    @staticmethod
    def __has_valid_units(tile, units, unit_to_build):
        if len(unit_to_build) == 3:
            if Checker.__valid_unit_of_three(unit_to_build):
                return Checker.__has_valid_units(tile, units + unit_to_build, [])
            else: # 回到上一层DFS
                return False
        if not tile:
            return not unit_to_build
        else:
            last_checked = None
            for i in range(len(tile)):
                if tile[i] == last_checked:  # 剪枝
                    continue
                if not unit_to_build or (tile[i].family == unit_to_build[-1].family and tile[i].number - unit_to_build[-1].number <=1):
                    unit_to_build.append(tile[i])
                    if Checker.__has_valid_units(tile[:i] + tile[i+1:], units, unit_to_build):
                        return True
                    last_checked = unit_to_build.pop() # back-tracking
            return False

    @staticmethod
    def __valid_unit_of_three(tiles):
        if len(tiles) != 3:
            return False
        triples = all(x == tiles[0] for x in tiles)
        triplets = all(tiles[i].family == tiles[i-1].family and tiles[i].number - tiles[i-1].number == 1
                            for i in range(1, len(tiles)))
        return triples or triplets


    @staticmethod
    def check_jiao(hand_tile):
        """如果下叫，进入听牌状态"""
        if len(hand_tile.get_private_tiles()) != hand_tile.get_private_tile_size_to_win() - 1:
            return []
        jiao_tiles = []
        suite = MahjongSuite().all_suite()
        for tile in suite:
            win_hand_tile = copy.deepcopy(hand_tile)
            win_hand_tile.append_private_tile(tile)
            if Checker.check_win(win_hand_tile) and hand_tile.count(tile) < 4:
                jiao_tiles.append(tile)
        return jiao_tiles

    @staticmethod
    def check_peng(handTile):
        pass

    @staticmethod
    def checkGang(handTile):
        pass

    @staticmethod
    def checkPattern(handTile):
        """
        检查胡的番数，返回系数
        :param handTile:
        :return: int
        """
        return 1