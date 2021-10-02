'''
Global unit-testing fixtures and functions.
'''

import zipfile

import pytest

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
