WIN_TILE_SIZE_WITHOUT_GANG = 14


class Checker(object):
    @staticmethod
    def check_hu(hand_tile):
        # handTile.
        tile = hand_tile.getInvisibleTiles() #todo: 加入吃碰杠的情况
        tile.sort(key=lambda x: x.id)
        tile.sort(key=lambda x: x.number)
        tile.sort(key=lambda x: x.family)
        for i in range(1, len(tile)):
            if tile[i-1].number == tile[i].number and tile[i-1].family == tile[i].family:
                # start dfs
                left = Checker.__has_valid_units(tile[:i-1], [], [])
                right = Checker.__has_valid_units(tile[i+1:], [], [])
                if left and right and len(tile) == WIN_TILE_SIZE_WITHOUT_GANG:
                    return True
        return False

    @staticmethod
    def __has_valid_units(tile, units, unit_to_build):
        if len(unit_to_build) == 3:
            if Checker.__valid_three(unit_to_build):
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
    def __valid_three(tiles):
        if len(tiles) != 3:
            return False
        same_number = all(x == tiles[0] for x in tiles)
        step_increase = all(tiles[i].family == tiles[i-1].family and tiles[i].number - tiles[i-1].number == 1
                            for i in range(1, len(tiles)))
        return same_number or step_increase


    @staticmethod
    def checkJiao(self, hand_tile):
        """如果下叫，进入听牌状态"""
        pass

    @staticmethod
    def checkPeng(self, handTile):
        pass

    @staticmethod
    def checkGang(self, handTile):
        pass

    @staticmethod
    def checkPattern(self, handTile):
        """
        检查胡的番数，返回系数
        :param self:
        :param handTile:
        :return: int
        """
        return 1