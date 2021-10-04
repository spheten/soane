'''
Click command group definition.
'''

import click

from soane.items import Book
from soane       import tools

DEFAULT_PATH = tools.path.expand('~/Dropbox/Notes')

@click.group(
    cls = tools.clui.AbbrGroup,
)
@click.pass_context
def group(ctx):
    '''
    Soane: Stephen's Old-Ass Note Engine.
    '''

    if not getattr(ctx, 'obj', None):
        ctx.obj = Book(DEFAULT_PATH)
