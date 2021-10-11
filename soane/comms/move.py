'''
Command definition for 'move'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'move',
    short_help = 'Rename a note.',
    add_help_option = False,
)
@click.argument('name')
@click.argument('dest')
@click.help_option('-h', '--help')
@click.pass_obj
def move(book, name, dest):
    '''
    Rename the note NAME to DEST.
    '''

    if name not in book:
        raise click.ClickException(f'the note {name!r} does not exist.')

    if dest in book:
        raise click.ClickException(f'the note {dest!r} already exists.')

    note = book.read(name)
    note.move(dest)
