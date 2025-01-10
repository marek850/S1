from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def previous(self):
        pass
    
    @abstractmethod
    def has_previous(self):
        pass