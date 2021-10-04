'''
Tests for 'soane.comms.list'.
'''

from soane.comms.list import list_

def test_read(cli):
    # success - default GLOB
    assert cli(list_) == [
        'alpha\n',
        'bravo\n',
        'charlie\n',
    ]

    # success - custom GLOB
    assert cli(list_, 'a*') == [
        'alpha\n',
    ]
