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

    def __contains__(self, name):
        '''
        Return True if the Book contains a named Note.
        '''

        return name in self.read()

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
        Return a named Note in the Book using dict syntax.
        '''

        return self.read()[name]

    def __hash__(self):
        '''
        Return the Book's unique hash code.
        '''

        return hash('Book:' + self.path)

    def __iter__(self):
        '''
        Yield each Note in the Book in alphabetical order.
        '''

        key = lambda note: note.name
        yield from sorted(self.read().values(), key=key)

    def __len__(self):
        '''
        Return the number of Notes in the Book.
        '''

        return len(self.read())

    def __repr__(self):
        '''
        Return the Book as a code-representative string.
        '''

        return f'Book({self.path!r})'

    def create(self, name, body):
        '''
        Create and return a new Note in the Book.
        '''

        if tools.zips.exists(self.path, name):
            raise FileExistsError(f'{name!r} already exists in zip {self.path!r}')

        tools.zips.append(self.path, name, body)
        return Note(self.path, name)

    def exists(self):
        '''
        Return True if the Book's zipfile exists on disk.
        '''

        return os.path.isfile(self.path)

    def get(self, name, dflt=None):
        '''
        Return a named Note in the Book, or a default value.
        '''

        return self.read().get(name, dflt)

    def read(self):
        '''
        Return a '{name: Note}' dict of all Notes in the Book.
        '''

        names = tools.zips.list_names(self.path)
        return {name: Note(self.path, name) for name in names}

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
