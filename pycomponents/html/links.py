from . import BaseTag, BaseSingletonTag


class A(BaseTag):
    tag_name = 'a'


class Link(BaseSingletonTag):
    tag_name = 'link'


class Nav(BaseTag):
    tag_name = 'nav'
