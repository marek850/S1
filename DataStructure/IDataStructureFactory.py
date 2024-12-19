from abc import ABC, abstractmethod

from DataStructure.DataStructure import IDataStructure


class IDataStructureFactory(ABC):
    @abstractmethod
    def create_structure(self) -> IDataStructure:
        pass