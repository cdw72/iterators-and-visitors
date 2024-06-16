# visualizer/tree.py

from abc import ABC, abstractmethod
from visualizer.base import Container, Leaf


class TreeContainer(Container):
    def __init__(self, name):
        super().__init__(name)
        self.next_level = True

    def accept(self, visitor, icon_family):
        visitor.visit_container(self, icon_family)

    def draw(self, icon_family):
        if self.level > 0:
            prefix = ('│' if self.level > 1 else '') + ' ' * (self.level - 1) * 2 + ('└─' if self.is_last else '├─') \
                     + icon_family['node']
            print(prefix + self.name)
        for i, child in enumerate(self.children):
            if self.level == 0 and i == len(self.children) - 1:
                self.next_level = False
            child.next_level = self.next_level
            child.level = self.level + 1
            child.is_last = (i == len(self.children) - 1)


class TreeLeaf(Leaf):
    def __init__(self, name):
        super().__init__(name)
        self.next_level = True

    def accept(self, visitor, icon_family):
        visitor.visit_leaf(self, icon_family)

    def draw(self, icon_family):
        prefix = ('│' if self.level > 1 and self.next_level else '') + ' ' * (self.level - 1) * 2 + (
            '└─' if self.is_last else '├─') \
                 + icon_family['leaf']
        print(prefix + self.name)
