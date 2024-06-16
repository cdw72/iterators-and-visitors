# icons/fancy.py

from .base import IconFamily

# 具体产品类之一，实现了花哨风格的图标族
class FancyIconFamily(IconFamily):
    def get_icons(self):
        return {
            'node': '♢',
            'leaf': '♤'
        }
