'''
Tests for 'soane.items.zipf'.
'''

import pytest

from soane.items.zipf import ZipFile
from tests.conftest   import assert_zip_file, assert_zip_files

@pytest.fixture(scope='function')
def zipf(zpath):
    return ZipFile(zpath)

def test_init(zipf):
    # success
    assert zipf.path

def test_contains(zipf):
    # success
    assert 'alpha.txt' in zipf
    assert 'nope.txt' not in zipf

def test_eq(zipf):
    # success
    assert zipf == zipf
    assert zipf != ZipFile('nope')
    assert zipf != 'not a Zipfile'

def test_getitem(zipf):
    # success
    assert zipf['alpha.txt'] == 'Alpha note.\n'

def test_hash(zipf):
    # success
    assert {zipf, zipf} == {zipf}

def test_iter(zipf):
    # success
    assert list(zipf) == [
        'alpha.txt', 'bravo.txt', 'charlie.txt',
    ]

def test_len(zipf):
    # success
    assert len(zipf) == 3

def test_repr(zipf):
    # setup
    zipf.path = 'test.zip'

    # success
    assert repr(zipf) == "Zipfile('test.zip')"

def test_create(zipf):
    # success
    zipf.create('create.txt', 'test_create')
    assert_zip_file(zipf.path, 'create.txt', 'test_create\n')

    # failure - existing address
    with pytest.raises(FileExistsError):
        zipf.create('alpha.txt', 'test_create')

def test_open(zipf):
    # success
    with zipf.open('r') as zobj:
        assert zobj

def test_read(zipf):
    # success
    assert zipf.read('alpha.txt') == 'Alpha note.\n'

def test_read_dict(zipf):
    # success
    assert zipf.read_dict() == {
        'alpha.txt':   'Alpha note.\n',
        'bravo.txt':   'Bravo note.\n',
        'charlie.txt': 'Charlie note.\n',
    }

def test_update(zipf):
    # success
    zipf.update('alpha.txt', 'test_update')
    assert_zip_file(zipf.path, 'alpha.txt', 'test_update\n')

    # failure - nonexistent address
    with pytest.raises(FileNotFoundError):
        zipf.update('nope', 'test_update')
