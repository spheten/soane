'''
Tests for 'soane.comms._base'.
'''

import os

import click
from click.testing import CliRunner

from soane.comms import _base
from soane.items import Book

def test_group(cli, temp_dire):
    # setup
    @_base.group.command()
    @click.pass_context
    def test(ctx):
        assert isinstance(ctx.obj, Book)
        assert ctx.obj.dire == temp_dire
        assert ctx.obj.ext  == 'txt'

    # success
    result = CliRunner().invoke(_base.group, ['test'], env={
        'SOANE_DIR': temp_dire,
        'SOANE_EXT': 'txt',
    })
    assert result.exit_code == 0

    # failure - missing SOANE_DIR
    result = CliRunner().invoke(_base.group, ['test'], env={
        'SOANE_DIR': '',
        'SOANE_EXT': 'txt',
    })
    assert 'SOANE_DIR environment variable not set.' in result.output
    assert result.exit_code == 2

    # failure - missing SOANE_EXT
    result = CliRunner().invoke(_base.group, ['test'], env={
        'SOANE_DIR': temp_dire,
        'SOANE_EXT': '',
    })
    assert 'SOANE_EXT environment variable not set.' in result.output
    assert result.exit_code == 2

    # failure - nonexistent SOANE_DIR
    result = CliRunner().invoke(_base.group, ['test'], env={
        'SOANE_DIR': '/nope',
        'SOANE_EXT': 'txt',
    })
    assert 'Configured notes directory does not exist.' in result.output
    assert result.exit_code == 2
