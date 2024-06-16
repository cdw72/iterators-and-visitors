# iterators.py

from abc import ABC, abstractmethod


class Iterator(ABC):
    # @abstractmethod
    # # def has_next(self):
    # #     pass
    @abstractmethod
    def __next__(self):
        pass