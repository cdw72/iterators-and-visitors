# 抽象工厂模式涉及的相关类和工厂方法

from abc import ABC, abstractmethod

# 抽象产品类，属于抽象工厂模式的一部分
class IconFamily(ABC):
    def __init__(self):
        self.icons = {
            'node': '',
            'leaf': ''
        }

    @abstractmethod
    def get_icons(self):
        return self.icons
