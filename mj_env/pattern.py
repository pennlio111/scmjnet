from abc import ABCMeta, abstractclassmethod

class Pattern(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, multiplier):
        self.name = name
        self.multiplier = multiplier

    @abstractclassmethod
    def is_valid(self, handTile):
        pass

class QiduiPattern(Pattern):

    def __init__(self):
        super().__init__("Qidui", 4)

    def is_valid(self, handTile):
        pass

class KaXingWuPattern(Pattern):
    def __init__(self, name, multiplier):
        super().__init__("KaXingWu", 2)

    def is_valid(self, handTile):
        pass
