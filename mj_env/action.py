from abc import ABCMeta, abstractclassmethod


class Action(object):

    __metaclass__ = ABCMeta

    @abstractclassmethod
    def can_do(self):
        pass

    @abstractclassmethod
    def can_pass(self):
        pass