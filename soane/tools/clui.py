'''
Command-line user interface classes and functions.
'''

import click

class AbbrGroup(click.Group):
    '''
    A custom Group type that supports abbreviated commands.
    '''

    def get_command(self, ctx, comm_name):
        '''
        Return a Command from a complete or abbreviated name.
        '''

        names = [
            name for name in self.list_commands(ctx)
            if name.startswith(comm_name)
        ]

        if not names:
            return None
        elif len(names) == 1:
            return super().get_command(ctx, names[0])
        else:
            ambi = ', '.join(sorted(names))
            ctx.fail(f'Ambiguous abbreviation, did you mean: {ambi}?')
