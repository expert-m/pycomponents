from abc import ABC

from . import BaseComponent


class Component(BaseComponent, ABC):
    def __init__(self, child=None, **kwargs):
        super().__init__(child, **kwargs)
