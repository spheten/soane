'''
Tests for 'soane.items.note'.
'''

import pytest

from soane.items.note import Note

@pytest.fixture(scope='function')
def note(temp_dire):
    return Note(temp_dire + '/alpha.txt')

def test_init(note):
    # success
    assert note.path.endswith('alpha.txt')
    assert note.name == 'alpha'

def test_contains(note):
    # success
    assert 'Alpha' in note
    assert 'nope' not in note

def test_eq(note):
    # success
    assert note == note
    assert note != Note('/nope.txt')
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
    note.path = '/alpha.txt'

    # success
    assert repr(note) == "Note('/alpha.txt')"

def test_delete(note):
    # success
    note.delete()
    assert not note.exists()

def test_exists(note):
    # success
    assert note.exists()
    assert not Note('/nope.txt').exists()

def test_match(note):
    # success
    assert note.match('alph?')
    assert not note.match('nope')

def test_read(note):
    # success
    assert note.read() == 'Alpha note.\n'

def test_move(note):
    # success
    note.move('move')
    assert note.path.endswith('move.txt')
    assert note.name == 'move'

def test_search(note):
    # success
    assert note.search('alpha')
    assert not note.search('nope')

def test_write(note):
    # success
    note.write('body')
    assert note.read() == 'body\n'
