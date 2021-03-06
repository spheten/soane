'''
Command definition for 'create'.
'''

import click

from soane.comms._base import group

@group.command(
    name       = 'create',
    short_help = 'Create a note.',
    add_help_option = False,
)
@click.argument('name')
@click.option('-o', '--open-after',
    help    = 'Open after creation.',
    is_flag = True,
)
@click.help_option('-h', '--help')
@click.pass_obj
def create(book, name, open_after):
    '''
    Create the empty note NAME.
    '''

    if name in book:
        raise click.ClickException(f'the note {name!r} already exists.')

    note = book.create(name)
    if open_after:
        click.launch(note.path)
