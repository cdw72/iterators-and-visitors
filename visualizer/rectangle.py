# visualizer/rectangle.py

from abc import ABC, abstractmethod
from visualizer.base import Container, Leaf


class RectangleContainer(Container):
    def __init__(self, name):
        super().__init__(name)
        self.isfirst = True
        self.the_last = ''
        self.width = 0

    def accept(self, visitor, icon_family):
        visitor.visit_container(self, icon_family)

    def draw(self, icon_family):
        if self.level == 1:
            if self.isfirst:
                prefix = '┌─' + icon_family['node']
                suffix = ' ' + '─' * (self.width - len(self.name) - len(prefix) - len(' ') - len('┐')) + '┐'
                print(prefix + self.name + suffix)
            else:
                prefix = '├─' + icon_family['node']
                suffix = ' ' + '─' * (self.width - len(self.name) - len(prefix) - len(' ') - len('┤')) + '┤'
                print(prefix + self.name + suffix)
        if self.level > 1:
            prefix = '│ ' + ' │ ' * (self.level - 2) + ' ├─' + icon_family['node']
            suffix = ' ' + '─' * (self.width - len(self.name) - len(prefix) - len(' ') - len('┤')) + '┤'
            print(prefix + self.name + suffix)
        for i, child in enumerate(self.children):
            child.level = self.level + 1
            child.is_last = i == len(self.children) - 1
            child.width = self.width
            child.isfirst = self.isfirst
            child.the_last = self.the_last
            if self.level == 0 and self.isfirst:
                self.isfirst = False


class RectangleLeaf(Leaf):
    def __init__(self, name):
        super().__init__(name)
        self.isfirst = True
        self.the_last = ''
        self.width = 0

    def accept(self, visitor, icon_family):
        visitor.visit_leaf(self, icon_family)

    def draw(self, icon_family):
        if self.name is not self.the_last:
            prefix = '│ ' + ' │ ' * (self.level - 2) + ' ├─' + icon_family['leaf']
            suffix = ' ' + '─' * (self.width - len(self.name) - len(prefix) - len(' ') - len('┤')) + '┤'
        else:
            prefix = '└' + '─' * self.level + '┴─' + icon_family['leaf']
            suffix = ' ' + '─' * (self.width - len(self.name) - len(prefix) - len(' ') - len('┘')) + '┘'
        print(prefix + self.name + suffix)
