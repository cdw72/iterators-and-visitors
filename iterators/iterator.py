# iterators.py

from abc import ABC, abstractmethod


# 迭代器接口定义，属于迭代器模式的一部分
class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass
