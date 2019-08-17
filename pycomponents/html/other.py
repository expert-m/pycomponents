from . import Link
from .. import TextComponent

try:
    from jinja2 import Template
except ImportError:
    class Template:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError()


class Fragment(TextComponent):
    def render(self):
        return self.child


class Style(Link):
    def __init__(self, *args, **kwargs):
        kwargs['rel'] = kwargs.get('rel', 'stylesheet')
        super().__init__(*args, **kwargs)


class File(TextComponent):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def render(self):
        with open(self.file_name, 'r') as file:
            data = file.read()

        return data


class Jinja2(TextComponent):
    def render(self):
        template = Template(self.render_component(self.child))
        return template.render(**self.kwargs)


class EscapeCharacter(TextComponent):
    def render(self):
        text = self.render_component(self.child)
        return text.replace(
            '&', '&amp;'
        ).replace(
            '<', '&lt;'
        ).replace(
            '>', '&gt;'
        ).replace(
            '>', '&gt;'
        ).replace(
            '"', '&quot;'
        ).replace(
            '\'', '&#39;'
        )
