'''
Tests for 'soane.tools.zips'.
'''

import pytest

from soane.tools    import zips
from tests.conftest import assert_zip_file, assert_zip_files

def test_append(zpath):
    # success
    zips.append(zpath, 'append.txt', 'test_append')
    assert_zip_file(zpath, 'append.txt', 'test_append\n')

    # failure - existing name
    with pytest.raises(FileExistsError):
        zips.append(zpath, 'append.txt', 'test_append')

def test_exists(zpath):
    # success
    assert     zips.exists(zpath, 'alpha.txt')
    assert not zips.exists(zpath, 'nope.txt')

def test_list_infos(zpath):
    # success
    infos = zips.list_infos(zpath)
    assert {info.filename for info in infos} == {
        'alpha.txt', 'bravo.txt', 'charlie.txt',
    }

def test_list_names(zpath):
    # success
    assert set(zips.list_names(zpath)) == {
        'alpha.txt', 'bravo.txt', 'charlie.txt',
    }

def test_read(zpath):
    # success
    assert zips.read(zpath, 'alpha.txt') == 'Alpha note.\n'

def test_read_all(zpath):
    # success
    assert zips.read_all(zpath) == {
        'alpha.txt':   'Alpha note.\n',
        'bravo.txt':   'Bravo note.\n',
        'charlie.txt': 'Charlie note.\n',
    }

def test_write(zpath):
    # success
    zips.write(zpath, 'alpha.txt', 'test_write')
    assert_zip_file(zpath, 'alpha.txt', 'test_write\n')

def test_write_all(zpath):
    # success
    zips.write_all(zpath,   {'foo.txt': 'foo',   'bar.txt': 'bar'})
    assert_zip_files(zpath, {'foo.txt': 'foo\n', 'bar.txt': 'bar\n'})
