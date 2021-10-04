'''
Class definition for 'Note'.
'''

import fnmatch

from soane            import tools
from soane.items.zipf import ZipFile

class Note:
    '''
    A plaintext note file in a zipfile.
    '''

    __slots__ = ['path', 'zipf', 'addr', 'name']

    def __init__(self, path, addr):
        '''
        Initialise a new Note.
        '''

        self.path = tools.path.clean(path)
        self.zipf = ZipFile(self.path)
        self.addr = tools.path.clean(addr)
        self.name = tools.path.name(addr)

    def __eq__(self, note):
        '''
        Return True if the Note is equal to another Note.
        '''

        return all([
            isinstance(note, Note),
            self.path == getattr(note, 'path', None),
            self.addr == getattr(note, 'addr', None),
        ])

    def __hash__(self):
        '''
        Return the Note's unique hash code.
        '''

        return hash('Note:' + self.path + self.addr)

    def __iter__(self):
        '''
        Yield each line in the Note's body.
        '''

        yield from self.read().splitlines(keepends=True)

    def __len__(self):
        '''
        Return the size of the Note's body.
        '''

        return len(self.read())

    def __repr__(self):
        '''
        Return the Note as a code-representative string.
        '''

        return f'Note({self.path!r}, {self.addr!r})'

    def exists(self):
        '''
        Return True if the Note exists in the zipfile.
        '''

        return self.zipf.exists(self.addr)

    def match(self, glob):
        '''
        Return True if the Note's name matches a glob pattern.
        '''

        return fnmatch.fnmatch(self.name, glob)

    def read(self):
        '''
        Return the Note's body as a string.
        '''

        return self.zipf.read(self.addr)

    def search(self, text):
        '''
        Return True if the Note's body contains a substring.
        '''

        return text.lower().strip() in self.read().lower()

    def update(self, body):
        '''
        Overwrite the Note's body with a string.
        '''

        self.zipf.update(self.addr, body)
