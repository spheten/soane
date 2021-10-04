'''
Command-line user interface classes and functions.
'''

import click

from soane import tools

class AbbrGroup(click.Group):
    '''
    A custom Group type that supports abbreviated commands.
    '''

    def get_command(self, ctx, comm_name):
        '''
        Return a Command from a complete or abbreviated name.
        '''

        names = [
            name for name in self.list_commands(ctx)
            if name.startswith(comm_name)
        ]

        if not names:
            return None
        elif len(names) == 1:
            return super().get_command(ctx, names[0])
        else:
            ambi = ', '.join(sorted(names))
            ctx.fail(f'Ambiguous abbreviation, did you mean: {ambi}?')


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
