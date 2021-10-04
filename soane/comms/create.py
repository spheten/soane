'''
Command definition for 'create'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'create',
    short_help = 'Create a note.',
    add_help_option = False,
)
@click.help_option('-h', '--help')
@click.argument('name')
@click.pass_obj
def create(book, name):
    '''
    Create the empty note NAME.
    '''

    if name not in book:
        book.create(name)
    else:
        raise click.UsageError(f'The note {name!r} already exists.')
