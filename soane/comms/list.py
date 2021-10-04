'''
Command definition for 'list'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'list',
    short_help = 'List notes.',
    add_help_option = False,
)
@click.help_option('-h', '--help')
@click.argument('glob',
    default  = '*',
    required = False,
)
@click.pass_obj
def list_(book, glob):
    '''
    List all notes or notes matching GLOB.
    '''

    for note in book.match(glob):
        click.echo(note.name)
