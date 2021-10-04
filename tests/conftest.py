'''
Global unit-testing fixtures and functions.
'''

import click
import pytest
from click.testing import CliRunner

from soane.items import Book

@pytest.fixture(scope='function')
def cli(temp_dire):
    '''
    Return a function that returns the output of a Click command.
    '''

    def func(comm, *args):
        runner = CliRunner()
        result = runner.invoke(comm, args, obj=Book(temp_dire))
        return result.output.splitlines(keepends=True)
    return func

@pytest.fixture(scope='function')
def temp_dire(tmpdir):
    '''
    Return the path of a temporary directory populated with test data.
    '''

    for name in ['alpha', 'bravo', 'charlie']:
        tmpdir.join(f'{name}.txt').write(f'{name.title()} note.\n')
    return str(tmpdir)
