'''
Global unit-testing fixtures and functions.
'''

import zipfile

import click
import pytest
from click.testing import CliRunner

from soane.items import Book

def assert_zip_file(path, name, body):
    '''
    Assert the contents of a file in a zipfile.
    '''

    with zipfile.ZipFile(path, 'r') as zobj:
        with zobj.open(name, 'r') as fobj:
            assert body == fobj.read().decode('utf-8')

def assert_zip_files(path, zdict):
    '''
    Assert the contents of multiple files in a zipfile.
    '''

    with zipfile.ZipFile(path, 'r') as zobj:
        for name, body in zdict.items():
            with zobj.open(name, 'r') as fobj:
                assert body == fobj.read().decode('utf-8')

def assert_zip_names(path, *names):
    '''
    Assert the namelist in a zipfile.
    '''

    with zipfile.ZipFile(path, 'r') as zobj:
        assert set(names) == set(zobj.namelist())

@pytest.fixture(scope='function')
def cli(zpath):
    '''
    Return a function that returns the output of a Click command.
    '''

    def func(comm, *args):
        runner = CliRunner()
        result = runner.invoke(comm, args, obj=Book(zpath))
        return result.output.splitlines(keepends=True)
    return func

@pytest.fixture(scope='function')
def zpath(tmpdir):
    '''
    Return the path of a temporary zipfile populated with test data.
    '''

    path = tmpdir.join('soane-test.zip')
    with zipfile.ZipFile(path, 'w') as zobj:
        zobj.writestr('alpha.txt',   b'Alpha note.\n')
        zobj.writestr('bravo.txt',   b'Bravo note.\n')
        zobj.writestr('charlie.txt', b'Charlie note.\n')
    return str(path)
