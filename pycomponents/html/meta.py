from . import BaseTag, BaseSingletonTag


class Head(BaseTag):
    tag_name = 'head'


class Meta(BaseSingletonTag):
    tag_name = 'meta'


class Base(BaseSingletonTag):
    tag_name = 'base'
