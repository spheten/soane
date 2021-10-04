'''
Class definition for 'Book'.
'''

from soane            import tools
from soane.items.note import Note

class Book:
    '''
    A directory containing plaintext Notes.
    '''

    __slots__ = ['dire', 'ext']

    def __init__(self, path, ext):
        '''
        Initialise a new Book.
        '''

        self.dire = tools.path.clean(path)
        self.ext  = str(ext).strip().lstrip('.')

    def __contains__(self, name):
        '''
        Return True if the Book contains a Note.
        '''

        path = tools.path.join(self.dire, f'{name}.{self.ext}')
        return tools.file.exists(path)

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

        for path in tools.file.glob(self.dire, f'*.{self.ext}'):
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

    def create(self, name):
        '''
        Create and return a new empty Note in the Book.
        '''

        path = tools.path.join(self.dire, f'{name}.{self.ext}')

        if tools.file.exists(path):
            raise FileExistsError(f'Note file {path} already exists')

        note = Note(path)
        note.write('')
        return note

    def exists(self):
        '''
        Return True if the Book's directory exists.
        '''

        return tools.file.exists(self.dire, dire=True)

    def read(self, name, default=None):
        '''
        Return a Note from the Book, or a default value.
        '''

        path = tools.path.join(self.dire, f'{name}.{self.ext}')

        if tools.file.exists(path):
            return Note(path)
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
