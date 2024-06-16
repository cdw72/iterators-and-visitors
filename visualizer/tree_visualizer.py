# tree_visualizer.py

from visitors.tree_visitor import TreeVisitor
from visualizer.tree import TreeLeaf, TreeContainer

class TreeVisualizer:

    # 访问者模式：使用访问者遍历和处理树结构的节点
    def visualize(self, icon_family, iterator, visitor):
        for node in iterator:
            node.accept(visitor, icon_family)

    # 构建树结构，将JSON数据转换为树形容器和叶子的组合模式结构
    def build_tree(self, data, name='root'):
        root = TreeContainer(name)
        for key, value in data.items():
            if isinstance(value, dict):
                root.add(self.build_tree(value, key))
            else:
                root.add(TreeLeaf(f"{key}: {value}"))
        return root
