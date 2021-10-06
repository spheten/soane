'''
Command-line user interface classes and functions.
'''

import click

from soane import tools

class AbbrGroup(click.Group):
    '''
    A custom Group type that supports abbreviated commands.
    '''

    def get_command(self, ctx, name):
        '''
        Return a Command from a complete or abbreviated name.
        '''

        comms = self.list_commands(ctx)
        names = tools.text.disambiguate(name, comms)

        if not names:
            return None
        elif len(names) == 1:
            return super().get_command(ctx, names[0])
        else:
            ambi = ', '.join(sorted(names))
            ctx.fail(f'Ambiguous abbreviation, did you mean: {ambi}?')
