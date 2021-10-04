'''
Command group definition for 'soane'.
'''

import click

from soane.items import Book
from soane       import tools

DEFAULT_PATH = tools.path.expand('~/.soane')

@click.group(cls=tools.clui.AbbrGroup)
@click.option('--path',
    envvar  = 'SOANE_PATH',
    default = DEFAULT_PATH,
    hidden  = True,
    type    = tools.clui.BOOK,
)
@click.pass_context
def soane(ctx, path):
    '''
    Soane: Stephen's Old-Ass Note Engine.
    '''

    if not getattr(ctx, 'obj', None):
        ctx.obj = Book(path)
