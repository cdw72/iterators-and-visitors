# icons/fancy.py

from .base import IconFamily


class FancyIconFamily(IconFamily):
    def get_icons(self):
        return {
            'node': '♢',
            'leaf': '♤'
        }
