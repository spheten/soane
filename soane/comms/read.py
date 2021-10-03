'''
Command definition for 'read'.
'''

import click

from soane.comms._base import soane
from soane.tools.clui  import NAME

@soane.command(short_help='Print a note.')
@click.argument('name', type=NAME)
@click.pass_obj
def read(book, name):
    '''
    Print note NAME if it exists.
    '''

    if note := book.read(name):
        click.echo(note.read().strip() + '\n')
