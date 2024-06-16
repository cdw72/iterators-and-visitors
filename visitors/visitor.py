# visitor.py

from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_leaf(self, node, icon_family):
        pass

    @abstractmethod
    def visit_container(self, node, icon_family):
        pass
