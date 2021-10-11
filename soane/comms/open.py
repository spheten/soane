'''
Command definition for 'open'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'open',
    short_help = 'Open a note.',
    add_help_option = False,
)
@click.argument('name')
@click.help_option('-h', '--help')
@click.pass_obj
def open_(book, name):
    '''
    Open the note NAME in your default editor.
    '''

    if name not in book:
        raise click.ClickException(f'the note {name!r} does not exist.')

    note = book.read(name)
    click.launch(note.path)
