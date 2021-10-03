'''
Class definition for 'Note'.
'''

import fnmatch

from soane import tools

class Note:
    '''
    A plaintext note file in a zipfile.
    '''

    __slots__ = ['path', 'addr', 'name']

    def __init__(self, path, addr):
        '''
        Initialise a new Note.
        '''

        self.path = path
        self.addr = addr
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
        Return True if the Note exists in its zipfile.
        '''

        return tools.zips.exists(self.path, self.addr)

    def match(self, glob):
        '''
        Return True if the Note's name matches a glob pattern.
        '''

        return fnmatch.fnmatch(self.name, glob)

    def read(self):
        '''
        Return the Note's body as a string.
        '''

        return tools.zips.read(self.path, self.addr)

    def search(self, text):
        '''
        Return True if the Note's body contains a substring.
        '''

        return text.lower().strip() in self.read().lower()

    def update(self, body):
        '''
        Overwrite the Note's body with a string.
        '''

        tools.zips.update(self.path, self.addr, body)
