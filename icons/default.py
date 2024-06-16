# icons/default.py

from .base import IconFamily


class DefaultIconFamily(IconFamily):
    def get_icons(self):
        return {
            'node': ' ',
            'leaf': ' '
        }
