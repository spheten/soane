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
    Return a function that returns the Book and output of a Click command.
    '''

    def func(comm, *args):
        obj    = Book(temp_dire, 'txt')
        result = CliRunner().invoke(comm, args, obj=obj, env={
            'SOANE_DIR': temp_dire,
            'SOANE_EXT': 'txt',
        })
        return obj, result.output.splitlines(keepends=True)
    return func

@pytest.fixture(scope='function')
def temp_dire(tmpdir):
    '''
    Return the path of a temporary directory populated with test data.
    '''

    for name in ['alpha', 'bravo', 'charlie']:
        tmpdir.join(f'{name}.txt').write(f'{name.title()} note.\n')
    return str(tmpdir)
