# icons/default.py

from .base import IconFamily

# 具体产品类之一，实现了默认风格的图标族
class DefaultIconFamily(IconFamily):
    def get_icons(self):
        return {
            'node': ' ',
            'leaf': ' '
        }
