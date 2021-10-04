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
@click.help_option('-h', '--help')
@click.argument('name')
@click.pass_obj
def open_(book, name):
    '''
    Open the note NAME in your default editor.
    '''

    if note := book.read(name):
        click.launch(note.path)
    else:
        click.echo(f'Error: the note {name!r} does not exist.')
