# tree_visitor.py


from visitors.visitor import Visitor


class TreeVisitor(Visitor):

    def visit_leaf(self, node, icon_family):
        node.draw(icon_family)

    def visit_container(self, node, icon_family):
        node.draw(icon_family)
        # for i, child in enumerate(self.children):
        #     if level == 0 and i == len(self.children) - 1:
        #         next_level1 = False
        # self.level = self.level + 1

        # child.draw(icon_family, level + 1, i == len(self.children) - 1, next_level1)
