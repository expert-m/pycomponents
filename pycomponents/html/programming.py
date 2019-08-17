from . import BaseTag, BaseSingletonTag


class Script(BaseTag):
    tag_name = 'script'


class NoScript(BaseTag):
    tag_name = 'noscript'


class Embed(BaseSingletonTag):
    tag_name = 'embed'


class Object(BaseTag):
    tag_name = 'object'


class Param(BaseSingletonTag):
    tag_name = 'param'
