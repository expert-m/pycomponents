from abc import ABC

from .. import TextComponent


class BaseTag(TextComponent, ABC):
    tag_name = None

    @property
    def html_attrs(self):
        result = ''

        for key, value in self.kwargs.items():
            if key[-1] == '_':
                key = key[:-1]

            if key == 'style' and isinstance(value, dict):
                value = ';'.join(f'{k}:{v}' for k, v in value.items())
            elif isinstance(value, bool):
                if value:
                    result += f' {key.replace("_", "-")}'

                continue
            elif key == 'class' and isinstance(value, (list, tuple,)):
                value = ' '.join(value)
            else:
                value = self.render_component(value)

            result += f' {key.replace("_", "-")}="{value}"'

        return result

    def render(self):
        c = self.render_component
        return f'<{self.tag_name}{self.html_attrs}>{c(self.child)}</{self.tag_name}>'


class Tag(BaseTag):
    def __init__(self, tag_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag_name = tag_name

    def render(self):
        c = self.render_component
        return f'<{self.tag_name}{self.html_attrs}>{c(self.child)}</{self.tag_name}>'


class BaseSingletonTag(BaseTag):
    def render(self):
        return f'<{self.tag_name}{self.html_attrs}/>'


class SingletonTag(BaseSingletonTag):
    def __init__(self, tag_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag_name = tag_name

    def render(self):
        return f'<{self.tag_name}{self.html_attrs}/>'

