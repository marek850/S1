from abc import ABC, abstractmethod

from DataStructure.DataStructure import IDataStructure
from DataStructure.Node import IDataNode


class IDataStructureFactory(ABC):
    @abstractmethod
    def create_structure(self) -> IDataStructure:
        pass

    @abstractmethod
    def create_node(self, keys: tuple, data: object) -> IDataNode:
        pass