from . import BaseTag, BaseSingletonTag


class Form(BaseTag):
    tag_name = 'form'


class Input(BaseSingletonTag):
    tag_name = 'input'


class TextArea(BaseTag):
    tag_name = 'textarea'


class Button(BaseTag):
    tag_name = 'button'


class Select(BaseTag):
    tag_name = 'select'


class Optgroup(BaseTag):
    tag_name = 'optgroup'


class Option(BaseTag):
    tag_name = 'option'


class Label(BaseTag):
    tag_name = 'label'


class FieldSet(BaseTag):
    tag_name = 'fieldset'


class Legend(BaseTag):
    tag_name = 'legend'


class DataList(BaseTag):
    tag_name = 'datalist'


class Output(BaseTag):
    tag_name = 'output'
