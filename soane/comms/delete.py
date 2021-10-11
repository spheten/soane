'''
Command definition for 'delete'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'delete',
    short_help = 'Delete a note.',
    add_help_option = False,
)
@click.argument('name')
@click.help_option('-h', '--help')
@click.pass_obj
def delete(book, name):
    '''
    Send the note NAME to your system trash.
    '''

    if name not in book:
        raise click.ClickException(f'the note {name!r} does not exist.')

    note = book.read(name)
    note.delete()
