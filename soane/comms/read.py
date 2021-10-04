'''
Command definition for 'read'.
'''

import click

from soane.comms._base import group

@group.command(
    short_help = 'Print a note.',
)
@click.argument('name')
@click.pass_obj
def read(book, name):
    '''
    Print the note NAME if it exists.
    '''

    if note := book.read(name):
        click.echo(note.read().strip())
