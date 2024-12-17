from abc import ABC, abstractmethod

class IFileStrategy(ABC):
    @abstractmethod
    def save(self, filename, data):
        """Save data to the file."""
        pass

    @abstractmethod
    def load(self, filename, app):
        """Load data from the file."""
        pass