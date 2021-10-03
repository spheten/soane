'''
Tests for 'soane.tools.clui'.
'''

from soane.tools import clui

clui.COMMANDS.append(('T', 'Test', ['TEXT'], 'Run test with TEXT.'))

def test_parse_args():
    # success - short options
    assert clui.parse_args(['-Tq', 'foo']) == {
        'command':   'Test',
        'arguments': {'TEXT': 'foo'},
        'force':     False,
        'quiet':     True,
        'verbose':   False,
    }

    # success - long options
    assert clui.parse_args(['--Test', '--quiet', 'foo']) == {
        'command':   'Test',
        'arguments': {'TEXT': 'foo'},
        'force':     False,
        'quiet':     True,
        'verbose':   False,
    }

def test_generate_help():
    # success
    assert clui.generate_help()
