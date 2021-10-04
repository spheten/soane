'''
Tests for 'soane.items.book'.
'''

import pytest

from soane.items.book import Book
from soane.items.note import Note

@pytest.fixture(scope='function')
def book(temp_dire):
    return Book(temp_dire)

def test_init(book):
    # success
    assert book.dire

def test_contains(book):
    # success
    assert 'alpha' in book
    assert 'nope' not in book

def test_eq(book):
    # success
    assert book == book
    assert Book != Book('nope')
    assert Book != 'not a Book'

def test_getitem(book):
    # success
    assert book['alpha'] == Note(book.dire + '/alpha.txt')

def test_hash(book):
    # success
    assert {book, book} == {book}

def test_iter(book):
    # success
    assert set(book) == {
        book['alpha'], book['bravo'],  book['charlie'],
    }

def test_len(book):
    # success
    assert len(book) == 3

def test_repr(book):
    # setup
    book.dire = '/dire'

    # success
    assert repr(book) == "Book('/dire')"

def test_create(book):
    # success
    note = book.create('delta', 'test_create')
    assert note.read() == 'test_create\n'

    # failure - existing name
    with pytest.raises(FileExistsError):
        book.create('alpha', 'test_create')

def test_read(book):
    # success
    assert book.read('alpha', 'test') == book['alpha']
    assert book.read('nope',  'test') == 'test'

def test_match(book):
    # success
    assert list(book.match('alph?')) == [book['alpha']]

def test_search(book):
    # success
    assert list(book.search('alpha')) == [book['alpha']]
