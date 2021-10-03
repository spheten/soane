'''
Tests for 'soane.tools.clui'.
'''

import os.path

import click
import pytest

from soane.tools import clui

def test_BookType(tmpdir):
    # setup
    path = tmpdir.join('book.ext')
    path.write('')

    # success
    assert clui.BOOK.convert(str(path), None, None) == \
        os.path.normpath(str(path))

    # failure - nonexistent path
    with pytest.raises(click.exceptions.BadParameter):
        clui.BOOK.convert('nope.txt', None, None)

def test_NameType():
    # success
    assert clui.NAME.convert('TEST-123!@#$', None, None) == \
        'test-123'

    # failure - empty slug
    with pytest.raises(click.exceptions.BadParameter):
        clui.NAME.convert('!@#$', None, None)
