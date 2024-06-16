# rectangle_visualizer.py

from visitors.rectangle_visitor import RectangleVisitor
from visualizer.rectangle import RectangleContainer, RectangleLeaf


class RectangleVisualizer:

    def visualize(self, icon_family, iterator, visitor):
        # root = self._build_tree(data)
        # root.draw(icon_family)
        for node in iterator:
            node.accept(visitor, icon_family)

    def build_tree(self, data, name='root'):
        root = RectangleContainer(name)
        for key, value in data.items():
            if isinstance(value, dict):
                root.add(self.build_tree(value, key))
            else:
                root.add(RectangleLeaf(f"{key}: {value}"))
        lines = self._collect_lines(root)
        root.width = max(len(line) for line in lines) + 24
        root.the_last = lines[-1]
        return root

    def _collect_lines(self, component, level=0):
        lines = []
        for child in component.children:
            lines.append(child.name)
            if isinstance(child, RectangleContainer):
                lines.extend(self._collect_lines(child, level + 1))
        return lines
