'''
Tests for 'soane.tools.zips'.
'''

import pytest

from soane.tools    import zips
from tests.conftest import assert_zip_file, assert_zip_files

def test_create(zpath):
    # success
    zips.create(zpath, 'append.txt', 'test_append')
    assert_zip_file(zpath, 'append.txt', 'test_append\n')

    # failure - existing address
    with pytest.raises(FileExistsError):
        zips.create(zpath, 'append.txt', 'test_append')

def test_exists(zpath):
    # success
    assert     zips.exists(zpath, 'alpha.txt')
    assert not zips.exists(zpath, 'nope.txt')

def test_list_addrs(zpath):
    # success
    assert set(zips.list_addrs(zpath)) == {
        'alpha.txt', 'bravo.txt', 'charlie.txt',
    }

def test_list_infos(zpath):
    # success
    infos = zips.list_infos(zpath)
    assert {info.filename for info in infos} == {
        'alpha.txt', 'bravo.txt', 'charlie.txt',
    }

def test_read(zpath):
    # success
    assert zips.read(zpath, 'alpha.txt') == 'Alpha note.\n'

def test_read_dict(zpath):
    # success
    assert zips.read_dict(zpath) == {
        'alpha.txt':   'Alpha note.\n',
        'bravo.txt':   'Bravo note.\n',
        'charlie.txt': 'Charlie note.\n',
    }

def test_update(zpath):
    # success
    zips.update(zpath, 'alpha.txt', 'test_write')
    assert_zip_file(zpath, 'alpha.txt', 'test_write\n')

    # failure - nonexistent address
    with pytest.raises(FileNotFoundError):
        zips.update(zpath, 'nope', 'test_write')

def test_write_dict(zpath):
    # success
    zips.write_dict(zpath, {'foo.txt': 'foo', 'bar.txt': 'bar'})
    assert_zip_files(zpath, {'foo.txt': 'foo\n', 'bar.txt': 'bar\n'})
