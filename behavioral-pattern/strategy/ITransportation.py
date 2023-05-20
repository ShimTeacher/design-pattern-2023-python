
from abc import ABC, abstractclassmethod


class ITransportation(ABC):

    @abstractclassmethod
    def run():
        pass
