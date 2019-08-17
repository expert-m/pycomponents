import pytest

from pycomponents import ComponentException
from pycomponents.html import Jinja2, Tag


def test_tag():
    tag = Tag('div', 'test')
    tag.init({})

    assert tag.get() == '<div>test</div>'


def test_jinja2_tag():
    tag = Jinja2('<b>{{ name }}</b>', name='Mike')
    tag.init({})

    assert tag.get() == '<b>Mike</b>'


def test_uninitialized_tag():
    tag = Tag('div', 'test')

    with pytest.raises(ComponentException):
        tag.get()
