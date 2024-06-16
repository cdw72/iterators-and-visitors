# tree_visitor.py

from visitors.visitor import Visitor


# 具体访问者类，实现了对树形结构节点的访问
class TreeVisitor(Visitor):

    def visit_leaf(self, node, icon_family):
        # 对叶子节点进行操作，这里调用了其 draw 方法
        node.draw(icon_family)

    def visit_container(self, node, icon_family):
        # 对容器节点进行操作，同样调用了其 draw 方法
        node.draw(icon_family)
