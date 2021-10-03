'''
Command group definition for 'soane'.
'''

import click

from soane.items import Book
from soane       import tools

DEFAULT_PATH = tools.path.expand('~/.soane')

@click.group()
@click.option('--path',
    envvar  = 'SOANE_PATH',
    default = DEFAULT_PATH,
    hidden  = True,
    type    = click.Path(
        exists   = True,
        dir_okay = False,
        readable = True,
        writable = True,
        resolve_path = True,
    ),
)
@click.pass_context
def soane(ctx, path):
    '''
    Soane: Stephen's Old-Ass Note Engine.
    '''

    if not getattr(ctx, 'obj', None):
        ctx.obj = Book(path)
