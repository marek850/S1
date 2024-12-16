from abc import ABC, abstractmethod

from DataStructure.Node import IDataNode


class IDataStructure(ABC):
    @abstractmethod
    def insert(self, node: IDataNode):
        pass

    @abstractmethod
    def search(self, key: tuple) -> IDataNode:
        pass
    @abstractmethod
    def delete(self, key: tuple, data):
        pass
    @abstractmethod
    def update(self, key: tuple, data, new_data):
        pass