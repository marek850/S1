from abc import ABC, abstractmethod


class IUserInterface(ABC):
    @abstractmethod
    def notify(self, sender, event_type: str, *args):
        pass
    @abstractmethod
    def request(self, sender, event_type: str, *args):
        pass