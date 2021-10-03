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
    assert 'alpha.txt' in book
    assert not 'nope'  in book

def test_eq(book):
    # success
    assert book == book
    assert Book != Book('nope')
    assert Book != 'not a Book'

def test_getitem(book):
    # success
    assert book['alpha.txt'] == book.read()['alpha.txt']

def test_hash(book):
    # success
    assert {book, book} == {book}

def test_iter(book):
    # success
    assert set(book) == {
        book['alpha.txt'],
        book['bravo.txt'],
        book['charlie.txt'],
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
    book.create('test.txt', 'test_create')
    assert_zip_file(book.path, 'test.txt', 'test_create\n')

    # failure - existing name
    with pytest.raises(FileExistsError):
        book.create('alpha.txt', 'test_create')

def test_exists(book):
    # success
    assert     book.exists()
    assert not Book('nope').exists()

def test_get(book):
    # success
    assert book.get('alpha.txt', 'test') == book['alpha.txt']
    assert book.get('nope.txt',  'test') == 'test'

def test_read(book):
    # success
    assert book.read() == {
        'alpha.txt':   book['alpha.txt'],
        'bravo.txt':   book['bravo.txt'],
        'charlie.txt': book['charlie.txt'],
    }

def test_match(book):
    # success
    assert list(book.match('alph?')) == [book['alpha.txt']]

def test_search(book):
    # success
    assert list(book.search('alpha')) == [book['alpha.txt']]
