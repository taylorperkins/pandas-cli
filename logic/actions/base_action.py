import abc


class BaseAction(metaclass=abc.ABCMeta):
    def __init__(self):
        super(BaseAction, self).__init__()

    @abc.abstractmethod
    def go(self):
        """Root method for performing an operation"""
        pass
