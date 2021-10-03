'''
Class definition for 'Note'.
'''

import fnmatch

from soane import tools

class Note:
    '''
    A plaintext note file in a zipfile.
    '''

    __slots__ = ['path', 'name', 'stem']

    def __init__(self, path, name):
        '''
        Initialise a new Note.
        '''

        self.path = path
        self.name = name
        self.stem = tools.path.stem(name)

    def __eq__(self, note):
        '''
        Return True if the Note is equal to another Note.
        '''

        return all([
            isinstance(note, Note),
            self.path == getattr(note, 'path', None),
            self.name == getattr(note, 'name', None),
        ])

    def __hash__(self):
        '''
        Return the Note's unique hash code.
        '''

        return hash(self.path + self.name)

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

        return f'Note({self.path!r}, {self.name!r})'

    def exists(self):
        '''
        Return True if the Note exists in its zipfile.
        '''

        return tools.zips.exists(self.path, self.name)

    def match(self, glob):
        '''
        Return True if the Note's stem matches a glob pattern.
        '''

        return fnmatch.fnmatch(self.stem, glob)

    def read(self):
        '''
        Return the Note's body as a string.
        '''

        return tools.zips.read(self.path, self.name)

    def search(self, text):
        '''
        Return True if the Note's body contains a substring.
        '''

        return text.lower().strip() in self.read().lower()

    def update(self, body):
        '''
        Overwrite the Note's body with a string.
        '''

        tools.zips.write(self.path, self.name, body)
