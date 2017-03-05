from abc import ABCMeta, abstractclassmethod

class ActionType(object):

    __metaclass__ = ABCMeta

    @abstractclassmethod
    def canDo(self):
        pass

    @abstractclassmethod
    def canPass(self):
        pass

    @abstractclassmethod
    def isLegalAction(self):
        pass