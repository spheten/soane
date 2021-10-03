'''
Command-line user interface functions.
'''

import getopt
import sys

from soane import VERSION_NUMBER

COMMANDS = [
    ('C', 'Create', ['NOTE', 'TEXT'], 'Create NOTE with TEXT.'),
    ('D', 'Delete', ['NOTE'],         'Delete NOTE.'),
    ('E', 'Edit',   ['NOTE'],         'Open NOTE in editor.'),
    ('H', 'Help',   [],               'Show this help message.'),
    ('M', 'Match',  ['NOTE'],         'List notes matching GLOB.'),
    ('R', 'Read',   ['NOTE'],         'Print NOTE.'),
    ('S', 'Search', ['NOTE'],         'List notes containing TEXT.'),
    ('U', 'Update', ['NOTE', 'TEXT'], 'Update NOTE with TEXT.'),
]

OPTIONS = [
    ('f', 'force',   [], 'Force all yes/no prompts.'),
    ('q', 'quiet',   [], 'Do not print output.'),
    ('v', 'verbose', [], 'Print verbose output.'),
]

HELP_TEMPLATE = '''
Soane: Stephen's Old-Ass Note Engine (version {VERSION}).

Commands:
{commands}

Options:
{options}

See github.com/spheten/soane for help & info.
'''

def parse_args(args=None):
    '''
    Return a dict of parsed command-line arguments.
    '''

    pairs, nargs = getopt.getopt(
        args or sys.argv[1:],
        ''.join(line[0] for line in COMMANDS + OPTIONS),
        [line[1] for line in COMMANDS + OPTIONS],
    )

    parsed = {}
    for char, name, pams, desc in COMMANDS:
        for opt, val in pairs:
            if opt in [f'-{char}', f'--{name}']:
                parsed['command']   = name
                parsed['arguments'] = dict(zip(pams, nargs[:len(pams)]))

    for char, name, size, desc in OPTIONS:
        parsed[name] = False
        for opt, val in pairs:
            if opt in [f'-{char}', f'--{name}']:
                parsed[name] = True

    return parsed

def generate_help():
    '''
    Return a generated command-line help message.
    '''

    commands = []
    options  = []

    for char, name, pams, desc in COMMANDS:
        pref = f'\t-{char} --{name} {" ".join(pams)}'
        line = f'{pref.rstrip() + ":":<23} {desc}'
        commands.append(line)

    for char, name, pams, desc in OPTIONS:
        pref = f'\t-{char} --{name}'
        line = f'{pref + ":":<16} {desc}'
        options.append(line)

    return HELP_TEMPLATE.format(
        commands = '\n'.join(commands),
        options  = '\n'.join(options),
        VERSION  = VERSION_NUMBER,
    ).strip() + '\n'
