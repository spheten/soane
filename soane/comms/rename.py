'''
Command definition for 'rename'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'rename',
    short_help = 'Rename a note.',
    add_help_option = False,
)
@click.argument('name')
@click.argument('dest')
@click.help_option('-h', '--help')
@click.pass_obj
def rename(book, name, dest):
    '''
    Rename the note NAME to DEST.
    '''

    if note := book.read(name):
        if dest in book:
            click.echo(f'Error: the note {dest!r} already exists.')
        else:
            note.rename(dest)
    else:
        click.echo(f'Error: the note {name!r} does not exist.')
