'''
Tests for 'soane.tools.clui'.
'''

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
    assert group.get_command(None, 'nope')     == None

    with pytest.raises(click.exceptions.UsageError):
        group.get_command(click.Context(group), 'test')
