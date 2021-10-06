'''
Command definition for 'read'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'read',
    short_help = 'Print a note.',
    add_help_option = False,
)
@click.argument('name')
@click.help_option('-h', '--help')
@click.pass_obj
def read(book, name):
    '''
    Print the note NAME if it exists.
    '''

    if note := book.read(name):
        click.echo(note.read().strip())
