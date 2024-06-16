# visualizer/visualizer_factory.py

from iterators.tree_iterator import TreeIterator
from iterators.rectangle_iterator import RectangleIterator
from visualizer.tree_visualizer import TreeVisualizer
from visualizer.rectangle_visualizer import RectangleVisualizer
from visitors.rectangle_visitor import RectangleVisitor
from visitors.tree_visitor import TreeVisitor


class VisualizerFactory:
    @staticmethod
    def create_visualizer(style):
        if style == 'tree':
            return TreeVisualizer(), TreeIterator, TreeVisitor
        elif style == 'rectangle':
            return RectangleVisualizer(), RectangleIterator, RectangleVisitor
        else:
            raise ValueError(f"Unknown style: {style}")

    @staticmethod
    def get_styles():
        return ['tree', 'rectangle']
