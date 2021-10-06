'''
Class definition for 'Note'.
'''

from soane import tools

class Note:
    '''
    A plaintext note file in a directory.
    '''

    __slots__ = ['path', 'name']

    def __init__(self, path):
        '''
        Initialise a new Note.
        '''

        self.path = tools.path.clean(path)
        self.name = tools.path.name(self.path)

    def __contains__(self, string):
        '''
        Return True if the Note contains a substring.
        '''

        return string in self.read()

    def __eq__(self, note):
        '''
        Return True if the Note is equal to another Note.
        '''

        return all([
            isinstance(note, Note),
            self.path == getattr(note, 'path', None),
        ])

    def __hash__(self):
        '''
        Return the Note's unique hash code.
        '''

        return hash('Note:' + self.path)

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

        return f'Note({self.path!r})'

    def delete(self):
        '''
        Delete the Note's file by sending it to system trash.
        '''

        tools.file.delete(self.path)

    def exists(self):
        '''
        Return True if the Note's file exists.
        '''

        return tools.file.exists(self.path)

    def match(self, glob):
        '''
        Return True if the Note's name matches a glob pattern.
        '''

        return tools.text.glob(self.name, glob)

    def read(self):
        '''
        Return the Note's body as a string.
        '''

        return tools.file.read(self.path)

    def search(self, text):
        '''
        Return True if the Note's body contains a substring.
        '''

        return text.lower().strip() in self.read().lower()

    def write(self, body):
        '''
        Overwrite the Note's body with a string.
        '''

        tools.file.write(self.path, body)
