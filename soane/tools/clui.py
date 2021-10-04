'''
Command-line user interface classes and functions.
'''

import click

from soane import tools

class BookType(click.ParamType):
    '''
    A custom parameter type for Book paths.
    '''

    name = 'book'

    def convert(self, value, param, ctx):
        '''
        Convert a raw value into a Book path.
        '''

        path = tools.path.expand(value)
        if not tools.path.exists(path):
            self.fail(f'Book path {path!r} does not exist')

        return path

class NameType(click.ParamType):
    '''
    A custom parameter type for Note names.
    '''

    name = 'name'

    def convert(self, value, param, ctx):
        '''
        Convert a raw value into a Note name.
        '''

        slug = tools.path.slug(value)
        if slug == '':
            self.fail(f'Note name {value!r} slugs to empty string')

        return slug

BOOK = BookType()
NAME = NameType()
