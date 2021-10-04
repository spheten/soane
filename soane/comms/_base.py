'''
Click command group definition.
'''

import os

import click

from soane       import tools
from soane       import VERSION_STRING
from soane.items import Book

@click.group(
    cls = tools.clui.AbbrGroup,
    add_help_option = False,
)
@click.help_option('-h', '--help')
@click.version_option('', '-v', '--version',
    message = VERSION_STRING,
)
@click.pass_context
def group(ctx):
    '''
    Soane: Stephen's Old-Ass Note Engine.
    '''

    if not getattr(ctx, 'obj', None):
        dire = os.environ.get('SOANE_DIR', '').strip()
        ext  = os.environ.get('SOANE_EXT', '').strip()

        if not dire:
            ctx.fail('SOANE_DIR environment variable not set.')
        elif not ext:
            ctx.fail('SOANE_EXT environment variable not set.')

        ctx.obj = Book(dire, ext)
        if not ctx.obj.exists():
            ctx.fail('Configured notes directory does not exist.')
