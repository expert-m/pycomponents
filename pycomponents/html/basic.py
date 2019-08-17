from . import BaseSingletonTag, BaseTag
from .. import TextComponent


class Html(BaseTag):
    tag_name = 'html'

    def __init__(self, child=None, without_doctype=False, **kwargs):
        super().__init__(child, **kwargs)

        self.without_doctype = without_doctype

    def render(self):
        if self.without_doctype:
            return super().render()
        else:
            return f'<!DOCTYPE html>{super().render()}'


class Head(BaseTag):
    tag_name = 'head'


class Title(BaseTag):
    tag_name = 'title'


class Body(BaseTag):
    tag_name = 'body'


class H1(BaseTag):
    tag_name = 'h1'


class H2(BaseTag):
    tag_name = 'h2'


class H3(BaseTag):
    tag_name = 'h3'


class H4(BaseTag):
    tag_name = 'h4'


class H5(BaseTag):
    tag_name = 'h5'


class H6(BaseTag):
    tag_name = 'h6'


class P(BaseTag):
    tag_name = 'p'


class BR(BaseSingletonTag):
    tag_name = 'br'


class HR(BaseSingletonTag):
    tag_name = 'hr'


class HtmlComment(TextComponent):
    def render(self):
        return f'<!-- {self.render_component(self.child)} -->'
