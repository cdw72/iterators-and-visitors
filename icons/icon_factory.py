# icons/icon_factory.py

from .default import DefaultIconFamily
from .fancy import FancyIconFamily

# 工厂类，负责创建具体的图标族对象
class IconFactory:
    @staticmethod
    def create_icon_family(name):
        if name == 'default':
            return DefaultIconFamily()
        elif name == 'fancy':
            return FancyIconFamily()
        else:
            raise ValueError(f"Unknown icon family: {name}")

    @staticmethod
    def get_families():
        return ['default', 'fancy']
