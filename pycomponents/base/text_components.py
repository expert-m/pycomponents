import collections
from abc import ABC

from . import Component, BaseComponent


class TextComponent(Component, ABC):
    def render_component(self, component):
        if isinstance(component, BaseComponent):
            component.parent = self
            component.init(self.context)
            return self.render_component(component.render())
        elif isinstance(component, collections.Iterable) and not isinstance(component,  (str, bytes,)):
            result = ''

            for item in component:
                result += self.render_component(item)

            return result
        elif component is None:
            return ''
        else:
            return str(component)

    def __str__(self):
        return self.get()

    def __repr__(self):
        return f'<{self.__class__.__name__}/>'
