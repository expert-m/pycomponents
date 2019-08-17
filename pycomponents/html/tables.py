from . import BaseTag, BaseSingletonTag


class Table(BaseTag):
    tag_name = 'table'


class Caption(BaseTag):
    tag_name = 'caption'


class TH(BaseTag):
    tag_name = 'th'


class TR(BaseTag):
    tag_name = 'tr'


class TD(BaseTag):
    tag_name = 'td'


class THead(BaseTag):
    tag_name = 'thead'


class TBody(BaseTag):
    tag_name = 'tbody'


class TFoot(BaseTag):
    tag_name = 'tfoot'


class COL(BaseSingletonTag):
    tag_name = 'col'


class ColGroup(BaseTag):
    tag_name = 'colgroup'
