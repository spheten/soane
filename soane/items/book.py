'''
Class definition for 'Book'.
'''

from soane            import tools
from soane.items.note import Note

class Book:
    '''
    A ZipFile containing plaintext Notes.
    '''

    __slots__ = ['dire']
    note_ext  = 'txt'

    def __init__(self, path):
        '''
        Initialise a new Book.
        '''

        self.dire = tools.path.clean(path)

    def __contains__(self, name):
        '''
        Return True if the Book contains a Note.
        '''

        for note in self:
            if name == note.name:
                return True
        return False

    def __eq__(self, book):
        '''
        Return True if the Book is equal to another Book.
        '''

        return all([
            isinstance(book, Book),
            self.dire == getattr(book, 'dire', None),
        ])

    def __getitem__(self, name):
        '''
        Return a Note from the Book using dict syntax.
        '''

        if name in self:
            return self.read(name)
        else:
            raise KeyError(name)

    def __hash__(self):
        '''
        Return the Book's unique hash code.
        '''

        return hash('Book:' + self.dire)

    def __iter__(self):
        '''
        Yield each Note in the Book.
        '''

        term = f'*.{self.__class__.note_ext}'
        for path in tools.file.glob(self.dire, term):
            yield Note(path)

    def __len__(self):
        '''
        Return the number of Notes in the Book.
        '''

        return len(list(self.__iter__()))

    def __repr__(self):
        '''
        Return the Book as a code-representative string.
        '''

        return f'Book({self.dire!r})'

    def create(self, name, body):
        '''
        Create and return a new Note in the Book.
        '''

        base = f'{name}.{self.__class__.note_ext}'
        path = tools.path.join(self.dire, base)

        if name in self:
            raise FileExistsError(f'file {path} already exists')

        note = Note(path)
        note.write(body)
        return note

    def read(self, name, default=None):
        '''
        Return a Note from the Book, or a default value.
        '''

        for note in self:
            if note.name == name:
                return note
        return default

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
