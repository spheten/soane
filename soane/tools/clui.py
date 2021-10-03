'''
Command-line user interface classes and functions.
'''

import click

from soane import tools

NAME_EXTENSION = 'txt'

class NameType(click.ParamType):
    '''
    A custom parameter type for Note names.
    '''

    name = 'slug'

    def convert(self, value, param, ctx):
        '''
        Convert a raw value into a Note name.
        '''

        slug = tools.path.slug(value)
        if slug == '':
            self.fail(f'note name {value!r} slugs to empty string')
        else:
            return f'{slug}.{NAME_EXTENSION}'

NAME = NameType()
