# rectangle_visitor.py

from visitors.visitor import Visitor


class RectangleVisitor(Visitor):

    def visit_leaf(self, node, icon_family):
        node.draw(icon_family)

    def visit_container(self, node, icon_family):
        node.draw(icon_family)




