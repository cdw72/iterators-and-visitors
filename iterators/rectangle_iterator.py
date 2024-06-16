# rectangle_iterator.py

from iterators import Iterator  # 引入迭代器接口
from visualizer.rectangle import RectangleContainer, RectangleLeaf  # 引入矩形结构相关类
from visitors.rectangle_visitor import RectangleVisitor  # 引入矩形访问者类


class RectangleIterator(Iterator):
    def __init__(self, root):
        self.stack = [root]  # 使用栈来追踪当前迭代位置

    def __iter__(self):
        return self  # 迭代器应该返回自身作为迭代器对象

    def __next__(self):
        if not self.stack:
            raise StopIteration()  # 栈为空时，迭代结束
        node = self.stack.pop()  # 弹出栈顶节点
        if isinstance(node, RectangleContainer):
            self.stack.extend(reversed(node.children))  # 如果是容器节点，则将其子节点逆序入栈
        return node  # 返回当前节点
