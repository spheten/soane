'''
Tests for 'soane.items.book'.
'''

import pytest

from soane.items.book import Book
from soane.items.note import Note
from tests.conftest   import assert_zip_file

@pytest.fixture(scope='function')
def book(zpath):
    return Book(zpath)

def test_init(book):
    # success
    assert book.path

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
    assert book['alpha'] == book.read_dict()['alpha']

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
    book.path = '/test.zip'

    # success
    assert repr(book) == "Book('/test.zip')"

def test_create(book):
    # success
    book.create('test', 'test_create')
    assert_zip_file(book.path, 'test.txt', 'test_create\n')

    # failure - existing name
    with pytest.raises(FileExistsError):
        book.create('alpha', 'test_create')

def test_read(book):
    # success
    assert book.read('alpha', 'test') == book['alpha']
    assert book.read('nope',  'test') == 'test'

def test_read_dict(book):
    # success
    assert book.read_dict() == {
        'alpha':   book['alpha'],
        'bravo':   book['bravo'],
        'charlie': book['charlie'],
    }

def test_match(book):
    # success
    assert list(book.match('alph?')) == [book['alpha']]

def test_search(book):
    # success
    assert list(book.search('alpha')) == [book['alpha']]
