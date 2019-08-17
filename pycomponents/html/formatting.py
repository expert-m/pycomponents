from . import BaseTag, BaseSingletonTag


class ABBR(BaseTag):
    tag_name = 'abbr'


class Address(BaseTag):
    tag_name = 'address'


class B(BaseTag):
    tag_name = 'b'


class BDI(BaseTag):
    tag_name = 'bdi'


class BDO(BaseTag):
    tag_name = 'bdo'


class BlockQuote(BaseTag):
    tag_name = 'blockquote'


class Cite(BaseTag):
    tag_name = 'cite'


class Code(BaseTag):
    tag_name = 'code'


class DEL(BaseTag):
    tag_name = 'del'


class DFN(BaseTag):
    tag_name = 'dfn'


class EM(BaseTag):
    tag_name = 'em'


class I(BaseTag):
    tag_name = 'i'


class INS(BaseTag):
    tag_name = 'ins'


class KBD(BaseTag):
    tag_name = 'kbd'


class Mark(BaseTag):
    tag_name = 'mark'


class Meter(BaseTag):
    tag_name = 'meter'


class Pre(BaseTag):
    tag_name = 'pre'


class Progress(BaseTag):
    tag_name = 'progress'


class Q(BaseTag):
    tag_name = 'q'


class RP(BaseTag):
    tag_name = 'rp'


class RT(BaseTag):
    tag_name = 'rt'


class Ruby(BaseTag):
    tag_name = 'ruby'


class S(BaseTag):
    tag_name = 's'


class Samp(BaseTag):
    tag_name = 'samp'


class Small(BaseTag):
    tag_name = 'small'


class Strong(BaseTag):
    tag_name = 'strong'


class SUB(BaseTag):
    tag_name = 'sub'


class SUP(BaseTag):
    tag_name = 'sup'


class Template(BaseTag):
    tag_name = 'template'


class Time(BaseTag):
    tag_name = 'time'


class U(BaseTag):
    tag_name = 'u'


class VAR(BaseTag):
    tag_name = 'var'


class WBR(BaseSingletonTag):
    tag_name = 'wbr'
