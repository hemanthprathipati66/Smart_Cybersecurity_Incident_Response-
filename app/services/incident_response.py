from abc import ABC, abstractmethod


class IncidentResponse(ABC):

    @abstractmethod
    def respond(self):
        pass