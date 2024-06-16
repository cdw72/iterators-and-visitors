# tree_visualizer.py

from visitors.tree_visitor import TreeVisitor
from visualizer.tree import TreeLeaf, TreeContainer


class TreeVisualizer:
    def visualize(self, icon_family, iterator, visitor):
        # root = self._build_tree(data)
        # root.draw(icon_family)
        for node in iterator:
            node.accept(visitor, icon_family)

    def build_tree(self, data, name='root'):
        root = TreeContainer(name)
        for key, value in data.items():
            if isinstance(value, dict):
                root.add(self.build_tree(value, key))
            else:
                root.add(TreeLeaf(f"{key}: {value}"))
        return root
