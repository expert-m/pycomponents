from . import BaseTag, BaseSingletonTag


class Image(BaseSingletonTag):
    tag_name = 'img'


class Map(BaseTag):
    tag_name = 'map'


class Area(BaseSingletonTag):
    tag_name = 'area'


class Canvas(BaseTag):
    tag_name = 'canvas'


class Figcaption(BaseTag):
    tag_name = 'figcaption'


class Figure(BaseTag):
    tag_name = 'figure'


class Picture(BaseTag):
    tag_name = 'picture'


class SVG(BaseTag):
    tag_name = 'svg'

