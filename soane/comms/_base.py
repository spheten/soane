'''
Click command group definition.
'''

import os

import click

from soane.items import Book
from soane       import tools

@click.group(
    cls = tools.clui.AbbrGroup,
)
@click.pass_context
def group(ctx):
    '''
    Soane: Stephen's Old-Ass Note Engine.
    '''

    if not getattr(ctx, 'obj', None):
        dire = os.environ.get('SOANE_DIR', '').strip()
        ext  = os.environ.get('SOANE_EXT', '').strip()

        if dire and ext:
            ctx.obj = Book(dire, ext)
        elif not dire:
            ctx.fail('SOANE_DIR environment variable not set.')
        elif not ext:
            ctx.fail('SOANE_EXT environment variable not set.')
