'''
Tests for 'soane.items.note'.
'''

import pytest

from soane.items.note import Note
from tests.conftest   import assert_zip_file

@pytest.fixture(scope='function')
def note(zpath):
    return Note(zpath, 'alpha.txt')

def test_init(note):
    # success
    assert note.path
    assert note.addr == 'alpha.txt'
    assert note.name == 'alpha'

def test_contains(note):
    # success
    assert 'Alpha' in note
    assert 'nope' not in note

def test_eq(note):
    # success
    assert note == note
    assert note != Note('nope.zip', 'nope.txt')
    assert note != 'not a Note'

def test_hash(note):
    # success
    assert {note, note} == {note}

def test_iter(note):
    # success
    assert list(note) == ['Alpha note.\n']

def test_len(note):
    # success
    assert len(note) == 12

def test_repr(note):
    # setup
    note.path = '/test.zip'

    # success
    assert repr(note) == "Note('/test.zip', 'alpha.txt')"

def test_exists(note):
    # success
    assert note.exists()
    assert not Note(note.path, 'nope').exists()

def test_match(note):
    # success
    assert note.match('alph?')
    assert not note.match('nope')

def test_read(note):
    # success
    assert note.read() == 'Alpha note.\n'

def test_search(note):
    # success
    assert note.search('alpha')
    assert not note.search('nope')

def test_update(note):
    # success
    note.update('test_update')
    assert_zip_file(note.path, 'alpha.txt', 'test_update\n')
