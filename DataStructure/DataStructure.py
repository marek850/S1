from abc import ABC, abstractmethod



class IDataStructure(ABC):
    @abstractmethod
    def insert(self, *args):
        pass

    @abstractmethod
    def search(self, *args):
        pass
    @abstractmethod
    def delete(self, *args):
        pass
    @abstractmethod
    def update(self, *args):
        pass