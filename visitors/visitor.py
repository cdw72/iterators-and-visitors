# visitor.py

from abc import ABC, abstractmethod


# 抽象访问者基类
class Visitor(ABC):
    @abstractmethod
    def visit_leaf(self, node, icon_family):
        pass

    @abstractmethod
    def visit_container(self, node, icon_family):
        pass
