'''
Tests for 'soane.tools.file'.
'''

import pytest

from soane.tools import file

def test_create(tmpdir):
    # setup
    path = tmpdir.join('test_create.txt')

    # success
    file.create(path, 'test_create')
    assert path.read() == 'test_create\n'

def test_delete(tmpdir):
    # setup
    path = tmpdir.join('test_delete.txt')
    path.write('')

    # success
    file.delete(path)
    assert not path.isfile()

def test_duplicate(tmpdir):
    # setup
    orig = tmpdir.join('test_duplicate_orig')
    dest = tmpdir.join('test_duplicate_dest')
    orig.write('')

    # success
    file.duplicate(orig, 'test_duplicate_dest')
    assert dest.isfile()

def test_exists(tmpdir):
    # setup
    path = tmpdir.join('test_exists.txt')
    path.write('')

    # success
    assert file.exists(path)
    assert file.exists(tmpdir, dire=True)

def test_glob(tmpdir):
    # setup
    for name in ['alpha', 'bravo', 'charlie']:
        tmpdir.join(f'{name}.txt').write('')

    # success
    globs = list(file.glob(tmpdir, '*.txt'))
    assert len(globs) == 3
    assert globs[0].endswith('alpha.txt')
    assert globs[1].endswith('bravo.txt')
    assert globs[2].endswith('charlie.txt')

def test_read(tmpdir):
    # setup
    path = tmpdir.join('test_read.txt')
    path.write('test_read')

    # success
    assert file.read(path) == 'test_read\n'

def test_rename(tmpdir):
    # setup
    orig = tmpdir.join('test_duplicate_orig')
    dest = tmpdir.join('test_duplicate_dest')
    orig.write('')

    # success
    file.rename(orig, 'test_duplicate_dest')
    assert dest.isfile()
    assert not orig.isfile()

def test_write(tmpdir):
    # setup
    path = tmpdir.join('test_write.txt')

    # success
    file.write(path, 'test_write')
    assert path.read() == 'test_write\n'
