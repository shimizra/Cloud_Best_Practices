from abc import ABC, abstractmethod

class BaseReporter(ABC):
    @abstractmethod
    def report(self, findings: dict):
        pass
