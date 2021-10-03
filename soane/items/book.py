'''
Class definition for 'Book'.
'''

import os.path

from soane            import tools
from soane.items.note import Note

class Book:
    '''
    A zipfile containing plaintext Notes.
    '''

    __slots__ = ['path']

    def __init__(self, path):
        '''
        Initialise a new Book.
        '''

        self.path = path

    def __contains__(self, addr):
        '''
        Return True if the Book contains a Note.
        '''

        return addr in self.read_dict().keys()

    def __eq__(self, book):
        '''
        Return True if the Book is equal to another Book.
        '''

        return all([
            isinstance(book, Book),
            self.path == getattr(book, 'path', None),
        ])

    def __getitem__(self, name):
        '''
        Return a Note in the Book using dict syntax.
        '''

        if note := self.read(name):
            return note
        else:
            raise KeyError(f'name {name!r} not in zip {self.path!r}')

    def __hash__(self):
        '''
        Return the Book's unique hash code.
        '''

        return hash('Book:' + self.path)

    def __iter__(self):
        '''
        Yield each Note in the Book.
        '''

        for addr in tools.zips.list_addrs(self.path):
            yield Note(self.path, addr)

    def __len__(self):
        '''
        Return the number of Notes in the Book.
        '''

        return len(self.read_dict().values())

    def __repr__(self):
        '''
        Return the Book as a code-representative string.
        '''

        return f'Book({self.path!r})'

    def create(self, name, body):
        '''
        Create and return a new Note in the Book.
        '''

        addr = f'{name}.txt'
        if tools.zips.exists(self.path, addr):
            raise FileExistsError(f'{addr!r} already exists in zip {self.path!r}')

        tools.zips.create(self.path, addr, body)
        return Note(self.path, addr)

    def exists(self):
        '''
        Return True if the Book's zipfile exists on disk.
        '''

        return os.path.isfile(self.path)

    def read(self, name, default=None):
        '''
        Return a Note from the Book, or a default value.
        '''

        for addr in tools.zips.list_addrs(self.path):
            if tools.path.name(addr) == name:
                return Note(self.path, addr)
        return default

    def read_dict(self):
        '''
        Return a name-to-note dict of all Notes in the Book.
        '''

        return {note.name: note for note in self}

    def match(self, glob):
        '''
        Yield each Note in the Book matching a glob pattern.
        '''

        yield from (note for note in self if note.match(glob))

    def search(self, text):
        '''
        Yield each Note in the Book containing a substring.
        '''

        yield from (note for note in self if note.search(text))
