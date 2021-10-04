'''
Tests for 'soane.tools.clui'.
'''

import os.path

import click
import pytest

from soane.tools import clui

def test_AbbrGroup():
    # setup
    @click.group(cls=clui.AbbrGroup)
    def group():
        pass

    @group.command()
    def test_one():
        pass

    @group.command()
    def test_two():
        pass

    # success
    assert group.get_command(None, 'test-o')   == test_one
    assert group.get_command(None, 'test-one') == test_one

    with pytest.raises(click.exceptions.UsageError):
        group.get_command(click.Context(group), 'test')

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
