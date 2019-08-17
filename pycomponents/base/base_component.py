import collections
from abc import ABC, abstractmethod


class ComponentException(Exception):
    pass


class BaseComponent(ABC):
    context = None
    initialized = False
    kwargs = None
    parent = None

    def __init__(self, child, **kwargs):
        self.child = child
        self.kwargs = kwargs

    def init(self, context=None):
        self.context = context
        self.initialized = True

    def get(self):
        if not self.initialized:
            raise ComponentException('The component is not initialized.')

        return self.render_component(self)

    @abstractmethod
    def render_component(self, component):
        if isinstance(component, BaseComponent):
            component.parent = self
            component.init(self.context)
            return self.render_component(component.render())
        elif isinstance(component, collections.Iterable):
            result = []

            for item in component:
                result.append(self.render_component(item))

            return result
        else:
            return component

    @abstractmethod
    def render(self):
        pass
