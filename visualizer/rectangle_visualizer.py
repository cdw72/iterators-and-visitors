# rectangle_visualizer.py

from visitors.rectangle_visitor import RectangleVisitor
from visualizer.rectangle import RectangleContainer, RectangleLeaf


class RectangleVisualizer:

    # 访问者模式：使用访问者遍历和处理树结构的节点
    def visualize(self, icon_family, iterator, visitor):
        for node in iterator:
            node.accept(visitor, icon_family)

    # 构建树结构，将JSON数据转换为矩形容器和叶子的组合模式结构
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

    # 辅助方法，用于收集树中每一层的节点信息
    def _collect_lines(self, component, level=0):
        lines = []
        for child in component.children:
            lines.append(child.name)
            if isinstance(child, RectangleContainer):
                lines.extend(self._collect_lines(child, level + 1))
        return lines
