'''
Class definition for 'Book'.
'''

import os.path

from soane            import tools
from soane.items.note import Note
from soane.items.zipf import ZipFile

class Book:
    '''
    A ZipFile containing plaintext Notes.
    '''

    addr_ext  = 'txt'
    __slots__ = ['path', 'zipf']

    def __init__(self, path):
        '''
        Initialise a new Book.
        '''

        self.path = tools.path.clean(path)
        self.zipf = ZipFile(self.path)

    def __contains__(self, name):
        '''
        Return True if the Book contains a Note.
        '''

        return self.addr(name) in self.zipf

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
        Return a Note from the Book using dict syntax.
        '''

        if name in self:
            return self.read(name)
        else:
            raise tools.errs.addr_not_exists(self.path, self.addr(name))

    def __hash__(self):
        '''
        Return the Book's unique hash code.
        '''

        return hash('Book:' + self.path)

    def __iter__(self):
        '''
        Yield each Note in the Book.
        '''

        for addr in self.zipf:
            yield Note(self.path, addr)

    def __len__(self):
        '''
        Return the number of Notes in the Book.
        '''

        return len(self.zipf)

    def __repr__(self):
        '''
        Return the Book as a code-representative string.
        '''

        return f'Book({self.path!r})'

    def addr(self, name):
        '''
        Return a Note name as a ZipFile address.
        '''

        name = tools.path.slug(name)
        return f'{name}.{self.__class__.addr_ext}'

    def create(self, name, body):
        '''
        Create and return a new Note in the Book.
        '''

        addr = self.addr(name)
        if self.zipf.exists(addr):
            raise tools.errs.addr_exists(self.path, addr)

        self.zipf.create(addr, body)
        return Note(self.path, addr)

    def exists(self, name):
        '''
        Return True if a Note exists in the Book.
        '''

        return self.addr(name) in self.zipf

    def read(self, name, default=None):
        '''
        Return a Note from the Book, or a default value.
        '''

        addr = self.addr(name)
        if self.zipf.exists(addr):
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
