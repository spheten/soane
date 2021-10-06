'''
Tests for 'soane.tools.file'.
'''

import pytest

from soane.tools import file

def test_create(tmpdir):
    # setup
    path = tmpdir.join('test.txt')

    # success
    file.create(path, 'body')
    assert path.read() == 'body\n'

def test_delete(tmpdir):
    # setup
    path = tmpdir.join('test.txt')
    path.write('')

    # success
    file.delete(path)
    assert not path.exists()

def test_duplicate(tmpdir):
    # setup
    orig = tmpdir.join('orig.txt')
    dest = tmpdir.join('dest.txt')
    orig.write('')

    # success
    file.duplicate(orig, 'dest')
    assert orig.isfile()
    assert dest.isfile()

def test_exists(tmpdir):
    # setup
    path = tmpdir.join('test.txt')
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
    path = tmpdir.join('test.txt')
    path.write('body')

    # success
    assert file.read(path) == 'body\n'

def test_rename(tmpdir):
    # setup
    orig = tmpdir.join('orig.txt')
    dest = tmpdir.join('dest.txt')
    orig.write('')

    # success
    file.rename(orig, 'dest')
    assert not orig.isfile()
    assert dest.isfile()

def test_write(tmpdir):
    # setup
    path = tmpdir.join('test.txt')

    # success
    file.write(path, 'body')
    assert path.read() == 'body\n'
