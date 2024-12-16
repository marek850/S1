from abc import ABC, abstractmethod

class IDataNode(ABC):
    @abstractmethod
    def __init__(self, key: tuple, data: object):
        pass