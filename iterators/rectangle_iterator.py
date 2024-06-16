# rectangle_iterator.py

from iterators import Iterator
from visualizer.rectangle import RectangleContainer, RectangleLeaf
from visitors.rectangle_visitor import RectangleVisitor


class RectangleIterator(Iterator):
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    # def has_next(self):
    #     return bool(self.queue)

    def __next__(self):
        if not self.stack:
            raise StopIteration()
        node = self.stack.pop()
        if isinstance(node, RectangleContainer):
            self.stack.extend(reversed(node.children))
        return node