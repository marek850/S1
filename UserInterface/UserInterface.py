from abc import ABC, abstractmethod


class IUserInterface(ABC):
    @abstractmethod
    def notify(self, event_type: str, *args):
        pass
    @abstractmethod
    def request(self, event_type: str, *args):
        pass