'''
Command definition for 'read'.
'''

import click

from soane.comms._base import group
from soane             import tools

@group.command(
    short_help = 'Print a note.',
)
@click.argument('name',
    type = tools.clui.NAME,
)
@click.pass_obj
def read(book, name):
    '''
    Print note NAME if it exists.
    '''

    if note := book.read(name):
        click.echo(note.read().strip() + '\n')
